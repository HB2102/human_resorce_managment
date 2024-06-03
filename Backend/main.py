from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from Backend.database.database import Base
from Backend.database.database import engine
from Backend.database import models
from Backend.authentication import authentication
from Backend.routers import employee, admin, team

app = FastAPI()
app.include_router(admin.router)
app.include_router(team.router)
app.include_router(employee.router)
app.include_router(authentication.router)

Base.metadata.create_all(engine)


@app.get('/')
def first_api():
    return "Welcome to our human resorce manager project"