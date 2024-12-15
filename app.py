from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from utils import unit_management

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/units/length", response_class=JSONResponse)
def listLengthUnits():
    return unit_management.listLengthUnits()

@app.get("/units/temperature", response_class=JSONResponse)
def listTemperatureUnits():
    return unit_management.listTemperatureUnits()

@app.get("/units/weight", response_class=JSONResponse)
def listWeightUnits():
    return unit_management.listWeightUnits()

@app.get("/units/speed", response_class=JSONResponse)
def listSpeedUnits():
    return unit_management.listSpeedUnits()

@app.get("/units/volume", response_class=JSONResponse)
def listVolumeUnits():
    return unit_management.listVolumeUnits()

@app.get("/units/area", response_class=JSONResponse)
def listAreaUnits():
    return unit_management.listAreaUnits()

@app.get("/units/time", response_class=JSONResponse)
def listTimeUnits():
    return unit_management.listTimeUnits()

@app.get("/units/digitalstorage", response_class=JSONResponse)
def listDigitalStorageUnits():
    return unit_management.listDigitalStorageUnits()

@app.get("/convert", response_class=JSONResponse)
def convert_units(value: float, input_unit: str, output_unit: str):
    return {"result": unit_management.convert(value, input_unit, output_unit)}