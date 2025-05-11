from pydantic import BaseModel

class TravelRequest(BaseModel):
    destination: str
    start_date: str
    end_date: str
    budget: float

"""
Before we can build intelligent agents, we need to define a common language for them to talk to each other. In our setup, this is done using:

A shared schema for input (defined via Pydantic)
A REST client utility to call agents
A REST server wrapper to standardize the /run endpoint across all agents

This class helps in:

Keeping input consistent for all agents.
Adding automatic validation with FastAPI.

"""