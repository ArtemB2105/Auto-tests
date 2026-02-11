import pytest
import allure
from playwright.sync_api import Browser, sync_playwright

from project_YT.src.frontend.src.base_page.base_page import BasePage

@allure.step("Запуск браузера")
@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:   
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def base_page(browser) -> BasePage:
    page = browser.new_context().new_page()
    return BasePage(page=page)
    

