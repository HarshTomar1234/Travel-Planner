"""
Instead of writing a custom FastAPI route for each agent, we generalize it using the create_app(agent) function, which handles:

Serving the agent on /run
Receiving a travel request
Returning a structured response
"""

from fastapi import FastAPI
import uvicorn
def create_app(agent):
    app = FastAPI()
    @app.post("/run")
    async def run(payload: dict):
        return await agent.execute(payload)
    return app


"""
This utility creates a FastAPI app with a standard /run route that delegates execution to the provided agent.
It ensures a consistent agent-to-agent (A2A) interface for all services using structured JSON input.
"""
