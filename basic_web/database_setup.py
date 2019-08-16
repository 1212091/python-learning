from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from sqlalchemy import ForeignKey

app = Flask(__name__)

# config database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://dotran:Leonardo112019!@localhost/company'

# config migrate
db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# model
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    business_unit_id = db.Column(db.Integer, ForeignKey('business_unit.id'))
    name = db.Column(db.String(128))
    description = db.Column(db.String(128))


class Business_unit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bu_name = db.Column(db.String(128))
    location = db.Column(db.String(255))


if __name__ == '__main__':
    manager.run()
