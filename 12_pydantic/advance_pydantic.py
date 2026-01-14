from pydantic import BaseModel, field_validator


class User(BaseModel):
    f_name: str
    l_name: str

    @field_validator("f_name", "l_name")
    def names_must_be_capitaliuzed(cls, v):
        if not v.istitle():
            raise ValueError("Names must be capitalized")
        return v


class Person(BaseModel):
    email: str
    age: 20

    @field_validator("email")
    def normalize_email(cls, v):
        return v.lower()


class Product():
    price: str

    @field_validator("price", mode="before")
    def parse_price(cls, v):
        if isinstance(v, str):
            return float(v.replace("$", "").replace(",", ""))
        return v
