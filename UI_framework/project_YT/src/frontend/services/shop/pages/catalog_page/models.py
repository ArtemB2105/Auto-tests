from dataclasses import dataclass
import re

@dataclass
class Good:
    name: str
    description: str
    price: float

    @classmethod
    def from_string(cls, text: str) -> 'Good':
        """
        Парсит строку с товаром с SauceDemo и возвращает экземпляр Good.
        
        Пример строки:
        "Sauce Labs Backpackcarry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection.$29.99Add to cart"
        """
        # Паттерн для SauceDemo:
        # 1. Название начинается с "Sauce Labs" и идет до границы с описанием
        # 2. Описание — всё между названием и ценой
        # 3. Цена — число после $ до .99
        
        # Извлекаем название (до первого пробела перед описанием или до цены)
        name_match = re.search(r"^(Sauce Labs [A-Za-z\-]+(?:\s+[A-Za-z\-]+)?)", text)
        name = name_match.group(1).strip() if name_match else ""
        
        # Извлекаем описание (всё после названия и до символа $)
        desc_match = re.search(rf"{re.escape(name)}(.+?)\$", text)
        description = desc_match.group(1).strip() if desc_match else ""
        
        # Извлекаем цену (число с плавающей точкой после $)
        price_match = re.search(r"\$(\d+\.\d{2})", text)
        price = float(price_match.group(1)) if price_match else 0.0
        
        return cls(
            name=name,
            description=description,
            price=price
        )