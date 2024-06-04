from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from Backend.database.database import Base
from Backend.database.database import engine
from Backend.database import models
from Backend.authentication import authentication
from Backend.routers import employee, admin, team, leave, arrival_departure, picture
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.include_router(admin.router)
app.include_router(team.router)
app.include_router(leave.router)
app.include_router(picture.router)
app.include_router(employee.router)
app.include_router(arrival_departure.router)
app.include_router(authentication.router)

Base.metadata.create_all(engine)

app.mount('/files', StaticFiles(directory='Backend/pictures'), name='files')


@app.get('/')
def first_api():
    return "Welcome to our human resource manager project"
