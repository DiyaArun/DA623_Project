from fastapi import FastAPI, UploadFile, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

from .barcode_utils import detect_barcode, lookup_barcode, df
from .search_utils import search_products

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/upload", response_class=HTMLResponse)
async def upload(request: Request, file: UploadFile):
    contents = await file.read()
    code = detect_barcode(contents)
    product = lookup_barcode(code) if code else None
    return templates.TemplateResponse("result.html", {"request": request, "product": product, "code": code})

@app.post("/search", response_class=HTMLResponse)
async def search(request: Request, query: str = Form(...)):
    results = search_products(df, query)
    return templates.TemplateResponse("result.html", {"request": request, "results": results, "query": query})
