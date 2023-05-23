from flask import Blueprint, request, jsonify, render_template
from sqlalchemy import Column, Integer, String
from database import db

class Bank(db.Model):
    __tablename__ = 'banks'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    location = Column(String)

    def __init__(self, name, location):
        self.name = name
        self.location = location

bank_blueprint = Blueprint('bank_blueprint', __name__)

@bank_blueprint.route('/add_bank', methods=['GET'])
def add_bank_form():
    return render_template('add_bank.html')


@bank_blueprint.route('/add_bank', methods=['POST'])
def create_bank():
    name = request.form.get('name')
    location = request.form.get('location')
    new_bank = Bank(name=name, location=location)
    db.session.add(new_bank)
    db.session.commit()
    return jsonify({'message': 'Bank created'}), 201


@bank_blueprint.route('/all_banks', methods=['GET'])
def get_banks():
    banks = Bank.query.all()
    return jsonify([{'id': bank.id, 'name': bank.name, 'location': bank.location} for bank in banks])


@bank_blueprint.route('/banks/<int:id>', methods=['GET'])
def get_bank(id):
    bank = db.session.get(Bank, id)
    if bank is None:
        return jsonify({'message': 'Bank not found'}), 404
    return jsonify({'id': bank.id, 'name': bank.name, 'location': bank.location})


@bank_blueprint.route('/banks/<int:id>', methods=['PUT'])
def update_bank(id):
    data = request.get_json()
    bank = db.session.get(Bank, id)
    if bank is None:
        return jsonify({'message': 'Bank not found'}), 404
    bank.name = data['name']
    bank.location = data['location']
    db.session.commit()
    return jsonify({'message': 'Bank updated'})


@bank_blueprint.route('/banks/<int:id>', methods=['DELETE'])
def delete_bank(id):
    bank = db.session.get(Bank, id)
    if bank is None:
        return jsonify({'message': 'Bank not found'}), 404
    db.session.delete(bank)
    db.session.commit()
    return jsonify({'message': 'Bank deleted'})
