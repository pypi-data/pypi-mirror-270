from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
from playhouse.shortcuts import model_to_dict, dict_to_model

import base64
import json
import threading
import asyncio
import os
import pymysql
import sys

from .interpreter.interpreter import TelliBot
from . import model
from .argparse import ArgParse

parser = ArgParse(argument_space_count=20, usage="gasper [path] [options]")
parser.add_argument(["--help"], description="show help", is_flag=True)
parser.add_argument(["--host", "-h"], description="mysql host")
parser.add_argument(["--username", "-u"], description="mysql username")
parser.add_argument(["--password", "-p"], description="mysql password")
parser.add_argument(["--port"], description="mysql server port")
args = parser.parse()

if args.help:
    parser.print_help()
    sys.exit(0)

password = ""
if args.password:
   password = args.password

host = "localhost"
if args.host:
    host = args.host

username = "root"
if args.username:
    username = args.username
    
port = "3306"
if args.port:
    port = args.port

conn = pymysql.connect(host=host, user=username, passwd=password, port=int(port))
cursor = conn.cursor()
cursor.execute(f"CREATE DATABASE IF NOT EXISTS tellibot;")
cursor.close()
conn.close()


app = Flask(__name__)
socketio = SocketIO(app)
bots = {}

SCRIPT_FOLDER_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates", "scripts")


@app.before_request
def before_request():
    model.initialize_db()


@app.after_request
def after_request(response):
    model.close_db()
    return response

@app.route("/")
def index():
    scripts = [model_to_dict(x) for x in model.Script.select().order_by(model.Script.id.desc())]
    for s in scripts:
        s["is_running"] = s["uid"] in bots
    return render_template("index.html", scripts=scripts)


@app.route("/editor")
def editor():
    name = request.args.get("name", None)
    uid = request.args.get("uid", None)
    
    if name is None or uid is None:
        return "<pre>Unable to process</pre>"

    workspace = None
    if os.path.exists(os.path.join(SCRIPT_FOLDER_PATH, f"{uid}.tel")):
        with open(os.path.join(SCRIPT_FOLDER_PATH, f"{uid}.tel"), "r") as f:
            workspace = f.read()
    else:
        model.Script.create(title=name, uid=uid)
        
    is_running = uid in bots
    
    return render_template("editor/index.html", title=name, uid=uid, workspace=workspace, is_running=is_running)

@app.route("/save", methods=["POST"])
def save():
    uid = request.form.get("uid", None)
    content = request.form.get("content", None)
    if uid is None or content is None:
        return "fail"
    
    with open(os.path.join(SCRIPT_FOLDER_PATH, f"{uid}.tel"), "w+") as f:
        f.write(content)
        
    return "ok"


@app.route("/run/<uid>")
def run(uid):
    if os.path.exists(os.path.join(SCRIPT_FOLDER_PATH, f"{uid}.tel")):
        with open(os.path.join(SCRIPT_FOLDER_PATH, f"{uid}.tel"), "r") as f:
            if uid in bots:
                asyncio.run_coroutine_threadsafe(bots[uid].stop_bot(), bots[uid].loop)
                bots.pop(uid)

            workspace = f.read()
            socketio.emit("is_running_" + uid, "running", namespace=None)
            threading.Thread(target=run_bot, args=(uid,workspace)).start()
    return "ok"


@app.route("/stop/<uid>")
def stop(uid):
    asyncio.run_coroutine_threadsafe(bots[uid].stop_bot(), bots[uid].loop)
    bots.pop(uid)
    socketio.emit("is_running_" + uid, "stopped", namespace=None)
    return "ok"


def run_bot(uid, data):
    telli = TelliBot(lambda s: socketio.emit(uid, s, namespace=None))
    bots[uid] = telli
    code = json.loads(base64.b64decode(json.loads(base64.b64decode(data))["code"]))
    telli.run(json.dumps(code))

# @app.route('/test')
# def test():
#     with open("tmp.tel", "r") as f:
#         data1 = f.read()
        
#     with open("tmp1.tel", "r") as f:
#         data2 = f.read()

#     # run(data)
#     threading.Thread(target=run, args=(data1,)).start()
#     threading.Thread(target=run, args=(data2,)).start()
#     return render_template('tmp.html')

@socketio.on('message')
def handle_message(message):
    emit('response', 'You said: ' + message)
    


def main():
    socketio.run(app, debug=True)

if __name__ == '__main__':
    main()
