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

class Person(BaseModel):
    first_name: str = Field(
        ..., 
        min_length=1,
        max_length=20,
        example="Gael"
        )
    last_name: str = Field(
        ..., 
        min_length=1,
        max_length=20,
        example="Ramos"
        )
    age: int = Field(
        ...,
        gt=0,
        le=100,
        example=18
    )
    hair_color: Optional[HairColor] = Field(default=None, example="black")
    is_married: Optional[bool] = Field(default=None, example=False)
    website: Optional[HttpUrl] = Field(default=None, example="https://www.esgaelramos.com")
    email: Optional[EmailStr] = Field(default=None, example="esgaelramos@gmail.com")
    heigth: Optional[PositiveFloat] = Field(default=None, example=1.68)

    # class Config:
    #     schema_extra = {
    #         "example": {
    #             "first_name": "Facundo",
    #             "last_name": "García",
    #             "age": 22,
    #             "hair_color": "blonde",
    #             "is_married": True,
    #             "web_site": "https://platzi.com/facundo",
    #             "email": "facundo@platzi.com",
    #             "heigth": "1.80"
    #         }
    #     }

class Location(BaseModel):
    city: str = Field(
        ...,
        min_length=3,
        max_length=30,
        example="Cuautitlán"
    )
    state: str = Field(
        ...,
        min_length=3,
        max_length=30,
        example="EdoMex"
    )
    country: str = Field(
        ...,
        min_length=3,
        max_length=30,
        example="México"
    )

    # class Config:
    #     schema_extra = {
    #         "example": {
    #             "city": "Buenos Aires",
    #             "state": "CABA",           
    #             "country": "Argentina"
    #         }
    #     }


@app.get("/")
def home():
    return{"Hello": "World"}

# Request and Response Body

@app.post("/person/new")
def create_person(person: Person = Body(...)):
    return person

# Validations: Query Parameters
@app.get("/person/detail")
def show_person(
    name: Optional[str] = Query(
        None, 
        min_length=1, 
        max_length=20,
        title="Person Name",
        description="This is the person name. It's between 1 and 50 characters.",
        example="Iran"
        ),
    age: str = Query(
        ...,
        title="Person Age",
        description="This is the person age. It's requeried.",     
        example=15
        )
):
    return {name: age}

# Validations: Path Parameters
@app.get("/person/detail/{person_id}")
def show_person(
    person_id: int = Path(
        ..., 
        gt=0,
        title="Person ID",
        description="It's requeried(path), greatest than zero.",
        example=17032007
        )
):
    return {person_id: "It exists!"}

# Validations: Request Body
# Test to commit?
@app.put("/person/{person_id}")
def update_person(
    person_id: int = Path(
        ...,
        title="Person ID",
        description="This the person ID, greatest than zero.",
        gt=0,
        example="17032007"
    ),
    person: Person = Body(...),
    location: Location = Body(...)
):
    results = person.dict()
    results.update(location.dict())
    return results
