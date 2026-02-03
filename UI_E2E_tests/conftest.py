import pytest
import os
from playwright.sync_api import sync_playwright, Page


@pytest.fixture
def page() -> Page:
    """Фикстура для создания страницы Playwright"""
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
        
        context = browser.new_context(
            viewport={'width': 1920, 'height': 1080},
            ignore_https_errors=True
        )
        
        page = context.new_page()
        page.set_default_timeout(30000)
        
        yield page
        
        page.close()
        context.close()
        browser.close()


@pytest.fixture
def authorized_page(page: Page) -> Page:
    """Фикстура для авторизованной страницы"""
    page.goto("https://www.saucedemo.com/") 
    page.locator("[data-test=\"username\"]").fill("standard_user") 
    page.locator("[data-test=\"password\"]").fill("secret_sauce") 
    page.locator("[data-test=\"login-button\"]").click() 
    page.wait_for_url("**/inventory.html") 
    return page
