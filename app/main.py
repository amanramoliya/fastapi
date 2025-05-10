from fastapi import FastAPI
from app.routes import hello

app = FastAPI()

# Include the hello router
app.include_router(hello.router)
