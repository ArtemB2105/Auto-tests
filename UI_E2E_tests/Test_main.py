import pytest
from playwright.sync_api import Page


def autorization(page: Page):
    page.goto("https://www.saucedemo.com/")  # переход на сайт
    page.locator('[data-test="username"]').click()  # клик на поле логина
    page.locator('[data-test="username"]').fill("standard_user")  # ввод логина
    page.locator('[data-test="password"]').click()  # клик на поле пароля
    page.locator('[data-test="password"]').fill("secret_sauce")  # ввод пароля
    page.locator('[data-test="login-button"]').click()  # клик на кнопку входа


class Test_autorization_field:
    def test_successful_authorization(self, page: Page):  # тестирование успешной авторизации
        page.goto("https://www.saucedemo.com/")  # переход на сайт
        page.locator('[data-test="username"]').click()  # клик на поле логина
        page.locator('[data-test="username"]').fill("standard_user")  # ввод логина
        page.locator('[data-test="password"]').click()  # клик на поле пароля
        page.locator('[data-test="password"]').fill("secret_sauce")  # ввод пароля
        page.locator('[data-test="login-button"]').click()  # клик на кнопку входа
        assert (page.url == "https://www.saucedemo.com/inventory.html")  # проверка успешной авторизации путем сравнения URL

    def test_unsuccessful_authorization_with_symbols(self, page: Page):  # тестирование неуспешной авторизации с введением символов
        page.goto("https://www.saucedemo.com/")  # переход на сайт
        page.locator('[data-test="username"]').click()  # клик на поле логина
        page.locator('[data-test="username"]').fill("aaa")  # ввод не валидных данных логина
        page.locator('[data-test="password"]').click()  # клик на поле пароля
        page.locator('[data-test="password"]').fill("aaa")  # ввод не валидных данных пароля
        page.locator('[data-test="login-button"]').click()  # клик на кнопку входа
        assert page.get_by_text("Epic sadface: Username and password do not match any user in this service").is_visible()  # проверка появления ошибки при неуспешной авторизации

    def test_unsuccessful_authorization_with_empty_fields(self, page: Page):  # тестирование неуспешной авторизации с пустыми полями
        page.goto("https://www.saucedemo.com/")  # переход на сайт
        page.locator('[data-test="login-button"]').click()  # клик на кнопку входа без ввода данных
        assert page.get_by_text("Epic sadface: Username is required").is_visible()  # проверка появления ошибки при неуспешной авторизации

    def test_unsuccessful_authorization_with_empty_password(self, page: Page):  # тестирование неуспешной авторизации с пустым полем пароля
        page.goto("https://www.saucedemo.com/")  # переход на сайт
        page.locator('[data-test="username"]').click()  # клик на поле логина
        page.locator('[data-test="username"]').fill("standard_user")  # ввод валидного логина
        page.locator('[data-test="login-button"]').click()  # клик на кнопку входа без ввода пароля
        assert page.get_by_text("Epic sadface: Password is required").is_visible()  # проверка появления ошибки при неуспешной авторизации

    def test_unsuccessful_authorization_with_empty_login(self, page: Page):  # тестирование неуспешной авторизации с пустым полем логина
        page.goto("https://www.saucedemo.com/")  # переход на сайт
        page.locator('[data-test="password"]').click()  # клик на поле пароля
        page.locator('[data-test="password"]').fill("secret_sauce")  # ввод валидного пароля
        page.locator('[data-test="login-button"]').click()  # клик на кнопку входа без ввода логина
        assert page.get_by_text("Epic sadface: Username is required").is_visible()  # проверка появления ошибки при неуспешной авторизации

    def test_closing_the_error_window(self, page: Page):  # тестирование закрытия окна с ошибкой
        page.goto("https://www.saucedemo.com/")  # переход на сайт
        page.locator('[data-test="login-button"]').click()  # клик на кнопку входа без ввода данных
        page.locator(".error-button").click()  # клик на кнопку закрытия окна с ошибкой
        assert not page.get_by_text("Epic sadface: Username is required").is_visible()  # проверка закрытия окна с ошибкой


class Test_after_authorization:
    def test_logout(self, authorized_page: Page):  # тестирование выхода из аккаунта
        page = authorized_page
        page.locator("#react-burger-menu-btn").click()  # клик на кнопку открытия меню
        page.locator("#logout_sidebar_link").click()  # клик на кнопку выхода из аккаунта
        assert page.url == "https://www.saucedemo.com/"  # проверка успешного выхода из аккаунта путем сравнения URL

    def test_adding_product_to_cart(self, authorized_page: Page):  # тестирование добавления товара в корзину
        page = authorized_page
        page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()  # клик на кнопку добавления товара в корзину
        page.locator(".shopping_cart_link").click()  # переход в корзину
        assert page.get_by_text("Sauce Labs Backpack").is_visible()  # проверка успешного добавления товара в корзину путем проверки наличия количества товаров в корзине

    def test_deleting_product_from_cart(self, authorized_page: Page):  # тестирование удаления товара из корзины
        page = authorized_page
        page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()  # клик на кнопку добавления товара в корзину
        page.locator(".shopping_cart_link").click()  # переход в корзину
        page.locator('[data-test="remove-sauce-labs-backpack"]').click()  # клик на кнопку удаления товара из корзины
        assert not page.get_by_text("Sauce Labs Backpack").is_visible()  # проверка успешного удаления товара из корзины путем проверки отсутствия товара в корзине

    def test_successful_order_placement(self, authorized_page: Page):  # тестирование процесса оформления заказа
        page = authorized_page
        page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()  # клик на кнопку добавления товара в корзину
        page.locator(".shopping_cart_link").click()  # переход в корзину
        page.locator('[data-test="checkout"]').click()  # клик на кнопку оформления заказа
        page.locator('[data-test="firstName"]').click()  # клик на поле имени
        page.locator('[data-test="firstName"]').fill("John")  # ввод имени
        page.locator('[data-test="lastName"]').click()  # клик на поле фамилии
        page.locator('[data-test="lastName"]').fill("Doe")  # ввод фамилии
        page.locator('[data-test="postalCode"]').click()  # клик на поле почтового индекса
        page.locator('[data-test="postalCode"]').fill("12345")  # ввод почтового индекса
        page.locator('[data-test="continue"]').click()  # клик на кнопку продолжения оформления заказа
        page.locator('[data-test="finish"]').click()  # клик на кнопку завершения оформления заказа
        assert page.get_by_text("THANK YOU FOR YOUR ORDER").is_visible()  # проверка успешного оформления заказа путем проверки наличия текста подтверждения заказа

    def test_unsuccessful_order_placement_with_empty_fields(self, authorized_page: Page):  # тестирование неуспешного оформления заказа с пустыми полями
        page = authorized_page
        page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()  # клик на кнопку добавления товара в корзину
        page.locator(".shopping_cart_link").click()  # переход в корзину
        page.locator('[data-test="checkout"]').click()  # клик на кнопку оформления заказа
        page.locator('[data-test="continue"]').click()  # клик на кнопку продолжения оформления заказа без ввода данных
        assert page.get_by_text("Error: First Name is required").is_visible()  # проверка появления ошибки при неуспешном оформлении заказа

    def test_unsuccessful_order_placement_with_empty_last_name(self, authorized_page: Page):  # тестирование неуспешного оформления заказа с пустым полем фамилии
        page = authorized_page
        page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()  # клик на кнопку добавления товара в корзину
        page.locator(".shopping_cart_link").click()  # переход в корзину
        page.locator('[data-test="checkout"]').click()  # клик на кнопку оформления заказа
        page.locator('[data-test="firstName"]').click()  # клик на поле имени
        page.locator('[data-test="firstName"]').fill("John")  # ввод имени
        page.locator('[data-test="postalCode"]').click()  # клик на поле почтового индекса
        page.locator('[data-test="postalCode"]').fill("12345")  # ввод почтового индекса
        page.locator('[data-test="continue"]').click()  # клик на кнопку продолжения оформления заказа
        assert page.get_by_text("Error: Last Name is required").is_visible()  # проверка появления ошибки при неуспешном оформлении заказа

    def test_unsuccessful_order_placement_with_empty_postal_code(self, authorized_page: Page):  # тестирование неуспешного оформления заказа с пустым полем почтового индекса
        page = authorized_page
        page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()  # клик на кнопку добавления товара в корзину
        page.locator(".shopping_cart_link").click()  # переход в корзину
        page.locator('[data-test="checkout"]').click()  # клик на кнопку оформления заказа
        page.locator('[data-test="firstName"]').click()  # клик на поле имени
        page.locator('[data-test="firstName"]').fill("John")  # ввод имени
        page.locator('[data-test="lastName"]').click()  # клик на поле фамилии
        page.locator('[data-test="lastName"]').fill("Doe")  # ввод фамилии
        page.locator('[data-test="continue"]').click()  # клик на кнопку продолжения оформления заказа
        assert page.get_by_text("Error: Postal Code is required").is_visible()  # проверка появления ошибки при неуспешном оформлении заказа

    def test_canceling_order_placement(self, authorized_page: Page):  # тестирование отмены оформления заказа
        page = authorized_page
        page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()  # клик на кнопку добавления товара в корзину
        page.locator(".shopping_cart_link").click()  # переход в корзину
        page.locator('[data-test="checkout"]').click()  # клик на кнопку оформления заказа
        page.locator('[data-test="firstName"]').click()  # клик на поле имени
        page.locator('[data-test="firstName"]').fill("John")  # ввод имени
        page.locator('[data-test="lastName"]').click()  # клик на поле фамилии
        page.locator('[data-test="lastName"]').fill("Doe")  # ввод фамилии
        page.locator('[data-test="postalCode"]').click()  # клик на поле почтового индекса
        page.locator('[data-test="postalCode"]').fill("12345")  # ввод почтового индекса
        page.locator('[data-test="cancel"]').click()  # клик на кнопку отмены оформления заказа
        assert page.url == "https://www.saucedemo.com/cart.html"  # проверка успешной отмены оформления заказа путем сравнения URL

    def test_sorting_products_by_price_low_to_high(self, authorized_page: Page):  # тестирование сортировки товаров по цене от низкой к высокой
        page = authorized_page
        page.locator('[data-test="product-sort-container"]').select_option("lohi")  # выбор опции сортировки по цене от низкой к высокой
        assert page.locator(".inventory_item_price").first.inner_text() == "$7.99"  # проверка что первый товар имеет минимальную цену
        assert page.locator(".inventory_item_price").last.inner_text() == "$49.99"  # проверка что последний товар имеет максимальную цену

    def test_sorting_products_by_price_high_to_low(self, authorized_page: Page):  # тестирование сортировки товаров по цене от высокой к низкой
        page = authorized_page
        page.locator('[data-test="product-sort-container"]').select_option("hilo")  # выбор опции сортировки по цене от высокой к низкой
        assert page.locator(".inventory_item_price").first.inner_text() == "$49.99"  # проверка что первый товар имеет максимальную цену
        assert page.locator(".inventory_item_price").last.inner_text() == "$7.99"  # проверка что последний товар имеет минимальную цену

    def test_sorting_products_by_name_a_to_z(self, authorized_page: Page):  # тестирование сортировки товаров по названию от А до Я
        page = authorized_page
        page.locator('[data-test="product-sort-container"]').select_option("az")  # выбор опции сортировки по названию от А до Я
        assert page.locator(".inventory_item_name").first.inner_text() == "Sauce Labs Backpack"  # проверка что первый товар соответствует первой позиции в алфавите
        assert page.locator(".inventory_item_name").last.inner_text() == "Test.allTheThings() T-Shirt (Red)"  # проверка что последний товар соответствует последней позиции в алфавите

    def test_sorting_products_by_name_z_to_a(self, authorized_page: Page):  # тестирование сортировки товаров по названию от Я до А
        page = authorized_page
        page.locator('[data-test="product-sort-container"]').select_option("za")  # выбор опции сортировки по названию от Я до А
        assert page.locator(".inventory_item_name").first.inner_text() == "Test.allTheThings() T-Shirt (Red)"  # проверка что первый товар соответствует последней позиции в алфавите
        assert page.locator(".inventory_item_name").last.inner_text() == "Sauce Labs Backpack"  # проверка что последний товар соответствует первой позиции в алфавите

    def test_viewing_product_details(self, authorized_page: Page):  # тестирование просмотра деталей товара
        page = authorized_page
        page.locator("text=Sauce Labs Backpack").click()  # клик на товар для просмотра деталей
        assert page.get_by_text("Sauce Labs Backpack").is_visible()  # проверка что открылась страница с деталями товара
        assert page.get_by_text("carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection.").is_visible()  # проверка что описание товара отображается корректно

    def test_back_to_products_page(self, authorized_page: Page):  # тестирование возврата на страницу с товарами из страницы деталей товара
        page = authorized_page
        page.locator("text=Sauce Labs Backpack").click()  # клик на товар для просмотра деталей
        page.locator('[data-test="back-to-products"]').click()  # клик на кнопку возврата на страницу с товарами
        assert page.url == "https://www.saucedemo.com/inventory.html"  # проверка успешного возврата на страницу с товарами путем сравнения URL

    def test_check_cart_quantity_indicator(self, authorized_page: Page):  # тестирование индикатора количества товаров в корзине
        page = authorized_page
        page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()  # добавление первого товара в корзину
        page.locator('[data-test="add-to-cart-sauce-labs-bike-light"]').click()  # добавление второго товара в корзину
        assert page.locator(".shopping_cart_badge").inner_text() == "2"  # проверка что индикатор количества товаров в корзине отображает корректное количество
