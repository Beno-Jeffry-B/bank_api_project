from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Bank(db.Model):
    __tablename__ = 'banks'

    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(49), nullable=False)


class Branch(db.Model):
    __tablename__ = 'branches'

    ifsc = db.Column(db.String(11), primary_key=True)
    bank_id = db.Column(db.BigInteger, db.ForeignKey('banks.id'))
    branch = db.Column(db.String(74))
    address = db.Column(db.String(195))
    city = db.Column(db.String(50))
    district = db.Column(db.String(50))
    state = db.Column(db.String(26))

#relationship
    bank = db.relationship("Bank", backref="branches")
