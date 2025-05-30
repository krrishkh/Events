# Event Explorer

A web application to explore and get tickets for upcoming events.

## ✨ Features

- Browse and view curated events
- Submit your email to get redirected to ticket booking pages
- Responsive UI with a clean, modern design
- Fast loading and dynamic routing

## 🖥 Frontend

Built with **React** and styled using **Tailwind CSS** and **Flowbite** for clean UI components.

### Pages:

- **Home**: Lists all available events
  ![image](https://github.com/user-attachments/assets/7f07b351-23ce-4bbb-b6e3-804f8a7969a8)

- **Email**: Collects email before redirecting to the actual event page
  ![image](https://github.com/user-attachments/assets/a07a34b8-4b00-4a79-a5fb-ae3b958385f8)

- **Example original site** : sample original site to get tickets
  ![image](https://github.com/user-attachments/assets/a3228f40-d661-499c-9e7f-db45d1dbdb5e)


## 🚀 Backend

Developed using **Python** and **FastAPI**.

### Key Features:

- Extracts event data using **BeautifulSoup**
- Stores data in a lightweight **SQLite** database
- Provides REST API endpoints for frontend interaction

## 📦 Setup Instructions

### Backend

1. Navigate to the backend directory:
   ```bash
   cd backend
   
2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows

3. Install dependencies:
   ```
   pip install fastapi uvicorn beautifulsoup4 requests

4. Run the server:
   ```
   python run.py


### Frontend:
1. Navigate to the frontend directory:
   ```
   cd frontend
   
2. Install dependencies:
   ```
   npm install

3. Start the development server:
   ```
   npm run dev


### 🔗 API Endpoints

GET /events: Fetches all event data

POST /submit-email: Accepts user email and event name


### 📂 Database

Uses SQLite (events.db)

Stores event title, time, venue, image link, and URL
