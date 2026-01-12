from pydantic import BaseModel, Field


class User(BaseModel):
    name: str = Field(
        ...,
        min_length=3,
        max_length=100
    )
    email: str = Field(
        ...,
        min_length=3,
        max_length=80
    )
    age: int = Field(
        ...,
        gt=0,
        le=100,
        description="Age in years"
    )
    salary: float = Field(
        ...,
        ge=10000,
        le=2000000,
        description="Salary of the user"
    )


user_data = {
    "name": "MD.SAIF",
    "email": "Saif@gmail.com",
    "age": 22,
    "salary": 1200000
}
user = User(**user_data)
print(user)
