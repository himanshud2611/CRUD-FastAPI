from pydantic import BaseModel

# schema
class User(BaseModel):
    name: str
    email: str
    password: str

