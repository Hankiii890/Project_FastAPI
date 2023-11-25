from pydantic import BaseModel

class Currency(BaseModel):
    fram: str
    to: str 
    amount: int

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None