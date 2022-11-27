from unicodedata import category
from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import FloatField, RadioField, StringField, FileField, IntegerField, SelectField
# from werkzeug.utils import FileField
from wtforms.validators import DataRequired

class Search(FlaskForm):
    thc = IntegerField('THC')
    brand = StringField('Brand')
    category = SelectField('Type', choices=[('','Select'),('Sativa','Sativa'), ('Indica', 'Indica'), ('Hybrid', 'Hybrid')])
    
class Budorm(FlaskForm):
    brand = StringField('Brand', validators=[DataRequired()])
    strain = StringField('Strain', validators=[DataRequired()])
    category = RadioField('Category', choices=[ ('Hybrid', 'Hybrid'), ('Sativa', 'Sativa'),
    ('Indica', 'Indica')], validators=[DataRequired()])
    thc = FloatField('THC', validators=[DataRequired()])
    img = FileField('Image', validators=[DataRequired()])
    qty = StringField('QTY', validators=[DataRequired()])
    price = IntegerField('Price', validators=[DataRequired()])

