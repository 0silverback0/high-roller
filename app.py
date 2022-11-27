from flask import Flask, render_template, redirect, request
from models import connect_db, db, Bud
from forms import Budorm, Search
from filter import Filter
import os , string, pdb
from werkzeug.utils import secure_filename

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Deja1218@localhost/bud'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = True
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'key')

    with app.app_context():
        connect_db(app)
        db.create_all()
    return app

app = create_app()

@app.route('/admin', methods=['GET', 'POST'])
def home():
    form = Budorm()

    if form.validate_on_submit():
        brand = form.brand.data
        strain = form.strain.data
        category = form.category.data
        thc = form.thc.data
        img = form.img.data
        qty = form.qty.data
        price = form.price.data

        newBud = Bud(brand=brand, strain=strain, category=category, thc=thc,
        img=img, qty=qty, price=price)

        with app.app_context():
            
            db.session.add(newBud)
            db.session.commit()
       
        return redirect('/')

    return render_template('admin.html', form=form)

@app.route('/')
def bud():
    form = Search()
    bud = Bud.query.all()
    return render_template('index.html', bud=bud, form=form)

@app.route('/filter')
def filter():
    form = Search()
    thc = False if request.args.get('thc') == '' else request.args.get('thc')
    brand = None or string.capwords(request.args.get('brand'))
    category = None or request.args.get('category')

    filter = Filter(Bud,thc,brand,category)
    bud = filter.query_filter()
    
    return render_template('index.html', form=form, bud=bud)

