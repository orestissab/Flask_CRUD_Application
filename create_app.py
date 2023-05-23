from flask import Flask
from database import db

def create_app(test_config=None):
    app = Flask(__name__)
    
    if test_config is None:
        app.config.from_object('config.Config')
    else:
        app.config.from_mapping(test_config)
    
    db.init_app(app)
    return app


