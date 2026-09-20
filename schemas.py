from datetime import datetime

from pydantic import (  # we use Field to add constraints to schema fields
    BaseModel,
    ConfigDict,
    EmailStr,
    Field,
)


class UserBase(BaseModel):
    username: str = Field(min_length=1, max_length=50)
    email: EmailStr = Field(max_length=120)


class UserCreate(UserBase):
    pass
    # firstname: str = Field(min_length=1, max_length=50)
    # lastname: str = Field(min_length=1, max_length=50)


class UserResponse(UserBase):
    id: int
    image_file: str | None
    image_path: str

class UserUpdate(BaseModel):
    username: str | None = Field(default=None, min_length=1, max_length=50)
    email: EmailStr | None = Field(default=None, max_length=120)
    image_file: str | None = Field(default=None, min_length=1, max_length=200)

class PostBase(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    content: str = Field(min_length=1)


class PostCreate(PostBase):  # request model
    user_id: int  # temporary we will be getting the user id from the current session when we add authentication


class PostUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=100)
    content: str | None  = Field(default=None, min_length=1)


class PostResponse(PostBase):  # response model
    model_config = ConfigDict(
        from_attributes=True
    )  # for pydantic to be able to access attributes for data coming from databases

    id: int
    user_id: int
    date_posted: datetime
    author: UserResponse
