import base64
import os
import json
import shutil

from fastapi import FastAPI, HTTPException, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from main import main
from calculator import calculate
import uvicorn

app = FastAPI(title="Equation Solver", description="Equation Solver API")

# Enable CORS (Cross-Origin Resource Sharing)
origins = ["*"]  # Replace with your front-end's URL(s)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ImageData(BaseModel):
    image: str

router = APIRouter()


app.include_router(router)


@app.get("/", include_in_schema=False)
async def index():
    return RedirectResponse(url="/docs")
    # A welcome message to test our server
    # return {"message": "Equations Solver"}


if __name__ == "__main__":
    host = os.getenv("API_URL", "http://localhost")
    uvicorn.run(app, host=host, port=8000, debug=True)