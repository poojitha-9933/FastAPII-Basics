from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, Field

app = FastAPI()

class User(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=20)

@app.post("/register")
def register(user: User):
    return {
        "message": "User registered successfully",
        "email": user.email
    }