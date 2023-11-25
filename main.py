from fastapi import FastAPI
from pydantic import BaseModel
from currency import excheng
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from authentication import get_user
from fastapi import HTTPException
from typing import Annotated
from authentication import get_current_user
from databace import Person
from sxems import Currency, Token
from authentication import create_accec_token

app = FastAPI()


@app.post('/randomno')
async def podrugomy(currency:Currency):
    result = excheng(currency.fram, currency.to, currency.amount)
    print(result)
    return result 


@app.post('/login', response_model=Token)
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = get_user(form_data.username)
    if form_data.password != user.password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    return {"access_token": create_accec_token({'sub': user.name}) , "token_type": "bearer"}


@app.get('/test')
async def test(current_user: Annotated[Person, Depends(get_current_user)]):
    return {'current_user': current_user}
