from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class TravelRequest(BaseModel):
    origin: str
    destination: str
    start_date: str
    end_date: str
    budget: float

@app.post("/get_activities")
async def get_activities(request: TravelRequest):
    # Simulate activities search with ADK
    # In a real app, you would use the ADK agent to generate this content
    activities_info = f"**Top Activities in {request.destination}:**\n\n"
    activities_info += f"* **City Tour**\n"
    activities_info += f"  * Duration: 3 hours\n"
    activities_info += f"  * Price: \n"
    activities_info += f"  * Highlights: Historical sites, local cuisine\n\n"
    activities_info += f"* **Museum Pass**\n"
    activities_info += f"  * Duration: Full day access\n"
    activities_info += f"  * Price: \n"
    activities_info += f"  * Includes: Access to 5 popular museums\n\n"
    activities_info += f"* **Evening Entertainment**\n"
    activities_info += f"  * Duration: 2 hours\n"
    activities_info += f"  * Price: \n"
    activities_info += f"  * Type: Local cultural performance"
    
    return {"activities": activities_info}
