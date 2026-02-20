from src.backend.services.shop.catalog.models.response_models import Good
from src.backend.services.shop.catalog.adapter import FakeApiCatalogAdapter
from src.utils.validations.validations_REST_api import validate_response
from http import HTTPStatus


class FakeApiCatalogService:




    def __init__(self, catalog_adapter: FakeApiCatalogAdapter):
        self._catalog_adapter = catalog_adapter




    def get_catalog(self) -> list[Good]:
        response = self._catalog_adapter.get_catalog()
        validate_response(response=response, expected_status_code=HTTPStatus.OK)
        return [Good(**good) for good in response.json()]


if __name__ == "__main__":
    good = {
        "id": 1,
        "title": "Product 1",
        "price": 100,
        "rating": {
            "rate": 4.5,
            "count": 100
        }
    }
    good = Good(**good)
    print(model_good.price)
