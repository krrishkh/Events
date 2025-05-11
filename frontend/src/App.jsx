import { Routes, Route } from "react-router-dom";
import { useEffect, useState } from "react";
import EventCard from "./components/card";
import Email from "./components/email";
import Home from "./components/home";

function App() {
  const [events, setEvents] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8001")
      .then(res => res.json())
      .then(data => setEvents(data))
      .catch(err => console.error("Failed to fetch events", err));
  }, []);

  return (
    <Routes>
      <Route path="/" element={<Home events={events} />} />
      <Route path="/email" element={<Email />} />
    </Routes>
  );
}

export default App;
