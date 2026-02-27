


import random
import allure


pytestmark = [allure.feature("Тесты на каталог")]



@allure.feature("Тесты на каталог")
class TestCatalog:
    @allure.title("Получение всех товаров в каталоге")
    def test_get_all_catalog(self, login_page, catalog_page):
        login_page.login(username = "standard_user", password = "secret_sauce")
        all_goods = catalog_page.get_all_goods()
        catalog_page.add_good_to_cart(random.choice(all_goods))