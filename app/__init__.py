from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# Initialize the database
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configuration settings (you can modify these as needed)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cryptotracker.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize the extensions
    db.init_app(app)
    CORS(app)  # Enable CORS for cross-origin requests

    # Register the blueprint for routes
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
