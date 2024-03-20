from app import app
from models import db, Site, Instrument


with app.app_context():
    site = Site.query.filter_by(location_id=1).first()

    instruments = [
        Instrument(type='Radiometer', model='Cimel Radiometer', site=site),
        Instrument(type='Lidar', model='CCNY Elastic Raman Lidar', site=site),
        Instrument(type='Lidar', model='Leosphere 200s', site=site),
        Instrument(type='Ceilometer', model='Lufft CHM15k', site=site),
        Instrument(type='Radiometer', model='Radiometrics 300A', site=site),
        Instrument(type='Lidar', model='CCNY Lab O3-DIAL', site=site),
        Instrument(type='Radiosonde', model='', site=site)
    ]

    db.session.add_all(instruments)
    db.session.commit()

