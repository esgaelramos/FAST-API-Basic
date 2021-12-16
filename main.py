# Python
#Las anteriores no sé por qué aparecen
from typing import Optional
from enum import Enum

# Pydantic
from pydantic import BaseModel
from pydantic import Field
from pydantic import EmailStr
from pydantic import PositiveFloat
from pydantic import HttpUrl

# FastAPI
from fastapi import FastAPI
from fastapi import Body
from fastapi import Query
from fastapi import Path

app = FastAPI()

#Models

class HairColor(Enum):
    white = "white"
    brown = "brown"
    black = "black"
    blonde = "blonde"
    red = "red"

class EmailStr(EmailStr):
    pass
class PositiveFloat(PositiveFloat):
    pass
class HttpUrl(HttpUrl):
    pass
