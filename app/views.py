from flask import render_template
from app import app, db
from models import Printer
import pdb

# 'index' gives you the 5 schools and links to the printers in each
@app.route('/')
@app.route('/index')
def index():
    printers = Printer.query.all()
    schools = ['mhs', 'ait', 'apa', 'allied', 'uctech']
    return render_template('school.html', schools = schools)

# 'school' gives you the rooms found in the schools
@app.route('/<school>/')
def school(school):
    printers = Printer.query.filter(Printer.building == school)
    return render_template('room.html', printers = printers)

@app.route('/<school>/<int:room>')
def room(room):
    printers2 = printers.query.filter(Printer.room == room)
    return render_template('printers.html', printers = printers) 
