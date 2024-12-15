from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from utils.convert import convert

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/units/length", response_class=JSONResponse)
def listLengthUnits():
    return {"units": ["Meter", "Kilometer", "Centimeter", "Millimeter", "Micrometer", "Nanometer", "Mile", "Yard", "Foot", "Inch", "Light Year"]}

@app.get("/units/temperature", response_class=JSONResponse)
def listTemperatureUnits():
    return {"units": ["Celsius", "Fahrenheit", "Kelvin"]}

@app.get("/units/weight", response_class=JSONResponse)
def listWeightUnits():
    return {"units": ["Kilogram", "Gram", "Milligram", "Microgram", "Ton", "Pound", "Ounce", "Carat"]}

@app.get("/convert", response_class=JSONResponse)
def convert_units(value: float, input_unit: str, output_unit: str):
    return {"result": convert(value, input_unit, output_unit)}