from fastapi import *

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/contacts")
def read_contacts():
    return [{"name": "John", "age": 30}, {"name": "Jane", "age": 29}]

@app.get("/about")
def read_contacts():
    return [{"name": "John", "age": 30}, {"name": "Jane", "age": 29}]