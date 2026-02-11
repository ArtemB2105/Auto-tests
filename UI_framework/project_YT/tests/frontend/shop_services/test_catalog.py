


import random
import allure


pytestmarks = [allure.feature("Тесты на каталог")]
def test_get_all_catalog(login_page, catalog_page):
    login_page.login(username = "standard_user", password = "secret_sauce")
    all_goods = catalog_page.get_all_goods()
    catalog_page.add_good_to_cart(random.choice(all_goods))