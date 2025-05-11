import sqlite3
from typing import List, Dict

DB_NAME = "events.db"

def init_db():
    """Initializes the database and creates the events and emails tables if they don't exist."""
    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        
        # Create events table
        c.execute('''
            CREATE TABLE IF NOT EXISTS events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                time TEXT,
                venue TEXT,
                image_link TEXT,
                url TEXT
            )
        ''')
        
        # Create emails table
        c.execute('''
            CREATE TABLE IF NOT EXISTS emails (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT NOT NULL,
                event_title TEXT,
                submitted_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        conn.commit()



def save_events(events: List[Dict[str, str]]):
    """
    Saves a list of event dictionaries into the database.
    Old events are cleared before inserting new ones.
    """
    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        c.execute("DELETE FROM events")  # Clear old events
        for event in events:
            c.execute("""
                INSERT INTO events (title, time, venue, image_link, url)
                VALUES (?, ?, ?, ?, ?)
            """, (
                event.get('title', 'N/A'),
                event.get('time', 'N/A'),
                event.get('venue', 'N/A'),
                event.get('image_link', 'N/A'),
                event.get('url', 'N/A')
            ))
        conn.commit()
        print(f"{len(events)} events saved to database.")


def get_events() -> List[Dict[str, str]]:
    """
    Retrieves all events from the database.
    Returns:
        A list of dictionaries, each representing an event.
    """
    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        c.execute("SELECT title, time, venue, image_link, url FROM events")
        rows = c.fetchall()
        return [
            {
                "title": row[0],
                "time": row[1],
                "venue": row[2],
                "image_link": row[3],
                "url": row[4]
            }
            for row in rows
        ]


def save_email(email: str, event_title: str):
    """
    Saves a submitted email with the associated event title.
    """
    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        c.execute('''
            INSERT INTO emails (email, event_title)
            VALUES (?, ?)
        ''', (email, event_title))
        conn.commit()
        print(f"Email '{email}' saved for event '{event_title}'.")
