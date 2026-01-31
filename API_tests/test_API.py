import requests
import pytest
import allure


@allure.feature("CRUD операции с объектами")
@allure.story("Создание объекта")
@pytest.mark.parametrize("object_data", [
    { "name": "MacBook Pro 16",
      "data": { 
            "year": 2021,
            "price": 999.99,
            "CPU model": "Test CPU",
            "Hard disk size": "512 GB",
        },
    },
    { "name": "Dell XPS 13",
        "data": {
            "year": 2020,
            "price": 1199.99,
            "CPU model": "Intel Core i7",
            "Hard disk size": "1 TB",
        },
    },
    { "name": "Lenovo ThinkPad X1 Carbon",
        "data": {
            "year": 2019,
            "price": 1399.99,
            "CPU model": "Intel Core i5",
            "Hard disk size": "256 GB",
        },
    },
])
def test_add_object(object_data): 
    response = requests.post("https://api.restful-api.dev/objects", json=object_data)
    assert response.status_code == 200
    
    response_data = response.json()
    assert response_data["name"] == object_data["name"]
    assert "id" in response_data
    assert response_data["data"]["year"] == object_data["data"]["year"]
    assert response_data["data"]["price"] == object_data["data"]["price"]
    


@allure.feature("CRUD операции с объектами")
@allure.story("Получение объекта")
def test_get_object(create_test_object):
    object_id = create_test_object
    response = requests.get(f"https://api.restful-api.dev/objects/{object_id}").json()
    assert response["id"] == object_id
    response = requests.get(f"https://api.restful-api.dev/objects/{object_id}")
    assert response.status_code != 404


@allure.feature("CRUD операции с объектами")
@allure.story("Обновление объекта")
def test_update_object(create_test_object): 
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
    response = requests.put(f"https://api.restful-api.dev/objects/{object_id}", json=update_data).json()
    assert response["name"] == update_data["name"]
    response = requests.put(f"https://api.restful-api.dev/objects/{object_id}", json=update_data)
    assert response.status_code == 200


@allure.feature("CRUD операции с объектами")
@allure.story("Удаление объекта")
def test_delete_object(create_test_object): 
    object_id = create_test_object
    response = requests.delete(f"https://api.restful-api.dev/objects/{object_id}")
    assert response.status_code == 200
    response = requests.get(f"https://api.restful-api.dev/objects/{object_id}")
    assert response.status_code == 404


@allure.feature("CRUD операции с объектами")
@allure.story("Частичное обновление объекта")
def test_partial_update_object(create_test_object): 
    object_id = create_test_object
    partial_update_data = {
        "data": {
            "price": 1499.99
        }
    }
    response = requests.patch(f"https://api.restful-api.dev/objects/{object_id}", json=partial_update_data).json()
    assert response['data']["price"] == partial_update_data['data']["price"]
    response = requests.patch(f"https://api.restful-api.dev/objects/{object_id}", json=partial_update_data)
    assert response.status_code == 200


@allure.feature("Негативные тесты для API управления объектами")
@allure.story("Получение несуществующего объекта")
def test_get_nonexistent_object(): 
    nonexistent_id = "nonexistent-id-12345"
    response = requests.get(f"https://api.restful-api.dev/objects/{nonexistent_id}")
    assert response.status_code == 404


@allure.feature("Негативные тесты для API управления объектами")
@allure.story("Удаление несуществующего объекта")
def test_delete_nonexistent_object(): 
    nonexistent_id = "nonexistent-id-12345"
    response = requests.delete(f"https://api.restful-api.dev/objects/{nonexistent_id}")
    assert response.status_code == 404


@allure.feature("Негативные тесты для API управления объектами")
@allure.story("Создание объекта с некорректными данными")
def test_create_object_invalid_data(): 
    invalid_object = {
        "name": "",  # Пустое имя
        "data": {
            "year": "two thousand twenty-one",  # Некорректный формат года
            "price": -100,  # Отрицательная цена
            "CPU model": "Test CPU",
            "Hard disk size": "512 GB",
        },
    }
    response = requests.post("https://api.restful-api.dev/objects", json=invalid_object)
    assert response.status_code == 400  # Ожидаем ошибку клиента (Bad Request)


@allure.feature("Негативные тесты для API управления объектами")
@allure.story("Обновление объекта с некорректными данными")
def test_update_object_invalid_data(create_test_object): 
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
    response = requests.put(f"https://api.restful-api.dev/objects/{object_id}", json=invalid_update_data)
    assert response.status_code == 400  # Ожидаем ошибку клиента (Bad Request)


@allure.feature("CRUD операции с объектами")
@allure.story("Список всех объектов")
def test_get_all_objects(): #получение списка всех объектов
    response = requests.get("https://api.restful-api.dev/objects")
    assert response.status_code == 200
    response = requests.get("https://api.restful-api.dev/objects").json()
    assert isinstance(response, list)


@allure.feature("Негативные тесты для API управления объектами")
@allure.story("Создание дубликата объекта")
def test_create_duplicate_object(): 
    object_data = {
        "name": "Duplicate Object",
        "data": {
            "year": 2021,
            "price": 999.99,
            "CPU model": "Test CPU",
            "Hard disk size": "512 GB",
        },
    }
    responcs1 = requests.post("https://api.restful-api.dev/objects", json=object_data)
    responcs2 = requests.post("https://api.restful-api.dev/objects", json=object_data)
    assert responcs2.status_code == 409  # Ожидаем ошибку конфликта (Conflict)
    # Очистка созданного объекта
    created_id = responcs1.json().get("id")
    requests.delete(f"https://api.restful-api.dev/objects/{created_id}")


