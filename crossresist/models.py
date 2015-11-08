from crossresist import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True, unique=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(64), index=True)
    email = db.Column(db.String(120), index=True)

    def __init__(self, id, username, password, email):
        self.id = id
        self.username = username
        self.password = password
        self.email = email

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)  # python 3

    def __repr__(self):
        return '<User %r>' % self.username