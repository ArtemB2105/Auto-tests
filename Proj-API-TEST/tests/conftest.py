import allure
from config import TestConfig
from src.backend.clients.http.client import HTTPClient
import pytest
from faker import Faker
from src.backend.services.shop.auth.adapter import FakeApiAuthAdapter
from src.backend.services.shop.catalog.adapter import FakeApiCatalogAdapter
from src.backend.services.shop.catalog.service import FakeApiCatalogService


@allure.title("Инициализация фейкера")
@pytest.fixture(scope="session")
def faker() -> Faker:
    return Faker()



@allure.title("Инициализация http клиента")
@pytest.fixture
def htt_client():
    return HTTPClient(host=TestConfig.SHOP_BASE_URL)




@allure.title("Инициализация адаптера аутентификации для API")
@pytest.fixture
def fake_api_auth_adapter(htt_client) -> FakeApiAuthAdapter:
    return FakeApiAuthAdapter(http_client=htt_client)



@allure.title("Регистрация нового пользователя")
@pytest.fixture
def create_user(fake_api_auth_adapter, faker) -> dict[str, str]: # type: ignore
    username = faker.user_name()
    password = faker.password()
    email = faker.email()
    response = fake_api_auth_adapter.register(username=username, email=email, password=password)
    assert response.status_code == 201

    yield {"username":username, "password": password}

    fake_api_auth_adapter.delete_user(user_id=response.json()["id"])


@allure.title("Логин нового пользователя и инициализвация http клиента с аутентификацией")
@pytest.fixture
def http_client_with_auth(create_user, fake_api_auth_adapter) -> HTTPClient:
    token = fake_api_auth_adapter.login(username=create_user["username"], password=create_user["password"]).text
    return HTTPClient(host=TestConfig.SHOP_BASE_URL, default_headers={"Authorization": f"Bearer {token}"})



@allure.title("Инициализация адаптера каталогa для API без auth")
@pytest.fixture
def fake_api_catalog_adapter_no_auth(htt_client) -> FakeApiCatalogAdapter:
    return FakeApiCatalogAdapter(http_client=htt_client)


@allure.title("Инициализация адаптера каталогa для API с auth")
@pytest.fixture
def fake_api_catalog_adapter_with_auth(http_client_with_auth) -> FakeApiCatalogAdapter:
    return FakeApiCatalogAdapter(http_client=http_client_with_auth)



@allure.title("Инициализация сервиса каталога")
@pytest.fixture
def fake_api_catalog_service(fake_api_catalog_adapter_with_auth) -> FakeApiCatalogService:
    return FakeApiCatalogService(catalog_adapter=fake_api_catalog_adapter_with_auth)


