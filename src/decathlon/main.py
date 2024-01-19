from fastapi import Depends, FastAPI, Header, HTTPException
import src.decathlon.Controller.init_bdd
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

import src.decathlon.Controller.health
from src.decathlon.Controller.user import get_user_by_id, post_user
from src.decathlon.Model.user import User, UserInput
from src.decathlon.Model.health import HealthDataInput
from src.decathlon.Controller.health import health_data_by_user_id, get_health_history_data_by_user_id, post_health_data
from fastapi.openapi.utils import get_openapi

from typing import Dict, Optional, Union


app = FastAPI()

def custom_openapi():
    if not app.openapi_schema:
        app.openapi_schema = get_openapi(
            title=app.title,
            version=app.version,
            openapi_version=app.openapi_version,
            description=app.description,
            terms_of_service=app.terms_of_service,
            contact=app.contact,
            license_info=app.license_info,
            routes=app.routes,
            tags=app.openapi_tags,
            servers=app.servers,
        )
        for _, method_item in app.openapi_schema.get('paths').items():
            for _, param in method_item.items():
                responses = param.get('responses')
                # remove 422 response, also can remove other status code
                if '422' in responses:
                    del responses['422']
    return app.openapi_schema

app.openapi = custom_openapi


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/users/{user_id}",tags=["user"])
async def read_user(user_id: int):
    return get_user_by_id(user_id)

@app.post("/users/",tags=["user"])
async def create_user(user: UserInput):
    return post_user(user)

@app.get("/health_data/{user_id}",tags=["health_data"])
async def read_health_data(user_id: int):
    return health_data_by_user_id(user_id)
    

@app.get("/UserHealthDataHistory/{user_id}",tags=["health_data"])
async def read_health_data(
    user_id: int,
    start_date: str,
    end_date: str
    ):
    return get_health_history_data_by_user_id(user_id, start_date, end_date)


@app.post("/health_data/",tags=["health_data"])
async def create_or_update_health_data(health_data: HealthDataInput):
    return post_health_data(health_data)

