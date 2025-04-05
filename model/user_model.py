from pydantic import BaseModel # type: ignore

class UserModel(BaseModel):
    # id: int
    name: str
    email: str
    password: str
