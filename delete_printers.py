#!bin/python
from app import db, models
printers = models.Printer.query.all()

for printer in printers:
    db.session.delete(printer)

db.session.commit()
