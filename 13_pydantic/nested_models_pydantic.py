from pydantic import BaseModel


class Address(BaseModel):
    city: str
    street: str


address = Address(city="Muzaffar Pur", street="Chand Kothi")


class User(BaseModel):
    name: str
    age: int
    address: Address


user = User(name="Saif", age=22, address=address)

# print(user)

user_data = {
    "name": "Rehan Ali",
    "age": 20,
    "address": {
        "city": "Thawe",
        "street": "Paya gali"
    }
}

user2 = User(**user_data)
print(user2)
