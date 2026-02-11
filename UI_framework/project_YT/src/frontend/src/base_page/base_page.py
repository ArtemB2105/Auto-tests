import allure
from playwright.sync_api import Locator
from playwright.sync_api import Page

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
    

        
        