import json
import requests

expected = {"name": "Running", "description": "30 minutes", "done": "False"}

data = {"name": "Running", "description": "30 minutes", "done": "False"}

headers = {"Content-type": "application/json"}

response = requests.post("http://127.0.0.1:8000/notes", data=json.dumps(data), headers=headers)

assert expected == response.json()
