import os
from flask import Flask
from flask_pymongo import PyMongo
from dotenv import load_dotenv

# Load environment variables from .env if available
load_dotenv()

mongo = PyMongo()

def create_app():
    app = Flask(__name__)

    mongo_uri = os.getenv("MONGO_URI")
    if not mongo_uri:
        raise ValueError("❌ MONGO_URI is not set. Please check your environment variables.")

    # Apply config and init Mongo
    app.config["MONGO_URI"] = mongo_uri
    mongo.init_app(app)

    # Register blueprints
    from app.routes import main
    app.register_blueprint(main)

    return app
