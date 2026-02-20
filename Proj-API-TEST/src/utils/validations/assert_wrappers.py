import json
import allure



from typing import Any, Optional


def assert_eq(
        actual_value: Any,
        expected_value: Any,
        allure_title: str,
        error_msg: Optional[str] = None
) -> None:        
        with allure.step(allure_title):
            try:
                assert actual_value == expected_value, error_msg or "Сравнимаемые значения не равны"
            except AssertionError:
                attach_response = {
                      "Actual_value": str(actual_value),
                      "Expected_value": str(expected_value)
                }
                _allure_attach_error(attach_response=attach_response,error_name="Values comparison error")
                raise
        


def assert_in(
        actual_value: Any,
        expected_container: Any,
        allure_title: str,
        error_msg: Optional[str] = None
) -> None:
    with allure.step(allure_title):
        try:
            assert actual_value in expected_container, error_msg or f"{actual_value} не найден в контейнере"
        except AssertionError:
            attach_response = {
                "Actual_value": str(actual_value),
                "Expected_container": str(expected_container)
            }
            _allure_attach_error(attach_response=attach_response,
                                 error_name="Expected container does not exist expected value")
            raise



def _allure_attach_error(attach_response: dict, error_name:str) -> None:
     allure.attach(
          json.dumps(attach_response, indent="\t", separators=(",",": "),ensure_ascii=False),
          error_name,
          attachment_type=allure.attachment_type.JSON
     )




def assert_not_eq():
    pass




def assert_bool(
    actual_value: Any,
    expected_bool: bool,
    allure_title: str,
    error_msg: Optional[str] = None
) -> None:
    with allure.step(allure_title):
        try:
            assert actual_value is expected_bool, error_msg or f"Значение {actual_value} не {expected_bool}"
        except AssertionError:
            attach_response = {
                "Actual_value": str(actual_value),
                "Expected_bool": str(expected_bool)
            }
            _allure_attach_error(attach_response=attach_response, 
            error_name="Boolean comparison error")
            raise
    



def assert_not_in():
    pass