from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI()

class TravelRequest(BaseModel):
    origin: str
    destination: str
    start_date: str
    end_date: str
    budget: float

@app.post("/run")
async def plan_trip(request: TravelRequest):
    try:
        # Coordinate with other agents
        flight_response = requests.post("http://localhost:8001/get_flights", json=request.dict())
        stay_response = requests.post("http://localhost:8002/get_stays", json=request.dict())
        activities_response = requests.post("http://localhost:8003/get_activities", json=request.dict())
        
        if flight_response.ok and stay_response.ok and activities_response.ok:
            return {
                "flights": flight_response.json()["flights"],
                "stay": stay_response.json()["stay"],
                "activities": activities_response.json()["activities"]
            }
        else:
            if not flight_response.ok:
                raise HTTPException(status_code=500, detail=f"Flight agent error: {flight_response.text}")
            elif not stay_response.ok:
                raise HTTPException(status_code=500, detail=f"Stay agent error: {stay_response.text}")
            elif not activities_response.ok:
                raise HTTPException(status_code=500, detail=f"Activities agent error: {activities_response.text}")
    except requests.exceptions.ConnectionError as e:
        raise HTTPException(status_code=500, detail=f"Connection error: Make sure all agent services are running")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
