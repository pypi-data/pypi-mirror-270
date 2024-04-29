from typing import Literal
from pydantic import BaseModel


class Product(BaseModel):
    """A product with the urls
    The shop names have to be filled with urls
    """

    name: str
    category: str = ""
    alternate: str = ""
    berrybase: str = ""
    welectron: str = ""
    botland: str = ""
    rossmann: str = ""
    aldi_sued: str = ""
    lidl: str = ""
    skandic: str = ""
    struck: str = ""
    ikea: str = ""


class ShopResponse(BaseModel):
    """Response model with availability
    This is the response model.
    It contains the price (which also can be none), and the availability (which also just can be none).
    """

    price: float = None
    available: Literal["yes", "delayed", "no", "only-in-store", "None"] = None
