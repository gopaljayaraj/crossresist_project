from flask import Flask
from flask_admin.contrib import peewee
from flask_admin import Admin
from peewee import SqliteDatabase
from models import User

app=Flask (__name__)
app.config.update(
    WTF_CSRF_ENABLED=True,
    SECRET_KEY='x\xb7\xfb\x9b\x17:\xd1\xd72\xea\x17-\x13\xd4/\x93\x08>\xa1\xd3\x96\x15\xe7\xd1',
)

database = SqliteDatabase('database.sqlite', threadlocals=True)
admin = Admin(app, name='CrossResist', template_mode='bootstrap3')
class Admin(peewee.ModelView):
    column_display_pk = True
admin.add_view(Admin(User))

import views



