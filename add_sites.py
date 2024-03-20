from app import app
from models import db, Site


sites = [
    Site(name='City College Steinman Hall', address='275 Convent Ave, New York, NY 10031', latitude=40.82164787191762, longitude=-73.94805812164206),
    Site(name='CUNY ASRC', address='85 St Nicholas Terrace, New York, NY 10031', latitude=40.81567968015576, longitude=-73.95018624908833),
    Site(name='Yale Coastal Site', address='276 Old Quarry Rd', latitude=41.258113767203504, longitude=-72.73281085162301),
    Site(name='Columbia University LDEO', address='61 Rte 9W, Palisades, NY 10964', latitude=41.003432414889495, longitude=-73.90709234803525),
    Site(name='Hampton University Turner Hall', address='200 William R. Harvey Way, Hampton, VA 23669', latitude=38.986143412699015, longitude=-76.93730810053025),
    Site(name='Howard University Beltsville Campus', address='7501 Muirkirk Rd Unit C, Beltsville, MD 20705', latitude=39.05630677454083, longitude=-76.87558009401812),
    Site(name='Howard University Interdisciplinary Research Building', address='2201 Georgia Ave NW, Washington, DC 20059', latitude=38.9192487350571, longitude=-77.02152738509146)
]

with app.app_context():
    db.session.add_all(sites)
    db.session.commit()
    