from flask import Flask
from flask_admin import Admin
from flask.ext.sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config.update(
    WTF_CSRF_ENABLED=True,
    SECRET_KEY='x\xb7\xfb\x9b\x17:\xd1\xd72\xea\x17-\x13\xd4/\x93\x08>\xa1\xd3\x96\x15\xe7\xd1',
    SQLALCHEMY_DATABASE_URI='sqlite:///database.sqlite'
)
db = SQLAlchemy(app)
# admin = Admin(app, name='CrossResist', template_mode='bootstrap3')
# class Admin(peewee.ModelView):
#     column_display_pk = True
# admin.add_view(Admin(User))

login_manager = LoginManager()
login_manager.init_app(app)

import views



