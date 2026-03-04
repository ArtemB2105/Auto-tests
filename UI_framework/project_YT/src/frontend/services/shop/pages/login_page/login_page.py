from project_YT.src.frontend.src.base_page.base_page import BasePage
import allure
from typing import Optional

ERROR_MESSAGE_TEXT = "Epic sadface: Username and password do not match any user in this service"


class LoginPageLocators:
    USERNAME_INPUT = "input[placeholder = 'Username']"
    PASSWORD_INPUT = "input[placeholder = 'Password']"
    LOGIN_BUTTON = "input[type = 'submit']"
    ERROR_MESSAGE = ".error-message-container"


class LoginPage:

    def __init__(self, base_page : BasePage):
        self._base_page = base_page

    @allure.step("Логин пользователя") 
    def login(self, username: Optional[str] = None, password: Optional[str] = None) -> "LoginPage":
        if username:
            self._base_page.fill(selector=LoginPageLocators.USERNAME_INPUT, value=username)
        if password:
            self._base_page.fill(selector=LoginPageLocators.PASSWORD_INPUT, value=password)
        self._base_page.click(selector=LoginPageLocators.LOGIN_BUTTON)

        return self

    @allure.step("Получение сообщения об ошибке")
    def get_error_message(self, expected_text: Optional[str] = ERROR_MESSAGE_TEXT) -> str:
        self._base_page.expect(selector=LoginPageLocators.ERROR_MESSAGE).to_be_attached()
        actual_text = self._base_page.get_text(selector=LoginPageLocators.ERROR_MESSAGE)
        if expected_text is not None:
            assert actual_text == expected_text, "Сообщение об ошибке не соответствует ожидаемому"
        return actual_text
        