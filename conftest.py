import pytest
from playwright.sync_api import Page

@pytest.fixture(scope="function", autouse=True)
def authorized_page(page: Page):
    #Возвращает авторизованную страницу
    page.goto("https://www.saucedemo.com/") 
    page.locator("[data-test=\"username\"]").fill("standard_user") 
    page.locator("[data-test=\"password\"]").fill("secret_sauce") 
    page.locator("[data-test=\"login-button\"]").click() 
    page.wait_for_url("https://www.saucedemo.com/inventory.html") 
    return page 