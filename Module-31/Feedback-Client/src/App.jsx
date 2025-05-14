import React, { useState } from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import FeedbackCard from "./components/FeedbackCard";

function App() {
  const [feedbacks, setFeedbacks] = useState([]);

  const [formData, setFormData] = useState({
    name: "",
    message: "",
  });

  const handleChange = (event) => {
    const { name, value } = event.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const handleFrom = (e) => {
    e.preventDefault();
    console.log(formData);
    setFeedbacks((prev) => [...prev, formData]);
    setFormData({
      name: "",
      message: "",
    });
  };

  const handleClear = () => {
    setFeedbacks([]);
  };

  return (
    <div className="container mt-5">
      <h2 className="text-center">Feedback Form</h2>
      <form className="mb-4" onSubmit={handleFrom}>
        <div className="mb-3">
          <input
            type="text"
            name="name"
            value={formData.name}
            placeholder="Enter your name"
            className="form-control"
            onChange={handleChange}
          />
        </div>
        <div className="mb-3">
          <textarea
            name="message"
            value={formData.message}
            className="form-control"
            placeholder="Your feedback"
            onChange={handleChange}
          ></textarea>
        </div>
        <button type="submit" className="btn btn-primary me-2">
          Submit
        </button>
        <button type="button" className="btn btn-danger" onClick={handleClear}>
          Clear All
        </button>
      </form>
      <div className="row">
        {feedbacks.map((feedback, index) => (
          <div className="col-md-6" key={index}>
            <FeedbackCard name={feedback.name} message={feedback.message} />
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
