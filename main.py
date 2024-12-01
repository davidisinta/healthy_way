# to run --bash: fastapi dev main.py

#standard libraries
import os

#third party libraries
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from langgraph.graph import START, StateGraph

#project libraries
from chatbot.chatbot import chatbot_compile

app = FastAPI()

graph = chatbot_compile();

class Message(BaseModel):
    text: str

# Determine the absolute paths to the static and templates directories
base_dir = os.path.dirname(os.path.abspath(__file__))
static_dir = os.path.join(base_dir, "static")
templates_dir = os.path.join(base_dir, "templates")

# Use the absolute path for the static directory
app.mount("/static", StaticFiles(directory=static_dir), name="static")

# Use the absolute path for the templates directory
templates = Jinja2Templates(directory=templates_dir)

@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse(request, "index.html", {"request": request})

@app.get("/demo/chat")
async def demo_chat(request: Request):
    return templates.TemplateResponse(request, "chat.html", {"request": request})

@app.post("/v1/chat")
async def send_message(message: Message):
    response = graph.invoke({"question": message.text})
    return {"message": response["answer"]}


