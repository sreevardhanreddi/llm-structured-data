from pydantic import BaseModel, Field


class Products(BaseModel):
    name: str = Field(..., title="Product Name", max_length=100)
    description: str = Field(..., title="Description", max_length=500)
    quantity: int = Field(..., title="Quantity", ge=0)
    price: float = Field(..., title="Price", ge=0)
    total: float = Field(..., title="Total", ge=0)
