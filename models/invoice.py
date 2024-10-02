from typing import List

from pydantic import BaseModel, Field

from .address import Address
from .products import Products


class Invoice(BaseModel):
    invoice_date: str = Field(..., title="Invoice Date", max_length=50)
    invoice_number: str = Field(..., title="Invoice Number", max_length=50)
    products: List[Products]
    total: float = Field(..., title="Total", ge=0)
    shipping_address: Address
    billing_address: Address
    terms: str = Field(..., title="Terms", max_length=500)
    notes: str = Field(..., title="Notes", max_length=500)
