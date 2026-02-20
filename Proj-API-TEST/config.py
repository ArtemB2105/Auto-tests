import os

class TestConfig:

    SHOP_BASE_URL = os.getenv("SHOP_BASE_URL", "https://fakestoreapi.com")
    