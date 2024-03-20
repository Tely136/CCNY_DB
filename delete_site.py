from models import db, Site
from app import app

# Assuming you know the location_id of the site you want to remove
site_to_remove_id = 1  # Example ID

with app.app_context():
    site_to_remove = Site.query.get(site_to_remove_id)

    if site_to_remove:
        db.session.delete(site_to_remove)
        db.session.commit()
