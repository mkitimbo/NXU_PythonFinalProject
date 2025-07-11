import os
from flask import Flask
from flask_pymongo import PyMongo
from dotenv import load_dotenv

mongo = PyMongo()

def create_app():
    app = Flask(__name__)
    
    # MongoDB Atlas connection string
    app.config["MONGO_URI"] = "mongodb+srv://mkitimbo:txaHdneje2CZmkOt@kmt.tslnr0v.mongodb.net/income_db?retryWrites=true&w=majority&tls=true"
    
    mongo.init_app(app)

   # Import blueprints here to avoid circular imports
    from app.routes import main
    app.register_blueprint(main)
    
    return app
