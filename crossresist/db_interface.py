import os
import sys

base_path = os.path.dirname(os.getcwd())
sys.path.append(base_path)

from crossresist import db
from crossresist.models import User


def scratch_db():
	os.system('rm database.sqlite')
	db.create_all()
	admin = User(1, username='gopaladmin', password='kr', email='gopal@crossresist.org')
	db.session.add(admin)
	db.session.commit()

def show_users():
	print "--------------------"
	for i in  User.query.order_by(User.username):
		print i.username
	print "--------------------"
	return True

def show_password():
	username = raw_input('Enter username: ').rstrip('\n')
	query = User.query.filter_by(username=username).first()
	print "--------------------"
	print query.password
	print "--------------------"
	return True

def get_num_entries():
	print db.session.query(User).count()

def remove_user():
	username = raw_input('Enter username: ').rstrip('\n')
	query = User.query.filter_by(username=username).first()
	db.session.delete(query)
	db.session.commit()
	print "--------------------"
	print username, " removed"
	print "--------------------"

if __name__ == '__main__':
	commands = {
		'show_users': show_users,
		'show_password': show_password,
		'scratch_db': scratch_db,
		'get_num_entries': get_num_entries,
		'remove_user': remove_user
	}
	if len(sys.argv) == 1:
		print "Following options are available: "
		for i in commands:
			print "\t", i
	else:
		arg = sys.argv[1]
		commands[arg]()