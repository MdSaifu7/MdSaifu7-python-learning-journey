from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    is_active: bool


input_data = {
    "id": 2,
    "name": "Md.Saif",
    "is_active": True
}

user = User(id="3", name="Nida", is_active=True)
print(user)
