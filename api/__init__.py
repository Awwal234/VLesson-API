from flask import Flask
from flask_restx import Api
from .utils import db
import os
from dotenv import load_dotenv
from .info.information import info_namespace
load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'sk'
    app.config['SQLALCHEMY_TRACK_MODIFICAIONS'] = False
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stored.db'
    # db.init_app(app)
    # with app.app_context():
    #     db.create_all()
    
    api = Api(app, title="V LESSON", version='0.1')
    api.add_namespace(info_namespace, path='/api/getinfo')
    
    return app

#flask function
# def sit():
#     print('Okay im sitting')

# sit()