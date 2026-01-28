import requests
import pytest

def test_add_object(): #создание объекта
    object_id = {
        "name": "MacBook Pro 16",
        "data": {
            "year": 2021,
            "price": 999.99,
            "CPU model": "Test CPU",
            "Hard disk size": "512 GB",
        },
    }
    responce = requests.post("https://api.restful-api.dev/objects", json=object_id)
    assert responce.status_code == 200
    responce = requests.post("https://api.restful-api.dev/objects", json=object_id).json()
    assert responce["name"] == "MacBook Pro 16"



def test_get_object(create_test_object): #получение объекта
    object_id = create_test_object
    responce = requests.get(f"https://api.restful-api.dev/objects/{object_id}").json()
    assert responce["id"] == object_id
    responce = requests.get(f"https://api.restful-api.dev/objects/{object_id}")
    assert responce.status_code != 404


def test_update_object(create_test_object): #обновление данных объекта
    object_id = create_test_object
    update_data = {
        "name": "Apple MacBook Pro 16 - Updated",
        "data": {
            "year": 2020,
            "price": 1999.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "2 TB",
        },
    }
    responce = requests.put(f"https://api.restful-api.dev/objects/{object_id}", json=update_data).json()
    assert responce["name"] == update_data["name"]
    responce = requests.put(f"https://api.restful-api.dev/objects/{object_id}", json=update_data)
    assert responce.status_code == 200


def test_delete_object(create_test_object): #удаление объекта
    object_id = create_test_object
    responce = requests.delete(f"https://api.restful-api.dev/objects/{object_id}")
    assert responce.status_code == 200
    responce = requests.get(f"https://api.restful-api.dev/objects/{object_id}")
    assert responce.status_code == 404


def test_partial_update_object(create_test_object): #частичное обновление объекта
    object_id = create_test_object
    partial_update_data = {
        "data": {
            "price": 1499.99
        }
    }
    responce = requests.patch(f"https://api.restful-api.dev/objects/{object_id}", json=partial_update_data).json()
    assert responce['data']["price"] == partial_update_data['data']["price"]
    responce = requests.patch(f"https://api.restful-api.dev/objects/{object_id}", json=partial_update_data)
    assert responce.status_code == 200


def test_get_nonexistent_object(): #попытка получить несуществующий объект
    nonexistent_id = "nonexistent-id-12345"
    responce = requests.get(f"https://api.restful-api.dev/objects/{nonexistent_id}")
    assert responce.status_code == 404


def test_delete_nonexistent_object(): #попытка удалить несуществующий объект
    nonexistent_id = "nonexistent-id-12345"
    responce = requests.delete(f"https://api.restful-api.dev/objects/{nonexistent_id}")
    assert responce.status_code == 404


def test_create_object_invalid_data(): #попытка создать объект с некорректными данными
    invalid_object = {
        "name": "",  # Пустое имя
        "data": {
            "year": "two thousand twenty-one",  # Некорректный формат года
            "price": -100,  # Отрицательная цена
            "CPU model": "Test CPU",
            "Hard disk size": "512 GB",
        },
    }
    responce = requests.post("https://api.restful-api.dev/objects", json=invalid_object)
    assert responce.status_code == 400  # Ожидаем ошибку клиента (Bad Request)


def test_update_object_invalid_data(create_test_object): #попытка обновить объект с некорректными данными
    object_id = create_test_object
    invalid_update_data = {
        "name": "Valid Name",
        "data": {
            "year": "invalid-year",  # Некорректный формат года
            "price": "free",  # Некорректный формат цены
            "CPU model": "Intel Core i9",
            "Hard disk size": "2 TB",
        },
    }
    responce = requests.put(f"https://api.restful-api.dev/objects/{object_id}", json=invalid_update_data)
    assert responce.status_code == 400  # Ожидаем ошибку клиента (Bad Request)


def test_get_all_objects(): #получение списка всех объектов
    responce = requests.get("https://api.restful-api.dev/objects")
    assert responce.status_code == 200
    responce = requests.get("https://api.restful-api.dev/objects").json()
    assert isinstance(responce, list)


def test_create_duplicate_object(): #попытка создать дубликат объекта
    object_data = {
        "name": "Duplicate Object",
        "data": {
            "year": 2021,
            "price": 999.99,
            "CPU model": "Test CPU",
            "Hard disk size": "512 GB",
        },
    }
    responce1 = requests.post("https://api.restful-api.dev/objects", json=object_data)
    responce2 = requests.post("https://api.restful-api.dev/objects", json=object_data)
    assert responce2.status_code == 409  # Ожидаем ошибку конфликта (Conflict)
    # Очистка созданного объекта
    created_id = responce1.json().get("id")
    requests.delete(f"https://api.restful-api.dev/objects/{created_id}")


