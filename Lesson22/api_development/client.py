import requests

api_url = "https://127.0.0.1:8000/create_person"

person_date = {"name": "John Doe", "age": 30}

response = requests.post(api_url, json=person_date)

print("Response Code:", response.status_code)
print("Response JSON:", response.json())