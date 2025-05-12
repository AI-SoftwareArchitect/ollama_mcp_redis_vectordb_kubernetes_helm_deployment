from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from agent_commander import generate_command
from agent_coder import generate_code_with_ollama

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def serve_ui():
    with open("static/index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.post("/command")
async def command_handler(request: Request):
    data = await request.json()
    user_input = data.get("input")

    prompt = generate_command(user_input)
    code = generate_code_with_ollama(prompt)

    return {"generated_code": code}

@app.post("/agent-coder")
async def coder(request: Request):
    data = await request.json()
    prompt = data.get("prompt", "")
    return {"code": generate_code(prompt)}
