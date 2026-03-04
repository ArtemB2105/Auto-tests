


import random
import allure


pytestmark = [allure.feature("Тесты на каталог")]



@allure.feature("Тесты на каталог")
class TestCatalog:
    @allure.title("Получение всех товаров в каталоге")
    def test_get_all_catalog(self, shop_service_pages_manager_logon):
        all_goods = shop_service_pages_manager_logon.catalog_page.get_all_goods()
        shop_service_pages_manager_logon.catalog_page.add_good_to_cart(random.choice(all_goods))

    @allure.title("Получение товаров по существующему бренду")
    def test_get_all_catalog_by_existed_brand(self, shop_service_pages_manager_logon):
        pass

    @allure.title("Получение товаров по несуществующему бренду")
    def test_get_all_catalog_by_nonexistent_brand(self, shop_service_pages_manager_logon):
        pass