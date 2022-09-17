from dataclasses import dataclass
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db=SQLAlchemy() 
DB_NAME="databse.db"




def create_app():
    app = Flask(__name__,template_folder='template')
    app.config['SECRET_KEY'] = 'thisisasecretkey'
    app.config['SQLALCHEMY_DATABSE_URI']=f'sqlite:///website/{DB_NAME}'     
    db.init_app(app)        

    from .views import views
    from .auth import auth

    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')    

    from .models import User
    
    create_database(app)
    
    
    return app

    
    
def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')