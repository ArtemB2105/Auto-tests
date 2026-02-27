import allure

INVALID_CREDS_ERROR = "Epic sadface: Username and password do not match any user in this service"
EMPTY_CREDS_ERROR = "Epic sadface: Username is required"

pytestmark = [allure.feature("Тесты на Логин")]





@allure.feature("Тесты на Логин")
class TestLogin:
    @allure.title("Успешная авторизация")
    def test_login_valid_creds(self, login_page):
        login_page.login(username="standard_user", password="secret_sauce")



    @allure.title("Не успешная авторизация вводом не валидных данных")
    def test_login_no_valid_creds(self, login_page):
        login_page.login(username="standard_user123", password="secret_sauce123")
        login_page.get_error_message(expected_text=INVALID_CREDS_ERROR)


    @allure.title("Не успешная авторизация вводом пустых строк")
    def test_login_empty_creds(self, login_page):
        login_page.login()
        login_page.get_error_message(expected_text=EMPTY_CREDS_ERROR)
        