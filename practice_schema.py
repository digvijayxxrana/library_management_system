from pydantic import BaseModel,Field,EmailStr
from typing import Annotated,Union,Literal



class CreditCardRequest(BaseModel):
    choice: Literal["credit card"] = "credit card"
    card_number: str = Field(min_length=4,max_length=16)
    expiry: str = Field(min_length=2)
    amount: int = Field(gt=0)
    currency: str = Field(min_length=2)

class PaypalRequest(BaseModel):
    choice: Literal["paypal"] = "paypal"
    email:EmailStr = Field(min_length=2)
    token: str = Field(min_length=2)
    amount: int = Field(gt=0)
    currency: str = Field(min_length=2)

PaymentRequest = Annotated[Union[CreditCardRequest,PaypalRequest],Field(discriminator="choice")]
