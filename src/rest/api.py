from fastapi import FastAPI, HTTPException
from src.rest.controller import Controller
from src.data_model.answer import Answer
from src.data_model.question import Question

controller = Controller()
app = FastAPI()

@app.get("/")
def read_root():
    return {"Health": "OK"}

@app.post("/chat",response_model=Answer)
def chat(req: Question):
    return controller.chat(req)