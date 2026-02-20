from project_YT.src.frontend.src.base_page.base_page import BasePage
import allure
from typing import Optional


class LoginPageLocators:
    USERNAME_INPUT = "input[placeholder = 'Username']"
    PASSWORD_INPUT = "input[placeholder = 'Password']"
    LOGIN_BUTTON = "input[type = 'submit']"


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