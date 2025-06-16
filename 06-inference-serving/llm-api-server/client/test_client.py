import requests

API_URL = "http://localhost:8000/generate/"

data = {"prompt": "Once upon a time, there was a small village"}

response = requests.post(API_URL, json=data)

print(response.json())

