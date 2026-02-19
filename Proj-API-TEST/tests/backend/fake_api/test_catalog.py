


import http
import allure

from src.utils.validations.validations_REST_api import validate_response


@allure.title("Получение всего каталога")
@allure.feature("Тесты на каталог")
def test_get_all_catalog_without_filter(fake_api_catalog_adapter_with_auth):
    response = fake_api_catalog_adapter_with_auth.get_catalog()
    validate_response(response=response,expected_status_code=http.HTTPStatus.OK)




@allure.title("Получение всего каталога без аутентификации")
@allure.feature("Тесты на каталог")
def test_get_all_catalog_without_filter_no_auth(fake_api_catalog_adapter_no_auth):
    response = fake_api_catalog_adapter_no_auth.get_catalog()
    validate_response(response=response,expected_status_code=http.HTTPStatus.UNAUTHORIZED)



