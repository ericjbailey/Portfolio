import sys
import os
import requests

# Add the project directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# TODO: send a GET using the URL
base_url = "http://127.0.0.1:8000"

# Send GET request
response_get = requests.get(base_url)
print(f"GET Status Code: {response_get.status_code}")
print(f"GET Response: {response_get.json()}")

# TODO: send a POST using the URL
data = {
    "age": 37,
    "workclass": "Private",
    "fnlgt": 178356,
    "education": "HS-grad",
    "education-num": 10,
    "marital-status": "Married-civ-spouse",
    "occupation": "Prof-specialty",
    "relationship": "Husband",
    "race": "White",
    "sex": "Male",
    "capital-gain": 0,
    "capital-loss": 0,
    "hours-per-week": 40,
    "native-country": "United-States",
}

# Send POST request
response_post = requests.post(f"{base_url}/predict/", json=data)
print(f"POST Status Code: {response_post.status_code}")
print(f"POST Response: {response_post.json()}")
