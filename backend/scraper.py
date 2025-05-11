import requests
from bs4 import BeautifulSoup

def scrape_events():
    # URL to scrape
    url = "https://www.eventbrite.com.au/d/australia--sydney/events/"

    # Send a GET request to fetch the page content
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)
    print(response)

    # Ensure we got a successful response
    if response.status_code != 200:
        print("Failed to retrieve the page")
        return []

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    events = []

    # Corrected indentation here
    for h3 in soup.find_all("h3", class_=lambda c: c and "event-card__clamp-line--two" in c):
        try:
            # Extract Title and URL
            title = h3.get_text(strip=True)
            parent_a = h3.find_parent("a")
            event_url = parent_a["href"] if parent_a and parent_a.has_attr("href") else "N/A"

            # Extract Time
            time_tag = h3.find_next("p", class_=lambda c: c and "Typography_body-md-bold" in c)
            time = time_tag.get_text(strip=True) if time_tag else "N/A"

            # Extract Venue
            venue_tag = h3.find_next("p", class_="event-card__clamp-line--one")
            venue = venue_tag.get_text(strip=True) if venue_tag else "N/A"

            # Extract Image URL
            img_tag = parent_a.find("img", class_=lambda c: c and "event-card-image" in c)
            img_link = img_tag["src"] if img_tag and img_tag.has_attr("src") else "N/A"

            # Append event with additional details
            events.append({
                "title": title,
                "time": time,
                "venue": venue,
                "image_link": img_link,
                "url": event_url
            })

        except Exception as e:
            print(f"Error parsing event: {e}")
            continue

    return events

# Run the scraper and print the events
events = scrape_events()

