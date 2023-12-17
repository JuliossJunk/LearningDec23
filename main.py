from fastapi import FastAPI, Request, status
from typing import List, Optional
from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum
from fastapi.exceptions import ResponseValidationError
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

app = FastAPI(title='MyImprovmentAppFirstLesson',
              description='I Will Be Better!'
              )


# Client will see same error message as server, delete for most situations
@app.exception_handler(ResponseValidationError)
async def validation_exception_handler(request: Request, exc: ResponseValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors()})
    )


# Data model of Trade class
class Trade(BaseModel):
    id: int
    user_id: int
    # Name of value must be concise
    currency: str = Field(max_length=5)
    side: str
    # price must be greater or equal to 0
    price: float = Field(ge=0)
    amount: float


class DegreeType(Enum):
    newbie = 'newbie'
    expert = 'expert'


class Degree(BaseModel):
    id: int = Field(ge=1)
    created: datetime
    type: DegreeType


class User(BaseModel):
    id: int = Field(ge=1)
    role: str
    name: str
    degree: Optional[List[Degree]] = []


fake_users = [{"id": 1, "role": "admin", "name": "Ivan"},
              {"id": 2, "role": "investor", "name": "Fedor"},
              {"id": 3, "role": "trader", "name": "Janna"},
              {"id": 4, "role": "investor", "name": "Auramathon3000", "degree": [
                  {'id': 1, "created": "2020-01-01T00:00:00", "type": "expert"}
              ]}
              ]

fake_trades = [
    {'id': 1, 'user_id': 1, 'currency': 'BTC', 'side': 'buy', 'price': 123, 'amount': 2.13},
    {'id': 2, 'user_id': 1, 'currency': 'BTC', 'side': 'sell', 'price': 130, 'amount': 2.13},
]


@app.get('/users/{user_id}', response_model=List[User])
def get_user(user_id: int):
    return [user for user in fake_users if user.get('id') == user_id]


@app.post('/trades')
def post_trade(trades: List[Trade]):
    fake_trades.extend(trades)
    return {'status': 200, 'data': fake_trades}
