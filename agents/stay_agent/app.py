from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sys
import os

# FastAPI app
app = FastAPI()

class TravelRequest(BaseModel):
    origin: str
    destination: str
    start_date: str
    end_date: str
    budget: float

@app.post("/get_stays")
async def get_stays(request: TravelRequest):
    # Simulate stay search with ADK
    # In a real app, you would use the ADK agent to generate this content
    stays_info = f"**Accommodation Options in {request.destination}:**\n\n"
    stays_info += f"* **Luxury Hotel**\n"
    stays_info += f"  * Dates: {request.start_date} to {request.end_date}\n"
    stays_info += f"  * Price:  total\n"
    stays_info += f"  * Amenities: Pool, Spa, Restaurant\n\n"
    stays_info += f"* **Budget Friendly Option**\n"
    stays_info += f"  * Dates: {request.start_date} to {request.end_date}\n"
    stays_info += f"  * Price:  total\n"
    stays_info += f"  * Amenities: Free Breakfast, WiFi"
    
    return {"stay": stays_info}
