



from enum import StrEnum
from typing import Optional

import allure
from requests import Response

from src.backend.clients.http.client import HTTPClient


class Route(StrEnum):
    PRODUCTS = "products"


class FakeApiCatalogAdapter:



    def __init__(self,http_client: HTTPClient, route: Route = Route):
        self._http_client = http_client
        self._route = route


    @allure.step("Отправка запроса на получение каталога")
    def get_catalog(self) -> Response:
        return self._http_client.get(route=self._route.PRODUCTS)
    

    @allure.step("Отправка запроса на добавление продукта в каталог")
    def add_product(self, title: Optional[str] = None, price: Optional[int | float] = None, 
                    description: Optional[str] = None, category: Optional[str] = None) -> Response:
        product_data={}
        if title is not None:
            product_data["title"] = title
        if price is not None:
            product_data["price"] = price
        if description is not None:
            product_data["description"] = description
        if category is not None:
            product_data["category"] = category


        return self._http_client.post(route=self._route.PRODUCTS, json=product_data)