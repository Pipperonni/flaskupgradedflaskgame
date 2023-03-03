from app import db

class GameLibrary(db.Model):
      id = id= db.Column(db.Integer, primary_key=True)
      game_title = db.Column(db.String(140))
      genre = db.Column(db.String(40))
      rating = db.Column(db.String(20))
      

      def commit(self):
            db.session.add(self)
            db.session.commit()