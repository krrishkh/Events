import EventCard from "./card";
import { HiMapPin } from "react-icons/hi2";

function Home({ events }) {
  return (
    <div className="min-h-screen bg-gray-50">
      {/* Hero Section */}
      <div className="bg-white rounded-b-3xl shadow-md py-12 px-6 sm:px-16 text-center">
        <h1 className="text-4xl sm:text-5xl font-bold text-gray-900 mb-4">
          Best events in <span className="text-blue-600">Your City</span>
        </h1>
        <p className="text-gray-600 max-w-2xl mx-auto text-base sm:text-lg">
          Looking for something to do nearby? Whether you're a local, new in town, or just exploring — we’ve got tons of events. Let’s find something exciting!
        </p>

        {/* Location Button (Placeholder for future dropdown/filter) */}
        <div className="mt-6 flex justify-center">
          <button className="flex items-center gap-2 bg-blue-100 text-blue-700 px-4 py-2 rounded-full shadow-sm text-sm font-medium hover:bg-blue-200 transition">
            <HiMapPin className="w-4 h-4" />
            Sydney, Australia
            <svg
              className="w-4 h-4 text-blue-600"
              fill="none"
              stroke="currentColor"
              strokeWidth={2}
              viewBox="0 0 24 24"
            >
              <path strokeLinecap="round" strokeLinejoin="round" d="M19 9l-7 7-7-7" />
            </svg>
          </button>
        </div>
      </div>

      {/* Events Section */}
      <div className="max-w-7xl mx-auto px-6 sm:px-12 mt-12">
        <h2 className="text-2xl font-semibold text-gray-800 mb-6 text-center">
          Discover Upcoming Events
        </h2>

        {events.length === 0 ? (
          <p className="text-center text-gray-500 text-lg mt-20">
            No events available right now. Check back later!
          </p>
        ) : (
          <div className="grid gap-8 grid-cols-1 sm:grid-cols-2 lg:grid-cols-3">
            {events.map((event, index) => (
              <EventCard key={index} event={event} />
            ))}
          </div>
        )}
      </div>
    </div>
  );
}

export default Home;
