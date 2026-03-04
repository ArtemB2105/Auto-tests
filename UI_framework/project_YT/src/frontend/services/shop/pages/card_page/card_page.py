from project_YT.src.frontend.services.shop.elements.navbar_element.navbar_element import NavbarElement
from project_YT.src.frontend.src.base_page.base_page import BasePage


class CardPage:

    def __init__(self, base_page : BasePage):
        self._base_page = base_page
        self.navbar_elem = NavbarElement(self)


    def open(self) -> "CardPage":
        self.navbar_elem.open_cart_page()
        return self