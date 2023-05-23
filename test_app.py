import os
import pytest
from flask import Flask
from dotenv import load_dotenv
from create_app import create_app, db
from bank_blueprint import Bank, bank_blueprint

load_dotenv()

app = create_app({
    "SQLALCHEMY_DATABASE_URI": os.getenv('TEST_DB_URI'), 
    "TESTING": True,
    "SQLALCHEMY_TRACK_MODIFICATIONS": True
})
app.register_blueprint(bank_blueprint)


@pytest.fixture
def client():
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

@pytest.fixture(autouse=True)
def run_around_tests():
    with app.app_context():
        db.create_all()
    
    yield
    
    with app.app_context():
        db.drop_all()


def test_create_bank(client):
    with app.app_context():
        response = client.post('/add_bank', data=dict(name='Test Bank', location='Test Location'))
        assert response.status_code == 201
        assert b'Bank created' in response.data

def test_get_banks(client):
    with app.app_context():
        bank = Bank(name='Test Bank', location='Test Location')
        db.session.add(bank)
        db.session.commit()
        
        response = client.get('/all_banks')
        assert response.status_code == 200
        assert b'Test Bank' in response.data

def test_get_bank(client):
    with app.app_context():
        bank = Bank(name='Get Bank', location='Test Location')
        db.session.add(bank)
        db.session.commit()

        response = client.get(f'/banks/{bank.id}')
        assert response.status_code == 200
        assert b'Get Bank' in response.data

def test_update_bank(client):
    with app.app_context():
        bank = Bank(name='Update Bank', location='Update Location')
        db.session.add(bank)
        db.session.commit()

        response = client.put(f'/banks/{bank.id}', json={'name': 'Updated Bank', 'location': 'Updated Location'})
        assert response.status_code == 200
        assert b'Bank updated' in response.data

        updated_bank = db.session.get(Bank, bank.id)
        assert updated_bank.name == 'Updated Bank'
        assert updated_bank.location == 'Updated Location'

def test_delete_bank(client):
    with app.app_context():
        bank = Bank(name='Delete Bank', location='Delete Location')
        db.session.add(bank)
        db.session.commit()

        response = client.delete(f'/banks/{bank.id}')
        assert response.status_code == 200
        assert b'Bank deleted' in response.data

        deleted_bank = db.session.get(Bank, bank.id)
        assert deleted_bank is None
