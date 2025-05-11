from fastapi import APIRouter, Request
from pydantic import BaseModel
from app.agent_service import AgentService

router = APIRouter()
agent_service = AgentService()

class AgentRequest(BaseModel):
    prompt: str

@router.post("/agent")
def run_agent(request: AgentRequest):
    return agent_service.run_agent(request.prompt)
