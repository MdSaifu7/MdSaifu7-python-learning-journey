from pydantic import BaseModel, computed_field, Field


class Product(BaseModel):
    price: float
    quantity: int

    @computed_field
    @property
    def total_price(self) -> float:
        return self.price*self.quantity


p1 = Product(price=100, quantity=5)
print(p1.total_price)


class Booking(BaseModel):
    user_id: int
    room_id: int
    nights: int = Field(..., ge=1)
    rate_per_night: float

    @computed_field
    @property
    def total_bill(self) -> float:
        return self.nights*self.rate_per_night


b1 = Booking(user_id=10, room_id=15, nights=4, rate_per_night=500)
print(b1.model_dump())
