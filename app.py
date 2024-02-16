from flask import Flask
from flask_marshmallow import Marshmallow
from models import db
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hr.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate =  Migrate(app, db)


db.init_app(app)
ma= Marshmallow(app)



@app.route('/')
def index():
    return "code check one two"


if __name__ == '__main__':
    app.run(port=5555,debug=True)