from fastapi import FastAPI

app = FastAPI()

fake_users = [{"id": 1, "role": "admin", "name": "Ivan"},
              {"id": 2, "role": "investor", "name": "Fedor"},
              {"id": 3, "role": "trader", "name": "Janna"}
              ]

@app.get('/users/{user_id}')
def get_user(user_id:int):
    return [user for user in fake_users if user.get('id')==user_id]

