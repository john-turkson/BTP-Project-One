from flask import Flask
from flask_cors import CORS
from .models import db
from .routes import app_routes

def create_app():
    
    app = Flask(__name__)
    CORS(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost/music-app-db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Register routes
    app.register_blueprint(app_routes)

    # Intialize the Database
    db.init_app(app)

    with app.app_context():
        db.create_all()
    return app
