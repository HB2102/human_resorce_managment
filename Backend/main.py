from fastapi import FastAPI

app = FastAPI()





@app.get('/')
def first_api():
    return "Welcome to our human resorce manager project"