from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    username: str
    age: int
    email: EmailStr
    phone_number: int