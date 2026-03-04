from datetime import datetime
import json

import pytest
import allure
from playwright.sync_api import Browser, ConsoleMessage, Request, Response, sync_playwright

from project_YT.src.frontend.src.base_page.base_page import BasePage

@allure.step("Запуск браузера")
@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:   
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def base_page(browser) -> BasePage:
    page = browser.new_context().new_page()
    return BasePage(page=page)


@allure.step("Сбор логов консоли, запросов и ответов")
@pytest.fixture(scope="function", autouse=True)
def ui_report(base_page, request:pytest.FixtureRequest, tmp_path):
    
    console_logs = []
    network_logs = []

    playwright_page = base_page.page

    def current_timestamp():
        return datetime.now().strftime("%d-%m-%Y %H:%M:%S.%f")

    def on_console(msg: ConsoleMessage):
        console_logs.append({
            "timestamp": current_timestamp(),
            "type": msg.type,
            "text": msg.text
        })

    def on_request(req: Request):
        # Упрощенная версия - всегда берем post_data как есть
        data = req.post_data if req.post_data else "no data"
        
        network_logs.append({
            "timestamp": current_timestamp(),
            "event": "REQUEST",
            "method": req.method,
            "headers": req.headers,
            "resource_type": req.resource_type,
            "data": data,
            "url": req.url
        })

    def on_response(res: Response):
        content_type = res.headers.get("content-type", "").lower()
        response_body = None

        try:
            if "application/json" in content_type:
                response_body = res.json()
            elif "text/" in content_type:
                response_body = res.text()
            else:
                response_body = "binary content"
        except Exception:
            response_body = "failed to get response body"
        
        network_logs.append({
            "timestamp": current_timestamp(),
            "event": "RESPONSE",
            "status": res.status,
            "url": res.url,
            "response_content_type": content_type,
            "response_body": response_body
        })

    # Подписка на события
    playwright_page.on("console", on_console)
    playwright_page.on("request", on_request)
    playwright_page.on("response", on_response)

    failed_tests_count = request.session.testsfailed
    yield

    # Если тест упал - сохраняем логи
    if request.session.testsfailed > failed_tests_count:
        # Скриншот
        screenshot_path = tmp_path / "failure.png"
        base_page.attach_screenshot(path_to_save=str(screenshot_path))

        # Логи консоли
        console_log_path = tmp_path / "console_logs.json"
        with allure.step("Логи консоли"):
            with open(console_log_path, "w", encoding="utf-8") as f:
                json.dump(console_logs, f, ensure_ascii=False, indent=2, default=str)
            
            allure.attach(
                console_log_path.read_text(encoding="utf-8"),
                name="console_logs.json",
                attachment_type=allure.attachment_type.JSON
            )

        # Логи сети
        with allure.step("Логи сети"):
            network_log_path = tmp_path / "network_logs.json"
            with open(network_log_path, "w", encoding="utf-8") as f:
                json.dump(network_logs, f, ensure_ascii=False, indent=2, default=str)
            
            allure.attach(
                network_log_path.read_text(encoding="utf-8"),
                name="network_logs.json",
                attachment_type=allure.attachment_type.JSON
            )

    # Удаляем слушателей в любом случае
    playwright_page.remove_listener("console", on_console)
    playwright_page.remove_listener("request", on_request)
    playwright_page.remove_listener("response", on_response)

