from flask import render_template, g
from app import app, db
from models import Printer
import pdb

# 'index' returns the 5 schools and links to the printers in each
@app.route('/')
@app.route('/index')
def index():
    printers = Printer.query.all()
    schools = ['mhs', 'ait', 'apa', 'allied', 'uctech']
    return render_template('school.html', schools = schools)

# 'school' returns the rooms found in the schools
@app.route('/<school>/')
def school(school):
    printers = Printer.query.filter(Printer.building == school)
    return render_template('room.html', printers = printers)

# 'room' returns the printers found in the specified room
@app.route('/room/<int:room>')
def room(room):
    printers = Printer.query.filter(Printer.room == room)
    return render_template('printers.html', printers = printers)

# 'printer will return the instructions for a single printer'
@app.route('/instructions/<int:id>')
def printer(id):
    printer = Printer.query.get(id)
    return render_template('instructions.html', printer=printer)
