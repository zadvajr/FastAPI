"""This is how to implement CORS - Cross Origin Resource Sharing (CORSMiddleware in FastAPI)"""
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

app = FastAPI()

origins = [
    "http://localhost:3000",
    "https://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

@app.get("/")
async def read_root():
    """This is the root path"""
    return {"message": "Hellow CORS Middleware!"}

