from models import Contacts
from app import db


#create the database
#db.create_all()
#insert
db.session.add(Contacts("Blessing j", "lagos", "08062201523", "F", "Friend"))
db.session.add(Contacts("Mary M", "1, Ojuelegba rd",  "08055234567", "F", "Friend"))
db.session.add(Contacts("Mary M", "1, Ojuelegba rd",  "08055237567", "M", "Family"))
db.session.add(Contacts("Mary M", "1, Ojuelegba rd",  "08055034567", "M", "Work"))
#commit change
db.session.commit()