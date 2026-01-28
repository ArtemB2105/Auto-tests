import pytest
import requests

@pytest.fixture(scope="session")
def create_test_object():
    test_object = {
        "name": "Test Object",
        "data": {
            "year": 2021,
            "price": 999.99,
            "CPU model": "Test CPU",
            "Hard disk size": "512 GB"
        }
    }

    responce = requests.post("https://api.restful-api.dev/objects",json = test_object).json()
    yield responce['id']
    
    requests.delete(f"https://api.restful-api.dev/objects/{responce['id']}")