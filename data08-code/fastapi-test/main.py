from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

import ai

app = FastAPI()
# templates 폴더 지정
templates = Jinja2Templates(directory="templates")

@app.get("/")
def ai_html(request: Request):
    return templates.TemplateResponse("ai.html", {"request": request})


@app.get("/ai/{reply}")
def read_ai(reply : str):
    result = ai.ai_run(reply)
    return {"result" : result}