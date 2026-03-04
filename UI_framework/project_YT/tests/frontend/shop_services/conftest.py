import pytest


from project_YT.src.frontend.services.shop.pages.catalog_page.catalog_page import CatalogPage
from project_YT.src.frontend.services.shop.pages.login_page.login_page import LoginPage
from project_YT.config import TestConfig
from project_YT.src.frontend.services.shop.shop_service_pages_manager import ShopServicePagesManager
from project_YT.src.frontend.src.base_page.base_page import BasePage



@pytest.fixture
def shop_base_page(page) -> BasePage:
    page.goto(TestConfig.SHOP_BASE_URL)
    return BasePage(page)


@pytest.fixture
def login_page(shop_base_page) -> LoginPage:
    return LoginPage(base_page=shop_base_page)


@pytest.fixture
def catalog_page(shop_base_page) -> CatalogPage:
    return CatalogPage(base_page=shop_base_page)


@pytest.fixture
def shop_service_pages_manager_logon(shop_base_page) -> ShopServicePagesManager:
    pages_manager = ShopServicePagesManager(base_page=shop_base_page)
    pages_manager.login_page.login(username="standard_user", password="secret_sauce")
    return pages_manager


