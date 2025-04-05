from pydantic import BaseModel # type: ignore

class LogInRequest(BaseModel):
    email: str
    password: str

class RegisterRequest(BaseModel):
    name: str
    email: str
    password: str
