from peewee import *

DATABASE = MySQLDatabase("tellibot", host="localhost", port=3306, user="root", passwd="")


class Script(Model):
    id = PrimaryKeyField()
    title = CharField()
    uid = CharField()
    
    class Meta:
        database = DATABASE
        
        
def initialize_db():
    DATABASE.connect(reuse_if_open=True)
    DATABASE.create_tables([Script], safe=True)


def close_db():
    DATABASE.close()
