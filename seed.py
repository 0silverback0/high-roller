from app import app
from models import db, Bud

with app.app_context():
    db.drop_all()
    db.create_all()    

    b1 = Bud(
        brand='Collins Ave',
        strain='Cookies',
        category='Indica',
        thc = 21.04,
        img = 'safetypackIndica.jpeg',
        price= 50,
        qty = '1/8'
    )

    b2 = Bud(
        brand='Gage',
        strain='Grap Gmmiez',
        category='Hybrid',
        thc = 23.33,
        img = 'safetypackIndica.jpeg',
        price= 50,
        qty = '1/8'
        
    )

    b3 = Bud(
        brand='Good Green',
        strain='GTI - Love Affair',
        category='Sativa',
        thc = 22.18,
        price= 85,
        img = 'safetypackIndica.jpeg',
        qty = '1/4',
    )

    b4 = Bud(
        brand='Marzy Baby',
        strain='Emerald Cut',
        category='Sativa',
        thc = 30,
        price= 100,
        img = 'emeraldcuthybrid.jpeg',
        qty = '1/4',
    )

    b5 = Bud(
        brand='Collins Ave',
        strain='Afghan',
        category='Indica',
        thc = 21.04,
        img = 'safetypackIndica.jpeg',
        price= 40,
        qty = '1/8'
    )

    db.session.add_all([b1, b2, b3, b4, b5])
    db.session.commit()