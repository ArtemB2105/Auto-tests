from enum import StrEnum
from typing import Optional
import allure
from requests import Response
from src.backend.clients.http.client import HTTPClient



class Route(StrEnum):
    USERS = "users"
    LOGIN = "auth/login"
    DELETE = USERS
    


class FakeApiAuthAdapter:

    def __init__(self,http_client: HTTPClient, route: Route = Route):
        self._http_client = http_client
        self._route = route

    @allure.step("Регистрация нового пользователя")
    def register(self, username: Optional[str] = None, email: Optional[str] = None, password: Optional[str] = None) -> Response:
        user_data = {}
        if username is not None:
            user_data["userbane"] = username
        if email is not None:
            user_data["email"] = email
        if password is not None:
            user_data["password"] = password
        
        
        return self._http_client.post(route=self._route.USERS, json=user_data)
    


    @allure.step("Логин пользователя")
    def login(self, username: Optional[str] = None, password: Optional[str] = None) -> Response:
        login_data = {}
        if username is not None:
            login_data["usernane"] = username
        if password is not None:
            login_data["password"] = password
        return self._http_client.post(route=self._route.LOGIN, json=login_data)
    

    @allure.step("Удаление пользователя")
    def delete_user(self, user_id : Optional[str | int] = None) -> Response:
        route = self._route.DELETE
        if user_id is not None:
            route = f"{route}/{user_id}"

        return self._http_client.delete(route=route)