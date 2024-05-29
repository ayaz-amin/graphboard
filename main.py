import os
import base64
from io import BytesIO
from matplotlib.figure import Figure

from pydantic import BaseModel
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

class SequenceData(BaseModel):
    x: int
    y: int

gdata = [1, 2]

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
  global gdata
  fig = Figure()
  ax = fig.subplots()
  ax.plot(gdata)
  buf = BytesIO()
  fig.savefig(buf, format="svg")
  data = base64.b64encode(buf.getbuffer()).decode("ascii")
  return templates.TemplateResponse(
    "home.html", {"request": request, "data": data}
  )

@app.post("/end")
async def upload_data(data: SequenceData):
  gdata.append(data.x)

if __name__ == "__main__":
  import uvicorn
  uvicorn.run(app)