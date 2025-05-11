from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db import get_events
from pydantic import BaseModel

app = FastAPI()

# Allow frontend to access this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with frontend origin in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def list_events():
    events = get_events()
    print("Fetched events:", events)
    return events


@app.get("/ping")
def ping():
    return {"message": "pong"}

class EmailRequest(BaseModel):
    email: str
    eventName: str

@app.post("/submit-email")
def collect_email(data: EmailRequest):
    print(f"Email collected: {data.email} for event: {data.eventName}")
    # Save to database or send to Mailchimp etc.
    return {"status": "success"}

