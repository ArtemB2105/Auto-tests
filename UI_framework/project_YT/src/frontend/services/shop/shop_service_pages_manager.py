from project_YT.src.frontend.services.shop.pages.card_page.card_page import CardPage
from project_YT.src.frontend.services.shop.pages.catalog_page.catalog_page import CatalogPage
from project_YT.src.frontend.services.shop.pages.login_page.login_page import LoginPage
from project_YT.src.frontend.src.base_page.base_page import BasePage



class ShopServicePagesManager:



    def __init__(self, base_page: BasePage):
        self.login_page = LoginPage(base_page=base_page)
        self.catalog_page = CatalogPage(base_page)
        self.card_page = CardPage(base_page)