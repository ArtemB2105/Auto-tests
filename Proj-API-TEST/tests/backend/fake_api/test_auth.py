import http
import allure
from src.utils.validations.assert_wrappers import assert_eq, assert_in
from src.utils.validations.validations_REST_api import validate_response





pytestmark = [allure.feature("Тесты на сервис аутентификации")]


@allure.title("Валидное создание пользователя")
def test_create_new_user_positive(fake_api_auth_adapter):
    response = fake_api_auth_adapter.register(username="sdfsdf", email="sdf@gmail.com" ,password="pass123")
    assert_eq(expected_value=response.status_code, actual_value=201, error_msg="Пользователь не был успешно создан", 
              allure_title="Проверка успешности создания пользователя")
    assert_in(actual_value="id", expected_container=response.json(), allure_title="Проверка что  поле id есть в ответе")



@allure.title("Создание пользователя позитивное, пароль 12 символов")
def test_create_new_user_positive_password_len_12(fake_api_auth_adapter):
    response = fake_api_auth_adapter.register(username="john_doe", email="john@example.com" ,password="pass12387654")    
    with allure.step("Проверка ответа"):    
        assert response.status_code == 201, "Статус код не 201"
        assert "id" in response.json()    



@allure.title("Создание пользователя негативное, не передан username")
def test_create_new_user_negative_without_username(fake_api_auth_adapter):
    response = fake_api_auth_adapter.register(email="sdf@gmail.com" ,password="pass123")
    assert_eq(expected_value=response.status_code, actual_value=400, error_msg="Пользователь был успешно создан", 
              allure_title="Проверка неуспешности создания пользователя")
         
    


@allure.title("Регистрация пользователя с валидными данными")
def test_login_user_valid_creads(fake_api_auth_adapter, create_user):
    response = fake_api_auth_adapter.login(username=create_user["username"], password=create_user["password"])


@allure.title("Регистрация пользователя с невалидными данными логина")
def test_login_user_dont_valid_username(fake_api_auth_adapter, create_user, faker):
    response = fake_api_auth_adapter.login(username=faker.user_name(), password=create_user["password"])
    validate_response(response=response,expected_status_code=http.HTTPStatus.BAD_REQUEST, 
                      expected_text="username and password are not provided in JSON format")


@allure.title("Регистрация пользователя с невалидными данными пароля")
def test_login_user_dont_valid_password(fake_api_auth_adapter, create_user, faker):
    response = fake_api_auth_adapter.login(username=create_user["username"], password=faker.password())
    validate_response(response=response,expected_status_code=http.HTTPStatus.BAD_REQUEST, 
                      expected_text="username and password are not provided in JSON format")
    
