# Initializes the Flask app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    
    # Redirects to 'login' view if unauthenticated user tries to access protected routes
    login.login_view = 'login'

    @app.route('/')
    def hello():
        return "Hello, World!"

    return app

    return app
