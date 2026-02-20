import os





class UIConfig:
    PLAYWRIGHT_WAIT_TIMEOUT = 3000






class TestConfig:
    SHOP_BASE_URL = os.getenv("SHOP_BASE_URL", "https://www.saucedemo.com/")

    UI_Config = UIConfig


