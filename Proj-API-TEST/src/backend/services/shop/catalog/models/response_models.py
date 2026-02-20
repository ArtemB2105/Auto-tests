from pydantic import BaseModel, ConfigDict, PositiveInt, PositiveFloat

class Rating(BaseModel):
    rate: PositiveFloat
    count: PositiveInt

class Good(BaseModel):
    model_config = ConfigDict(extra="ignore")
    id: PositiveInt
    title: str
    price: PositiveFloat
    rating: Rating