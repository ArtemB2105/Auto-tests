import allure
from os.path import basename
from playwright.sync_api import Locator, LocatorAssertions, Page, expect

from project_YT.config import TestConfig



class BasePage:
    def __init__(self, page: Page, wait_timeout: int = TestConfig.UI_Config.PLAYWRIGHT_WAIT_TIMEOUT):
        self.page = page
        self.default_timeout = wait_timeout

    @allure.step("Переход по URL: {url}")
    def open(self, url: str) -> None:
        self.page.goto(url=url)
        self.page.wait_for_load_state(state="domcontentloaded", timeout=self.default_timeout)

    @allure.step("Получение локатора: {selector}")
    def locator(self, selector: str) -> Locator:
        locator = self.page.locator(selector=selector)
        locator.wait_for(timeout=self.default_timeout, state="attached")
        return locator



    @allure.step("Ввод текста '{value}' в элемент с селектором: {selector}")    
    def fill(self, selector: str, value: str) -> None:
        self.locator(selector=selector).fill(value=value)

    @allure.step("Клик по элементу с селектором: {selector}")
    def click(self, selector: str) -> None:
        self.locator(selector=selector).click()

    @allure.step("Получение всех элементов с селектором {selector}")
    def get_all_elements(self, selector: str,) -> list[Locator]:
        self.page.locator(selector).first.wait_for(timeout=self.default_timeout, state="attached")
        return self.page.locator(selector).all()


    @allure.step("Проверка для элемента: {selector}")
    def expect(self, selector: str) -> LocatorAssertions:
        return expect(self.page.locator(selector))

    @allure.step("Получение текста элемента: {selector}")
    def get_text(self, selector: str) -> str:
        return self.locator(selector).text_content()

    


    @allure.step("Получение скриншота")
    def attach_screenshot(self, path_to_save: str) -> None:
        screenshot = self.page.screenshot(full_page=True, path=path_to_save, type="png")
        allure.attach(screenshot, name="screenshot.png",attachment_type=allure.attachment_type.PNG) 
        
    

        
        