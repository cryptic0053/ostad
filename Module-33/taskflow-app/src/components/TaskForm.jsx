import { PlusCircle } from "lucide-react";
import React, { useState } from "react";

function TaskForm({ handleTask }) {
  const [title, setTitle] = useState("");
  const [category, setCategory] = useState("Study");
  const [priority, setPriority] = useState("Medium");
  const [error, setError] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();

    if (title.trim() === "") {
      setError("Title is required");
      return;
    }

    const newTask = {
      id: crypto.randomUUID(),
      title: title.trim(),
      category: category,
      priority: priority,
      completed: false,
      createdAt: new Date().toISOString(),
    };
    handleTask(newTask);

    setTitle("");
    setCategory("Personal");
    setPriority("Medium");

    setError("");
  };
  return (
    <div className="bg-white p-6 mt-8 rounded-lg shadow-md">
      <h2 className="text-xl font-semibold text-gray-800 mb-4 ">
        Add New Task
      </h2>

      <form onSubmit={handleSubmit} className="space-y-4">
        <div>
          <label htmlFor="title" className="block mb-1">
            Task Title
          </label>
          <input
            type="text"
            id="title"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            placeholder="Enter Task Title"
            className="w-full px-4 py-2 border border-gray-300 rounded"
          />
          {error && <p className="text-red-500 text-sm">{error}</p>}
        </div>
        <div>
          <label htmlFor="category" className="block mb-1">
            Category
          </label>

          <select
            id="category"
            value={category}
            onChange={(e) => setCategory(e.target.value)}
            className="w-full px-4 py-2 border border-gray-300 rounded"
          >
            <option value="Work">Work</option>
            <option value="Personal">Personal</option>
            <option value="Health">Health</option>
            <option value="Study">Study</option>
            <option value="Others">Others</option>
          </select>
        </div>
        <div>
          <label htmlFor="priority" className="block mb-1">
            Priority
          </label>

          <select
            id="priority"
            value={priority}
            onChange={(e) => setPriority(e.target.value)}
            className="w-full px-4 py-2 border border-gray-300 rounded"
          >
            <option value="High">High</option>
            <option value="Medium">Medium</option>
            <option value="Low">Low</option>
          </select>
        </div>
        <button
          type="submit"
          className="w-full md:w-auto px-6 py-2 bg-blue-600 hover:bg-blue-700 text-white font-medium rounded-lg flex items-center justify-center"
        >
          <PlusCircle className="h-4 w-4 mr-2" />
          Add Task
        </button>
      </form>
    </div>
  );
}

export default TaskForm;
