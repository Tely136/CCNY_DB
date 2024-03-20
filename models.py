from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Site(db.Model):
    __tablename__ = 'sites'

    location_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    address = db.Column(db.String(256), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    instruments = db.relationship('Instrument', backref='site', lazy=True)


class Instrument(db.Model):
    __tablename__ = 'intruments'

    instrument_id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(128), nullable=False)
    model = db.Column(db.String(128), nullable=False)
    site_id = db.Column(db.Integer, db.ForeignKey('sites.location_id'), nullable=False)

    def __repr__(self):
        return f'<Site {self.name}'

