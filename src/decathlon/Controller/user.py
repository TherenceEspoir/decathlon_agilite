
from fastapi import Depends, FastAPI, Header, HTTPException
from src.decathlon.Controller.init_bdd import conn, cursor
from src.decathlon.Model.user import User, UserInput
# from src.decathlon.main import app

from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_user_by_id(user_id: int):
    cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))
    user_data = cursor.fetchone()

    if user_data is None:
        raise HTTPException(status_code=404, detail="User not found")

    user = User(
        id=user_data[0],
        name=user_data[1],
        mail=user_data[2],
        password=user_data[3],
        birth_date=user_data[4]
    )

    return user

def post_user(userInput:UserInput):
    try:
        cursor.execute("INSERT INTO users (name, mail, password, birth_date) VALUES (?, ?, ?, ?)",
                       (userInput.name, userInput.mail, userInput.password, userInput.birth_date))
        conn.commit()

        user_id = cursor.lastrowid

        user = User(
            id=user_id,
            name=userInput.name,
            mail=userInput.mail,
            password=userInput.password,
            birth_date=userInput.birth_date
        )

        return user
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating user: {str(e)}")