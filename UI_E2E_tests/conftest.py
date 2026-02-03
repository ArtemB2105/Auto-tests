import pytest
import os
from playwright.sync_api import Page
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function", autouse=True)
def authorized_page(page: Page):
    #Возвращает авторизованную страницу
    page.goto("https://www.saucedemo.com/") 
    page.locator("[data-test=\"username\"]").fill("standard_user") 
    page.locator("[data-test=\"password\"]").fill("secret_sauce") 
    page.locator("[data-test=\"login-button\"]").click() 
    page.wait_for_url("https://www.saucedemo.com/inventory.html") 
    return page 


@pytest.fixture()
def browser():
    
    is_ci = os.getenv('CI') or os.getenv('GITHUB_ACTIONS')
    
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True if is_ci else False,  
            args=[
                '--no-sandbox',
                '--disable-dev-shm-usage',
                '--start-maximized'  
            ]
        )
        yield browser
        browser.close()