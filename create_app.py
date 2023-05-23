"""
This module provides a function to create a Flask application with optional configuration.
"""
from flask import Flask
from database import db

def create_app(test_config=None):
    """
    Create a Flask application with the given configuration. If no configuration is provided,
    the application uses the configuration from the config module.
    """
    app = Flask(__name__)
    
    if test_config is None:
        app.config.from_object('config.Config')
    else:
        app.config.from_mapping(test_config)
    
    db.init_app(app)
    return app


