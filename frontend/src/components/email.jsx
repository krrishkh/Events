import { useState } from "react";
import { useLocation } from "react-router-dom";

const Email = () => {
  const { state } = useLocation();
  const [email, setEmail] = useState("");

  if (!state) {
    return (
      <p className="text-center mt-10 text-red-500">
        Invalid event data. Please go back and try again.
      </p>
    );
  }

  const { eventName, redirectUrl } = state;

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const res = await fetch("http://localhost:8001/submit-email", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, eventName }),
      });

      if (!res.ok) throw new Error("Failed to submit email.");

      // Redirect after success
      window.location.href = redirectUrl;
    } catch (err) {
      console.error(err);
      alert("Submission failed. Please try again.");
    }
  };

  return (
    <div className="flex justify-center items-center min-h-screen bg-gray-100 px-4">
      <div className="bg-white rounded-2xl shadow-lg p-6 w-full max-w-sm">
        <h2 className="text-xl font-semibold text-gray-800 mb-4">Confirm your Email</h2>

        <form onSubmit={handleSubmit} className="flex flex-col gap-4">
          <input
            type="email"
            placeholder="you@example.com"
            required
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            className="border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-orange-400 transition"
          />

          <button
            type="submit"
            className="bg-orange-500 hover:bg-orange-600 text-white font-medium py-2 rounded-lg transition"
          >
            Submit
          </button>

          <p className="text-sm text-gray-500 mt-2">
            Event: <span className="font-medium text-gray-700">{eventName}</span>
          </p>
        </form>
      </div>
    </div>
  );
};

export default Email;
