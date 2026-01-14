from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import List


class Address(BaseModel):
    city: str
    street: str
    zip_code: str


class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    address: Address
    createdAt: datetime
    tags: List[str] = []
    model_config = ConfigDict(
        json_encoders={
            datetime: lambda v: v.strftime('%d-%m-%Y %H:%M:%S')
        }
    )


address = Address(city="Muz", street="Chandkothi", zip_code="842002")

user = User(
    id=1,
    name="Saif",
    email="Saif@Ai",
    is_active=False,
    address=address,
    createdAt=datetime(2024, 3, 15, 14, 30),
    tags=["Premium", "subscriber"],

)

py_dict = user.model_dump()
py_json = user.model_dump_json()
# print(py_dict)
print(py_json)
