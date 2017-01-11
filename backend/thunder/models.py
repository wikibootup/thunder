from thunder import db
from sqlalchemy.dialects.postgresql import JSON


class Result(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return '<id {}>'.format(self.id)
