from app import db, models
import csv

with open('printers.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        u = models.Printer(name=row[0], building=row[1], room=row[2], model=row[3])
        db.session.add(u)

db.session.commit()
