from os import major
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from python.scrape import concat_data

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/search", response_class=HTMLResponse)
async def search(request: Request):
    response = templates.TemplateResponse("search.html", {"request": request, 'result': result}) 
    return response

@app.post("/search", response_class=HTMLResponse)
async def search(request: Request, url: str = Form()):
    result = url
    table = concat_data(result)
    response = templates.TemplateResponse("search.html", {"request": request, 'result': table}) 
    return response

@app.get("/result", response_class=HTMLResponse)
async def result(request: Request):
    result = "paste a url"
    response = templates.TemplateResponse("result.html", {"request": request, 'result': result}) 
    return response