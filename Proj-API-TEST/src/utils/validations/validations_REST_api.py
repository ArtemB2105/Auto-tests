from typing import Optional
import allure
from requests import Response
from http import HTTPStatus

from src.utils.validations.assert_wrappers import assert_eq

@allure.step("Проверка валидности ответа")
def validate_response(response: Response, expected_status_code: HTTPStatus, expected_text: Optional[str]= None) -> None:

    with allure.step("Проверка статус кода"):
        assert_eq(actual_value=response.status_code, expected_value=expected_status_code, allure_title="Проверка статус кода ответа",
                  error_msg=f"Получен некорректный код ответа: ожидаемый={expected_status_code}," 
                            f"фактический={response.status_code}")
    
    if expected_text:
        with allure.step("Проверка текста ответа"):
            assert_eq(actual_value=response.text, expected_value=expected_text, allure_title="Проверка текста ответа",
                      error_msg=f"Получен некорректный текст ответа: ожидаемый={expected_text}," 
                                f"фактический={response.text}")