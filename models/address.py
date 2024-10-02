from pydantic import BaseModel, Field


class Address(BaseModel):
    address_line: str = Field(..., title="Street", max_length=100)
    city: str = Field(..., title="City", max_length=50)
    state: str = Field(..., title="State", max_length=50)
    pincode: str = Field(..., title="Zip", max_length=10)
    country: str = Field(..., title="Country", max_length=50)


class AddressInput(BaseModel):
    address: str = Field(..., title="Address", max_length=2000)
