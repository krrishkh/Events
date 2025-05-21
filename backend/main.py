from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db import get_events
from pydantic import BaseModel
from scheduler import start_scheduler
from db import init_db, save_events
from scraper import scrape_events
import uvicorn

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


@app.on_event("startup")
def startup_event():
    init_db()
    events = scrape_events()
    if events:
        save_events(events)
        print(f"{len(events)} events scraped and saved.")
    start_scheduler()



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

