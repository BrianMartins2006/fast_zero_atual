from http import HTTPStatus

from fastapi import FastAPI

from fast_sero.routers import auth, users
from fast_sero.schemas import Message

app = FastAPI()
app.include_router(users.rounter)
app.include_router(auth.rounter)


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}
