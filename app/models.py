from app import db

class Printer(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    building = db.Column(db.String(10), index = True)
    room = db.Column(db.Integer, index = True)
    model = db.Column(db.String(10), index = True)
    name = db.Column(db.String(15), index = True, unique = True)

    def __repr__(self):
        return '<Printer %r>' % (self.name)
