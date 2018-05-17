from app import db

class Stadium(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    city = db.Column(db.String(80), nullable=False)
    country = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return "<Stadium: {}>".format(self.name)
