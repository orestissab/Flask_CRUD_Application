import requests
import json

# URL for your Flask application
url = "http://localhost:5000"

# Create a new bank
def create_bank(name, location):
    payload = {'name': name, 'location': location}
    response = requests.post(f'{url}/add_bank', data=payload)
    print(response.json())

# Get all banks
def get_banks():
    response = requests.get(f'{url}/all_banks')
    print(response.json())

# Get a specific bank
def get_bank(id):
    response = requests.get(f'{url}/banks/{id}')
    print(response.json())

# Update a bank
def update_bank(id, name, location):
    payload = {'name': name, 'location': location}
    headers = {'Content-Type': 'application/json'}
    response = requests.put(f'{url}/banks/{id}', data=json.dumps(payload), headers=headers)
    print(response.json())

# Delete a bank
def delete_bank(id):
    response = requests.delete(f'{url}/banks/{id}')
    print(response.json())

# Test the functions
create_bank('Interact Bank', 'Interact Location')
get_banks()
get_bank(1)
update_bank(1, 'Updated Test Bank', 'Updated Test Location')
delete_bank(1)
