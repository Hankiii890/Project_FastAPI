from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy import select 
from databace import Person
from sqlalchemy.orm import Session 
from databace import engine
from typing import Annotated
from datetime import timedelta
from datetime import datetime
from jose import JWTError, jwt
from sxems import Token, TokenData


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_user(name: str):
    query = select(Person).where(Person.name == name) 
    with Session(engine) as session:
        result = session.execute(query)
        
        return result.one()[0]


def create_user(name: str, email: str, password: str):
    persen = Person(name=name, email=email, password=password)
    with Session(engine) as session:
        session.add(persen)
        session.commit()


async def get_current_user(Token: Annotated[str, Depends(oauth2_scheme)]):
    user = get_user(Token)
    return user 
    

SECRET_KEY = 'sdjsfjirji32434j25241j1j242ij'
ALGORITHM = "HS256"

def create_accec_token(data: dict):
    expire = datetime.utcnow() + timedelta(days=3)
    data.update({'exp': expire})
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(username=token_data.username)
    if user is None:
        raise credentials_exception
    return user