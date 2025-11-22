from pydantic import BaseModel, EmailStr

class SignupSchema(BaseModel):
    fullname: str
    email: EmailStr
    password: str

class LoginSchema(BaseModel):
    email: EmailStr
    password: str

class ForgotPasswordSchema(BaseModel):
    email: EmailStr