from flask import Flask, Blueprint
from .views import bp as main_bp  # Import the blueprint from views

def create_app():
    app = Flask(__name__)

    # Register the main Blueprint
    app.register_blueprint(main_bp)

    return app
