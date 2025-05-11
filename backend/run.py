from main import app
from scheduler import start_scheduler
from db import init_db, save_events
from scraper import scrape_events
import uvicorn

if __name__ == "__main__":
    # Step 1: Initialize database
    init_db()
    
    # Step 2: Scrape events and save them to DB
    events = scrape_events()
    if events:
        save_events(events)
        print(f"{len(events)} events scraped and saved.")
    else:
        print("No events found during initial scrape.")
    
    # Step 3: Start scheduled scraping (background)
    start_scheduler()
    
    # Step 4: Launch the FastAPI server
    uvicorn.run(app, host="0.0.0.0", port=8001)
