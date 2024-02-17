from flask import Flask
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_restful import Api, Resource, reqparse

from models import db
from schemas import ma
from resources.employees import Employee_list, Employee_by_id


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hr.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate =  Migrate(app, db)


db.init_app(app)
ma.init_app(app)
api=Api(app)


@app.route('/')
def index():
    return "code check one two"


api.add_resource(Employee_list, '/employees')
api.add_resource(Employee_by_id, '/employees/<int:id>')


if __name__ == '__main__':
    app.run(port=5555,debug=True)