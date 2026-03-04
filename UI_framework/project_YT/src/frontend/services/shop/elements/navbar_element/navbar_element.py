

import allure





class NavbarElementLocators:
    CART_BUTTON = "#shopping_cart_container"
    BURGER_MENU_BUTTON = "#react-burger-menu-btn"


class NavbarElement:
    def __init__(self, base_page):
        self._base_page = base_page




    @allure.step("Открытие страницы корзины")
    def open_cart_page(self) -> None:
        self._base_page.click(selector=NavbarElementLocators.CART_BUTTON)


    @allure.step("Открытие бургер-меню")
    def open_burger_menu(self) -> None:
        self._base_page.click(selector=NavbarElementLocators.BURGER_MENU_BUTTON)