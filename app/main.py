from fastapi import FastAPI
from app.routes import hello, run_agent

app = FastAPI()

# Include the hello router
app.include_router(hello.router)
# Include the agent router
app.include_router(run_agent.router)
