from pydantic import BaseModel, EmailStr


class ToDoCreate(BaseModel):
    title: str
    description: str


class ToDoUpdate(BaseModel):
    title: str
    description: str
    completed: bool


class ToDoResponse(BaseModel):
    id: int
    title: str
    description: str
    completed: bool

    class Config:
        from_attributes = True  # Enable ORM mode for ToDoResponse


# User Schemas
class UserCreate(BaseModel):

    username: str
    email: EmailStr
    password: str


class UserLogin(BaseModel):

    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr



    class Config:
        from_attributes = True  # Enable ORM mode for UserResponse
