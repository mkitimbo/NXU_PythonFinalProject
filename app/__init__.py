import os
from flask import Flask
from flask_pymongo import PyMongo
from pymongo.mongo_client import MongoClient

mongo = PyMongo()

def create_app():
    app = Flask(__name__)

    # Load MONGO_URI from environment variable
    app.config["MONGO_URI"] = os.getenv("MONGO_URI")

    # Initialize Mongo with Flask app
    mongo.init_app(app)

    # Optional: Test the MongoDB connection
    try:
        uri = app.config["MONGO_URI"]
        client = MongoClient(uri)
        client.admin.command('ping')
        print("✅ Successfully connected to MongoDB!")
    except Exception as e:
        print("❌ MongoDB connection failed:", e)

    # Import and register blueprint
    from app.routes import main
    app.register_blueprint(main)

    return app
