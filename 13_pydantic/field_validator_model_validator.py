from pydantic import BaseModel, field_validator, model_validator


class User(BaseModel):
    username: str
    age: int

    @field_validator("username")
    def username_len(cls, v):
        if len(v) < 4:
            raise ValueError("Name should be greate than 3 characters")
        return v


user = User(username="Saf", age=22)
print(user)


class SignUp(BaseModel):
    password: str
    confirm_pass: str

    @model_validator(mode='after')
    def check_pass(cls, values):
        if values.password != values.confirm_pass:
            raise ValueError("Password donot match")
        return values
