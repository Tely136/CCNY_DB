from tkinter import Image
from flask import Flask, render_template, send_from_directory, request, redirect
from flask_migrate import Migrate
from models import db, Site
import os
from datetime import datetime, timedelta


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

# db.init_app(app)
#
# with app.app_context():
#     db.create_all()

migrate = Migrate(app, db)

db.init_app(app)
migrate.init_app(app, db)

db_path = 'db'
db_dict = {}

dirs = os.listdir(os.path.join(os.getcwd(), db_path))

for dir in dirs:
    db_dict[dir] = os.listdir(os.path.join(db_path, dir))


sites = [
    ('CityCollege-SteinmanHall', 40.82164787191762, -73.94805812164206),
    ('CityCollege-ASRC', 40.81567968015576, -73.95018624908833),
    ('YaleCoastalSite', 41.258113767203504, -72.73281085162301),
    ('ColumbiaUniversity-LDEO', 41.003432414889495, -73.90709234803525),
    ('HamptonUniversity-Turner Hall', 38.986143412699015, -76.93730810053025),
    ('HowardUniversity-Beltsville Campus', 39.05630677454083, -76.87558009401812),
    ('HowardUniversity-Interdisciplinary Research Building', 38.9192487350571, -77.02152738509146)
]


@app.route('/')
def index():
    return render_template('test.html', sites=sites, db=db_dict)


# Define a route to serve images from an external directory
@app.route('/images/<filepath>/<filename>')
def serve_image(filepath, filename):
    return send_from_directory(filepath, filename)


@app.route('/submit/', methods=['POST'])
def submit():
    selected_date = request.form.get('selectedDate')
    data_type = request.form.get('inputValue')  # Use the input name attribute

    if selected_date == '':
        selected_date = (datetime.today() - timedelta(days=1)).strftime("%m/%d/%Y")

        print(selected_date)

    data_location = data_type.split('_')
    site = data_location[0]
    instrument = data_location[1]

    date = datetime.strptime(selected_date, "%m/%d/%Y").date()
    year = date.year

    datestr = date.strftime("%Y%m%d")
    print(date)
    print(datestr)

    try:
        path = os.path.join(db_path, site, instrument, str(year))
        folders = os.listdir(path)

    except FileNotFoundError:
        return 'No Data Available'

    if not folders:
        return 'No Data Available'

    folder_dates = []
    for folder in folders:
        folder_dates.append((folder.split('_')[0], folder))

    f = None
    for folder in folder_dates:
        if datestr == folder[0]:
            f = folder[1]

    if f is None:
        return 'No Data Available'

    file_name = None
    for file in os.listdir(os.path.join(db_path, site, instrument, str(year), f)):
        if file.endswith('.jpg'):
            file_name = file

    if file_name:
        img_path = os.path.join(os.getcwd(), db_path, site, instrument, str(year), f)
        print(img_path)

        return render_template('data_view.html', img_path=img_path, img_name=file_name, site=site,
                               instrument=instrument)

    else:
        return 'No Data Available'


if __name__ == '__main__':
    app.run(debug=True)
