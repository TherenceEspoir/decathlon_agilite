from fastapi import Depends, FastAPI, Header, HTTPException
import src.decathlon.Controller.init_bdd
from fastapi import FastAPI, HTTPException
from fastapi.openapi.utils import get_openapi
from fastapi.middleware.cors import CORSMiddleware

import src.decathlon.Controller.health
from src.decathlon.Controller.user import get_user_by_id, post_user
from src.decathlon.Model.user import User, UserInput, UserResponse
from src.decathlon.Model.health import HealthDataInput, HealthData
from src.decathlon.Controller.health import health_data_by_user_id, get_health_history_data_by_user_id, post_health_data

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


@app.get("/users/{user_id}", tags=["user"], response_model=UserResponse, responses={
    200: {
        "model": UserResponse,
        "description": "Successfully retrieved user data",
        "content": {
            "application/json": {
                "example": {
                    "id": 1,
                    "name": "Jhon",
                    "mail": "jhon@gmail.com",
                    "birth_date": "1990-01-01"
                }
            }
        }
    },
    404: {
        "description": "User not found",
        "content": {
            "application/json": {
                "example": {
                    "detail": "User not found"
                }
            }
        }
    }
})
async def read_user(user_id: int):
    return get_user_by_id(user_id)

@app.post("/users/",tags=["user"], response_model=UserResponse, responses={
    200: {
        "model": UserResponse,
        "description": "Successfully retrieved user data",
        "content": {
            "application/json": {
                "example": {
                    "id": 1,
                    "name": "Jhon",
                    "mail": "jhon@gmail.com",
                    "birth_date": "1990-01-01"
                }
            }
        }
    }
})
async def create_user(user: UserInput):
    return post_user(user)

@app.get("/health_data/{user_id}",tags=["health_data"], response_model=HealthData, responses={
    200: {
        "model": HealthData,
        "description": "Successfully retrieved user data",
        "content": {
            "application/json": {
                "example": {
                    "id_user": 1,
                    "date": "2024-01-19T00:00:00",
                    "nombre_pas": 0,
                    "duree_sommeil": 0,
                    "u_duree_sommeil": 0,
                    "frequence_cardiaque": 0,
                    "u_frequence_cardiaque": 0,
                    "poids": 0,
                    "u_poids": 0,
                    "taille": 0,
                    "u_taille": 0
                }
            }
        }
    },
    404: {
        "description": "HealthData not found",
        "content": {
            "application/json": {
                "example": {
                    "detail": "Health data not found for the user"
                }
            }
        }
    }
})
async def read_health_data(user_id: int):
    return health_data_by_user_id(user_id)
    

@app.get("/UserHealthDataHistory/{user_id}",tags=["health_data"], response_model=HealthData, responses={
    200: {
        "model": HealthData,
        "description": "Successfully retrieved health data",
        "content": {
            "application/json": {
                "example": {
                    "id_user": 1,
                    "date": "2024-01-19T00:00:00",
                    "nombre_pas": 0,
                    "duree_sommeil": 0,
                    "u_duree_sommeil": 0,
                    "frequence_cardiaque": 0,
                    "u_frequence_cardiaque": 0,
                    "poids": 0,
                    "u_poids": 0,
                    "taille": 0,
                    "u_taille": 0
                }
            }
        }
    },
    404: {
        "description": "HealthData not found",
        "content": {
            "application/json": {
                "example": {
                    "detail": "Health data not found for the user"
                }
            }
        }
    }
})
async def read_health_data(
    user_id: int,
    start_date: str,
    end_date: str
    ):
    return get_health_history_data_by_user_id(user_id, start_date, end_date)


@app.post("/health_data/",tags=["health_data"], response_model=HealthData, responses={
    200: {
        "model": HealthData,
        "description": "Successfully retrieved health data",
        "content": {
            "application/json": {
                "example": {
                    "id_user": 1,
                    "date": "2024-01-19T00:00:00",
                    "nombre_pas": 0,
                    "duree_sommeil": 0,
                    "u_duree_sommeil": 0,
                    "frequence_cardiaque": 0,
                    "u_frequence_cardiaque": 0,
                    "poids": 0,
                    "u_poids": 0,
                    "taille": 0,
                    "u_taille": 0
                }
            }
        }
    }
})
async def create_or_update_health_data(health_data: HealthDataInput):
    return post_health_data(health_data)

