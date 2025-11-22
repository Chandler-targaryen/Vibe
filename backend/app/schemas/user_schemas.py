from pydantic import BaseModel, EmailStr

class UserOut(BaseModel):
    id: int
    fullname: str
    email: EmailStr

    class Config:
        orm_mode = True