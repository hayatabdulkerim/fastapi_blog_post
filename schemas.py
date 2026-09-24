from datetime import datetime

from pydantic import (
    BaseModel,
    ConfigDict,
    EmailStr,
    Field,
)

# user schemas _____________________________________________________________________________

class UserBase(BaseModel):
    username: str = Field(min_length=1, max_length=50)
    email: EmailStr = Field(max_length=120)


class UserCreate(UserBase):
    password: str = Field(min_length=8)


class UserPublic(BaseModel):
    # this model is used in a response model which recives a user object from the db  but pydantic expencts a dictionary so this model config tells pydantic that this is an object and it can look the attributes to get the values needed for validation

    model_config = ConfigDict(from_attributes=True) 

    id: int
    username: str
    image_file: str | None
    image_path: str


class UserPrivate(UserPublic):
    email: EmailStr


class UserUpdate(BaseModel):
    username: str | None = Field(default=None, min_length=1, max_length=50)
    email: EmailStr | None = Field(default=None, max_length=120)
    image_file: str | None = Field(default=None, min_length=1, max_length=200)


# token schema _______________________________________________________________________________

class Token(BaseModel):
    access_token: str
    token_type: str



# post schema _______________________________________________________________________________


class PostBase(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    content: str = Field(min_length=1)


class PostCreate(PostBase):  # request model
    pass


class PostUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=100)
    content: str | None  = Field(default=None, min_length=1)


class PostResponse(PostBase):  # response model
    model_config = ConfigDict(
        from_attributes=True
    )

    id: int
    user_id: int
    date_posted: datetime
    author: UserPublic
