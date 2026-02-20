import allure


pytestmarks = [allure.feature("Тесты на Логин")]







@allure.title("Успешная авторизация")
def test_login_valid_creds(login_page):
    login_page.login(username="standard_user", password="secret_sauce")


@allure.title("Не успешная авторизация вводом не валидных данных")
def test_login_no_valid_creds(login_page):
    login_page.login(username="standard_user123", password="secret_sauce123")


@allure.title("Не успешная авторизация вводом пустых строк")
def test_login_empty_creds(login_page):
    login_page.login()
    