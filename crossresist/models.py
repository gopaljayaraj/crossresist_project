from peewee import SqliteDatabase, Model, CharField, IntegerField

db = SqliteDatabase('database.sqlite')

class BaseModel(Model):
	class Meta:
		database = db

class User(BaseModel):
	uid = IntegerField()
	username = CharField()
	password = CharField()
	
