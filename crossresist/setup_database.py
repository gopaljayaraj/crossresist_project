from peewee import SqliteDatabase
from models import User

database = SqliteDatabase('database.sqlite', threadlocals=True)

def create_tables():
	database.connect()
	database.create_tables([User])

if __name__ == '__main__':
	import os
	os.system('rm database.sqlite')
	create_tables()