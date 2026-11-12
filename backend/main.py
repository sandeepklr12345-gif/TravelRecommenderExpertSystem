from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Allow requests from frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Input model
class UserInput(BaseModel):
    budget: str
    climate: str
    place_type: str

# Rule-based recommendation logic
@app.post("/recommend")
def recommend(input: UserInput):
    rules = {
        ('low', 'hot', 'beach'): "Goa, India",
        ('medium', 'moderate', 'mountain'): "Manali, India",
        ('high', 'cold', 'historical'): "Prague, Czech Republic",
        ('low', 'cold', 'wildlife'): "Jim Corbett National Park, India",
        ('medium', 'hot', 'historical'): "Hampi, India",
        ('high', 'moderate', 'beach'): "Bali, Indonesia",
        ('low', 'moderate', 'beach'): "Pondicherry, India",
        ('medium', 'cold', 'mountain'): "Shimla, India"
    }

    destination = rules.get(
        (input.budget, input.climate, input.place_type),
        "No match found. Try different options!"
    )
    return {"destination": destination}
