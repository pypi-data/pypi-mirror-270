import json
import sys
import base64
import requests
import urllib.parse
import threading
import asyncio

from telegram import Bot
from telegram.ext import Application
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import filters
from telegram import ReplyKeyboardMarkup

from .interpreter.util import color

# Bot
from .interpreter.statements.bot_set_token import bot_set_token
from .interpreter.statements.bot_set_username import bot_set_username
from .interpreter.statements.bot_set_admin_username import bot_set_admin_username
from .interpreter.statements.bot_admin_word import bot_admin_word
from .interpreter.statements.bot_wait_for import bot_wait_for
from .interpreter.statements.bot_set_buttons import bot_set_buttons
from .interpreter.statements.bot_send_response import bot_send_response
from .interpreter.statements.bot_def_command import bot_def_command
from .interpreter.statements.bot_handle_message import bot_handle_message
from .interpreter.statements.bot_handle_admin_message import bot_handle_admin_message

# Database
from .interpreter.statements.db_connect import db_connect
from .interpreter.statements.db_create_table import db_create_table
from .interpreter.statements.db_delete_table import db_delete_table
from .interpreter.statements.db_insert import db_insert
from .interpreter.statements.db_read import db_read
from .interpreter.statements.db_delete_data import db_delete_data
from .interpreter.statements.db_update import db_update

# Logic
from .interpreter.statements.logic_controls_if import logic_controls_if
from .interpreter.statements.logic_compare import logic_compare
from .interpreter.statements.logic_operation import logic_operation
from .interpreter.statements.logic_negate import logic_negate
from .interpreter.statements.logic_boolean import logic_boolean
from .interpreter.statements.logic_confirm import logic_confirm
from .interpreter.statements.logic_ternary import logic_ternary

# Loops
from .interpreter.statements.controls_repeat_ext import controls_repeat_ext
from .interpreter.statements.controls_whileUntil import controls_whileUntil
from .interpreter.statements.controls_for import controls_for
from .interpreter.statements.controls_forEach import controls_forEach
from .interpreter.statements.controls_flow_statements import controls_flow_statements

# Math
from .interpreter.statements.math_number import math_number
from .interpreter.statements.math_arithmetic import math_arithmetic
from .interpreter.statements.math_single import math_single
from .interpreter.statements.math_trig import math_trig
from .interpreter.statements.math_constant import math_constant
from .interpreter.statements.math_number_property import math_number_property
from .interpreter.statements.math_convert_text_to_number import math_convert_text_to_number
from .interpreter.statements.math_round import math_round
from .interpreter.statements.math_on_list import math_on_list
from .interpreter.statements.math_modulo import math_modulo
from .interpreter.statements.math_constrain import math_constrain
from .interpreter.statements.math_random_int import math_random_int
from .interpreter.statements.math_random_float import math_random_float

# Text
from .interpreter.statements.text import text
from .interpreter.statements.text_join import text_join
from .interpreter.statements.text_append import text_append
from .interpreter.statements.text_length import text_length
from .interpreter.statements.text_isEmpty import text_isEmpty
from .interpreter.statements.text_convert import text_convert
from .interpreter.statements.text_indexOf import text_indexOf
from .interpreter.statements.text_charAt import text_charAt
from .interpreter.statements.text_getSubstring import text_getSubstring
from .interpreter.statements.text_changeCase import text_changeCase
from .interpreter.statements.text_trim import text_trim
from .interpreter.statements.text_print import text_print
from .interpreter.statements.text_prompt import text_prompt

# Lists
from .interpreter.statements.lists_create_with import lists_create_with
from .interpreter.statements.lists_chooser import lists_chooser
from .interpreter.statements.lists_repeat import lists_repeat
from .interpreter.statements.lists_length import lists_length
from .interpreter.statements.lists_isEmpty import lists_isEmpty
from .interpreter.statements.lists_indexOf import lists_indexOf
from .interpreter.statements.lists_getIndex import lists_getIndex
from .interpreter.statements.lists_setIndex import lists_setIndex
from .interpreter.statements.lists_getSublist import lists_getSublist
from .interpreter.statements.lists_split import lists_split
from .interpreter.statements.lists_regex import lists_regex
from .interpreter.statements.lists_sort import lists_sort

# Dict
from .interpreter.statements.dict_create_with import dict_create_with
from .interpreter.statements.dict_pair import dict_pair
from .interpreter.statements.dict_get_value import dict_get_value
from .interpreter.statements.dict_set_value import dict_set_value
from .interpreter.statements.dict_get_all_keys import dict_get_all_keys
from .interpreter.statements.dict_key_exist import dict_key_exist
from .interpreter.statements.dict_parse import dict_parse

# Variable
from .interpreter.statements.variables_set import variables_set
from .interpreter.statements.variables_get import variables_get
from .interpreter.statements.math_change import math_change

# Function
from .interpreter.statements.function_procedures_defnoreturn import function_procedures_defnoreturn
from .interpreter.statements.function_procedures_defreturn import function_procedures_defreturn
from .interpreter.statements.function_procedures_callnoreturn import function_procedures_callnoreturn
from .interpreter.statements.function_procedures_callreturn import function_procedures_callreturn
from .interpreter.statements.function_procedures_ifreturn import function_procedures_ifreturn

# HTTP
from .interpreter.statements.http_request import http_request

# Util
from .interpreter.statements.util_try_catch import util_try_catch


class TelliBot:
    def __init__(self, send_output):
        self.send_output = send_output
        asyncio.set_event_loop(asyncio.new_event_loop())  # Create a new event loop
        self.loop = asyncio.get_event_loop()
        self.LOOP_FLOW = None
        self.CATCH_BLOCK = None
        self.CATCH_VARIABLE_NAME = None
        self.VARIABLE_STACK = {}
        self.CURRENT_FUNCTION_NAME = None
        self.IS_FUNCTION_RETURN = None
        self.FUNCTION_RETURN_VALUE = None
        self.FUNCTION_STACK = []
        self.color = color
        
        self.BOT_TOKEN = None
        self.BOT_USERNAME = None
        self.BOT_ADMIN = None
        self.BOT_ADMIN_WORD = "admin"
        self.DEF_COMMANDS_STACK = []
        self.DEF_HANDLE_MESSAGE = None
        self.DEF_HANDLE_ADMIN_MESSAGE = None
        self.BOT_BUTTONS = []
        self.MESSAGE_POINTER = None
        
        self.BOT_DATABASE_NAME = None
        self.BOT_DATABASE = None
    
    async def handle_command(self, update, context):
        self.MESSAGE_POINTER = update.message
        self.BOT_BUTTONS.clear()
        text = update.message.text.strip()
        username = update.message.chat.username.lower()
        message_type = update.message.chat.type
        
        ds = [x for x in self.DEF_COMMANDS_STACK if x["commandName"] == text[1:].split(" ")[0]]
        if len(ds) > 0:
            d = ds[0]
            self.VARIABLE_STACK[d["variableMessage"]] = text
            self.VARIABLE_STACK[d["variableUsername"]] = username
            self.VARIABLE_STACK[d["variableChatId"]] = update.message.chat.id
            self.VARIABLE_STACK[d["variableType"]] = message_type
            self.execute(d["codeBlock"])
            # await update.message.reply_html(f"You've sent me {text} as <u>{username}</u>", reply_markup=ReplyKeyboardMarkup(self.BOT_BUTTONS))
        else:
            await update.message.reply_html(f"I don't understand", reply_markup=ReplyKeyboardMarkup(self.BOT_BUTTONS))
            
    async def handle_admin_message(self, update, context):
        self.MESSAGE_POINTER = update.message
        self.BOT_BUTTONS.clear()
        text = update.message.text
        username = update.message.chat.username.lower()
        message_type = update.message.chat.type
        
        if username == self.BOT_ADMIN:
            self.VARIABLE_STACK[self.DEF_HANDLE_ADMIN_MESSAGE["variableMessage"]] = text
            self.VARIABLE_STACK[self.DEF_HANDLE_ADMIN_MESSAGE["variableType"]] = message_type
            self.execute(self.DEF_HANDLE_ADMIN_MESSAGE["codeBlock"])
            # await update.message.reply_html('<span class="tg-spoiler">italic bold strikethrough spoiler</span>', reply_markup=ReplyKeyboardMarkup(self.BOT_BUTTONS))
        else:
            await update.message.reply_html(f"I don't understand", reply_markup=ReplyKeyboardMarkup(self.BOT_BUTTONS))
            
    async def handle_message(self, update, context):
        self.MESSAGE_POINTER = update.message
        self.BOT_BUTTONS.clear()
        text = update.message.text
        username = update.message.chat.username.lower()
        message_type = update.message.chat.type
        
        # for stack in self.DEF_COMMANDS_STACK:
        #     if text.startswith(stack["commandName"]):
        #         self.VARIABLE_STACK[stack["variableMessage"]] = text
        #         self.VARIABLE_STACK[stack["variableUsername"]] = username
        #         self.VARIABLE_STACK[stack["variableChatId"]] = update.message.chat.id
        #         self.VARIABLE_STACK[stack["variableType"]] = message_type
        #         self.execute(stack["codeBlock"])
        #         return
        
        # if text == "hello":
        #     self.TMP.append(update.message.chat.id)
        
        # if text == "do":
        #     for t in self.TMP:
        #         await self.bot.send_message(chat_id=t, text="global message")
        
        self.debug_print(f"User ({username}) in {message_type}: \"{text}\"")
        
        # if username == self.BOT_ADMIN and self.BOT_ADMIN_WORD is not None and text.startswith(self.BOT_ADMIN_WORD + " "):
        #     return
        
        if message_type == "group":
            if self.BOT_USERNAME in text:
                new_text = text.replace(self.BOT_USERNAME, "").strip()
                text = new_text
            else:
                return
        if self.DEF_HANDLE_MESSAGE is None:
            await update.message.reply_html("I don't understand", reply_markup=ReplyKeyboardMarkup(self.BOT_BUTTONS))
        else:
            self.VARIABLE_STACK[self.DEF_HANDLE_MESSAGE["variableMessage"]] = text
            self.VARIABLE_STACK[self.DEF_HANDLE_MESSAGE["variableUsername"]] = username
            self.VARIABLE_STACK[self.DEF_HANDLE_MESSAGE["variableChatId"]] = update.message.chat.id
            self.VARIABLE_STACK[self.DEF_HANDLE_MESSAGE["variableType"]] = message_type
            self.execute(self.DEF_HANDLE_MESSAGE["codeBlock"])
            # await update.message.reply_html(text, reply_markup=ReplyKeyboardMarkup(self.BOT_BUTTONS))
        
    def run(self, code):
        self.init_functions(code)
        self.init_bot_defs(code)
        self.execute(code)
        self.debug_print("Starting bot...")
        self.app = Application.builder().token(self.BOT_TOKEN).build()
        # self.bot = Bot(self.BOT_TOKEN)
        self.bot = self.app.bot
        self.app.add_handler(CommandHandler(list(map(lambda x: x["commandName"], self.DEF_COMMANDS_STACK)), self.handle_command))
        self.app.add_handler(MessageHandler(filters.Regex("^" + self.BOT_ADMIN_WORD), self.handle_admin_message))
        self.app.add_handler(MessageHandler(filters.TEXT, self.handle_message))
        self.loop.run_until_complete(self.app.run_polling(poll_interval=3))
    
    async def stop_bot(self):
        await self.app.stop()
        await self.app.updater.stop()
        self.app.updater._running = False
        await self.bot.close()
        await self.app.shutdown()
        self.loop.stop()

    def debug_print(self, s):
        self.send_output(s)
        print(f"{self.color.gray('[ DEBUG ]')} {s}")

    def init_bot_defs(self, code):
        statements = code
        if type(code) is str:
            statements = json.loads(statements)
            
        for i in range(len(statements)):
            statement = statements[i]
            cmd = statement.get("cmd")
            if cmd == "bot_def_command":
                bot_def_command(self, statement)
            elif cmd == "bot_handle_message":
                bot_handle_message(self, statement)
            elif cmd == "bot_handle_admin_message":
                bot_handle_admin_message(self, statement)
        return True

    def init_functions(self, code):
        statements = code
        if type(code) is str:
            statements = json.loads(statements)
        
        for i in range(len(statements)):
            statement = statements[i]
            cmd = statement.get("cmd")
            if cmd == "procedures_defnoreturn":
                function_procedures_defnoreturn(self, statement)
            elif cmd == "procedures_defreturn":
                function_procedures_defreturn(self, statement)
        return True
    
    def find_function(self, name):
        if name is None:
            return None
        for f in self.FUNCTION_STACK:
            if f["name"] == name:
                return f
        return None
    
    def show_error(self, statement, error):
        if self.CATCH_BLOCK is not None:
            catch_block = self.CATCH_BLOCK
            self.CATCH_BLOCK = None
            self.VARIABLE_STACK["error_is_here"] = f"Exception: {str(statement["cmd"]).upper()}\n{error}"
            self.execute(catch_block)
            return
        message = f"Exception: {statement["cmd"].upper()}\n\t{error}"
        self.send_output(message)
        print(self.color.red(message))
        sys.exit(1)
        
        
    def execute(self, code):
        statements = json.loads(code)
        for statement in statements:
            if self.LOOP_FLOW == "BREAK":
                break
            elif self.LOOP_FLOW == "CONTINUE":
                continue
            
            if self.IS_FUNCTION_RETURN is not None:
                break
            
            self.execute_statement(statement)
            
    def execute_statement(self, statement):
        try:
            if type(statement) is str:
                statement = json.loads(statement)
        except:
            pass
        
        if "cmd" not in statement:
            return statement
        
        cmd = statement["cmd"]
        
        # Bot
        if cmd == "bot_set_token":
            return bot_set_token(self, statement)
        elif cmd == "bot_set_username":
            return bot_set_username(self, statement)
        elif cmd == "bot_set_admin_username":
            return bot_set_admin_username(self, statement)
        elif cmd == "wait_for":
            return bot_wait_for(self, statement)
        elif cmd == "bot_admin_word":
            return bot_admin_word(self, statement)
        elif cmd == "bot_set_buttons":
            return bot_set_buttons(self, statement)
        elif cmd == "bot_send_response":
            return bot_send_response(self, statement)
        
        # Database
        elif cmd == "db_connect":
            return db_connect(self, statement)
        elif cmd == "db_create_table":
            return db_create_table(self, statement)
        elif cmd == "db_delete_table":
            return db_delete_table(self, statement)
        elif cmd == "db_insert":
            return db_insert(self, statement)
        elif cmd == "db_read":
            return db_read(self, statement)
        elif cmd == "db_delete_data":
            return db_delete_data(self, statement)
        elif cmd == "db_update":
            return db_update(self, statement)
        
        # Logic
        elif cmd == "controls_if":
            return logic_controls_if(self, statement)
        elif cmd == "logic_compare":
            return logic_compare(self, statement)
        elif cmd == "logic_operation":
            return logic_operation(self, statement)
        elif cmd == "logic_negate":
            return logic_negate(self, statement)
        elif cmd == "logic_boolean":
            return logic_boolean(self, statement)
        elif cmd == "logic_confirm":
            return logic_confirm(self, statement)
        elif cmd == "logic_null":
            return None
        elif cmd == "logic_ternary":
            return logic_ternary(self, statement)
        
        # Loops
        elif cmd == "controls_repeat_ext":
            return controls_repeat_ext(self, statement)
        elif cmd == "controls_whileUntil":
            return controls_whileUntil(self, statement)
        elif cmd == "controls_for":
            return controls_for(self, statement)
        elif cmd == "controls_forEach":
            return controls_forEach(self, statement)
        elif cmd == "controls_flow_statements":
            return controls_flow_statements(self, statement)
        
        # Math
        elif cmd == "math_number":
            return math_number(self, statement)
        elif cmd == "math_arithmetic":
            return math_arithmetic(self, statement)
        elif cmd == "math_single":
            return math_single(self, statement)
        elif cmd == "math_trig":
            return math_trig(self, statement)
        elif cmd == "math_constant":
            return math_constant(self, statement)
        elif cmd == "math_number_property":
            return math_number_property(self, statement)
        elif cmd == "convert_text_to_number":
            return math_convert_text_to_number(self, statement)
        elif cmd == "math_round":
            return math_round(self, statement)
        elif cmd == "math_on_list":
            return math_on_list(self, statement)
        elif cmd == "math_modulo":
            return math_modulo(self, statement)
        elif cmd == "math_constrain":
            return math_constrain(self, statement)
        elif cmd == "math_random_int":
            return math_random_int(self, statement)
        elif cmd == "math_random_float":
            return math_random_float(self, statement)
        
        # Text
        elif cmd == "text":
            return text(self, statement)
        elif cmd == "text_join":
            return text_join(self, statement)
        elif cmd == "text_append":
            return text_append(self, statement)
        elif cmd == "text_length":
            return text_length(self, statement)
        elif cmd == "text_isEmpty":
            return text_isEmpty(self, statement)
        elif cmd == "text_convert":
            return text_convert(self, statement)
        elif cmd == "text_indexOf":
            return text_indexOf(self, statement)
        elif cmd == "text_charAt":
            return text_charAt(self, statement)
        elif cmd == "text_getSubstring":
            return text_getSubstring(self, statement)
        elif cmd == "text_changeCase":
            return text_changeCase(self, statement)
        elif cmd == "text_trim":
            return text_trim(self, statement)
        elif cmd == "text_print":
            return text_print(self, statement)
        elif cmd == "prompt":
            return text_prompt(self, statement)
        
        # Lists
        elif cmd == "lists_create_with":
            return lists_create_with(self, statement)
        elif cmd == "lists_chooser":
            return lists_chooser(self, statement)
        elif cmd == "lists_repeat":
            return lists_repeat(self, statement)
        elif cmd == "lists_length":
            return lists_length(self, statement)
        elif cmd == "lists_isEmpty":
            return lists_isEmpty(self, statement)
        elif cmd == "lists_indexOf":
            return lists_indexOf(self, statement)
        elif cmd == "lists_getIndex":
            return lists_getIndex(self, statement)
        elif cmd == "lists_setIndex":
            return lists_setIndex(self, statement)
        elif cmd == "lists_getSublist":
            return lists_getSublist(self, statement)
        elif cmd == "lists_split":
            return lists_split(self, statement)
        elif cmd == "lists_regex":
            return lists_regex(self, statement)
        elif cmd == "lists_sort":
            return lists_sort(self, statement)
        
        # Dict
        elif cmd == "dict_create_with":
            return dict_create_with(self, statement)
        elif cmd == "dict_pair":
            return dict_pair(self, statement)
        elif cmd == "dict_get_value":
            return dict_get_value(self, statement)
        elif cmd == "dict_set_value":
            return dict_set_value(self, statement)
        elif cmd == "dict_get_all_keys":
            return dict_get_all_keys(self, statement)
        elif cmd == "dict_key_exist":
            return dict_key_exist(self, statement)
        elif cmd == "dict_parse":
            return dict_parse(self, statement)
        
        # Variables
        elif cmd == "variables_set":
            return variables_set(self, statement)
        elif cmd == "variables_get":
            return variables_get(self, statement)
        elif cmd == "math_change":
            return math_change(self, statement)
        
        # Function
        elif cmd == "procedures_callnoreturn":
            return function_procedures_callnoreturn(self, statement)
        elif cmd == "procedures_callreturn":
            return function_procedures_callreturn(self, statement)
        elif cmd == "procedures_ifreturn":
            return function_procedures_ifreturn(self, statement)
        
        # HTTP
        elif cmd == "http_request":
            return http_request(self, statement)
        
        # Utility
        elif cmd == "util_try_catch":
            return util_try_catch(self, statement)
        
        else:
            return None


if __name__ == "__main__":
    src_file = sys.argv[1]
    with open(src_file, "r") as f:
        data = f.read()
    telli = TelliBot(lambda s: print(s))
    code = json.loads(base64.b64decode(json.loads(base64.b64decode(data))["code"]))
    telli.run(json.dumps(code))

