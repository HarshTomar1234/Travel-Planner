from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class TravelRequest(BaseModel):
    origin: str
    destination: str
    start_date: str
    end_date: str
    budget: float

@app.post("/get_flights")
async def get_flights(request: TravelRequest):
    # Simulate flight search with ADK
    # In a real app, you would use the ADK agent to generate this content
    flights_info = f"**Flight Options:**\n\n"
    flights_info += f"* **Option 1**: {request.origin} to {request.destination}\n"
    flights_info += f"  * Date: {request.start_date}\n"
    flights_info += f"  * Price: \n"
    flights_info += f"  * Duration: 5 hours non-stop\n\n"
    flights_info += f"* **Option 2**: {request.origin} to {request.destination}\n"
    flights_info += f"  * Date: {request.start_date}\n"
    flights_info += f"  * Price: \n"
    flights_info += f"  * Duration: 7 hours with 1 connection"
    
    return {"flights": flights_info}
