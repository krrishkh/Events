from apscheduler.schedulers.background import BackgroundScheduler
from scraper import scrape_events

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(scrape_events, 'interval', hours=1)
    scheduler.start()
