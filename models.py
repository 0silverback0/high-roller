from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """ connect to database """
    db.app = app
    db.init_app(app)


class Bud(db.Model):
    """Bud Model"""
    __tablename__ = 'bud'

    id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    brand = db.Column(db.Text, nullable=False)
    strain = db.Column(db.Text, nullable=False)
    category = db.Column(db.Text, nullable=False)
    thc = db.Column(db.Float, nullable=False)
    img = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    qty = db.Column(db.String, nullable=False)
   

