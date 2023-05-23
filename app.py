import os
from dotenv import load_dotenv
from create_app import create_app, db
from bank_blueprint import bank_blueprint

load_dotenv()

def run_app():
    app = create_app({
        "SQLALCHEMY_DATABASE_URI": os.getenv('MAIN_DB_URI'),
        "SQLALCHEMY_TRACK_MODIFICATIONS": True,
    })
    app.register_blueprint(bank_blueprint)

    with app.app_context():
        db.create_all()

    app.run(debug=True)

if __name__ == '__main__':
    run_app()
