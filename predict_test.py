import requests
import json

url = "http://localhost:9696/predict"
client_id = 'Delilah Rivers'
client = {"job": "student", "duration": 280, "poutcome": "failure"}
response = requests.post(url, json=client).json()

print(response)

if response['subscription'] == True:
    print(f'This client {client_id} will get a subscription.')
else:
    print(f'This client {client_id} will not get a subscription.')