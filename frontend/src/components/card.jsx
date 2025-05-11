import { useNavigate } from "react-router-dom";

const EventCard = ({ event }) => {
  const navigate = useNavigate();

  const handleGetTickets = () => {
    navigate("/email", {
      state: {
        eventName: event.title,
        redirectUrl: event.url,
      },
    });
  };

  return (

    <div className="bg-white rounded-2xl shadow-md overflow-hidden max-w-sm transition-transform transform hover:scale-105">
      {event.image_link !== "N/A" && (
        <img
          src={event.image_link}
          alt={event.title}
          className="w-full h-48 object-cover"
        />
      )}

      <div className="p-4">
        <h3 className="text-lg font-semibold text-gray-900 leading-tight">
          {event.title}
        </h3>

        <p className="text-sm text-red-600 font-medium mt-1">
          {event.time !== "N/A" ? event.time : "Time not available"}
        </p>

        <p className="text-sm text-gray-600 mt-1">
          {event.venue !== "N/A" ? event.venue : "Venue not specified"}
        </p>

        <button
          onClick={handleGetTickets}
          className="mt-4 w-full bg-orange-500 hover:bg-orange-600 text-white font-medium py-2 px-4 rounded-lg transition"
        >
          Get Tickets
        </button>
      </div>
    </div>
  );
};

export default EventCard;
