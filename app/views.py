from flask import render_template
from app import app, db
from models import Printer

@app.route('/')
@app.route('/index')
def index():
    printers = Printer.query.all()
    schools = ['MHS', 'AIT', 'APA', 'AAHS', 'UCTECH']
    return render_template('school.html', schools = schools)

@app.route('/<school>')
def school(school):
    rooms = Printer.query.filter(Printer.building == school)
    return render_template('room.html', rooms = rooms)
