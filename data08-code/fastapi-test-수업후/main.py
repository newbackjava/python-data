from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from ai import ai_run

app = FastAPI()
# templates 폴더 지정
templates = Jinja2Templates(directory="templates")

@app.get("/")
def ai_html(request : Request):
    return templates.TemplateResponse("ai.html", {"request": request})

@app.get("/ai/{reply}") #/ai/짱이야!
def read_ai(reply : str):
    print("서버가 받은 댓글은 ", reply)
    # ai처리한 결과를 json을 응답할 예정
    result = ai_run(reply)
    return {"result" : result}
#{title:dksl, poster_url :dddkdkk}
#{{"result" : {title:dksl, poster_url :dddkdkk}}
