from typing import AsyncGenerator, List
from agno.agent import Agent
from agno.models.anthropic import Claude
from agno.tools.yfinance import YFinanceTools
from agno.utils.pprint import pprint_run_response

class AgentService:
    def __init__(self):
        self.agent = Agent(
            model=Claude(id="claude-3-7-sonnet-latest"),
            tools=[YFinanceTools(stock_price=True)],
            markdown=True,
        )
    
    def run_agent(self, prompt: str):
        response = self.agent.run(prompt)
        return response.content
        