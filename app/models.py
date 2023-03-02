from datetime import datetime
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), unique=True, nullable=True)
    last_name = db.Column(db.String(64), unique=True, nullable=True)
    username = db.Column(db.String(64), unique=True, nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=True)
    password_hash = db.Column(db.String(120), nullable=True)

    def __repr__(self):
            return f"<User: {self.username}>"

    def __str__(self):
        return f'User: {self.email}|{self.username}'

    def hash_password(self, password):
            self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def commit(self):
            db.session.add(self)
            db.session.commit()

class GameLibrary(db.Model):
      id = id= db.Column(db.Integer, primary_key=True)
      game_title = db.Column(db.String(140))
      genre = db.Column(db.String(40))
      rating = db.Column(db.String(20))

      def commit(self):
            db.session.add(self)
            db.session.commit()