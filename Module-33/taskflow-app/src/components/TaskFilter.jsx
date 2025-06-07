import React from "react";

function TaskFilter({ currentFilter, onFilterChange, tasksCount }) {
  return (
    <div className="flex justify-center gap-3 mt-6">
      <button
        className={`px-4 py-1 rounded-full  font-medium border transition ${
          currentFilter == "all"
            ? "bg-blue-600 text-white border-blue-600"
            : "bg-white text-gray-600 hover:bg-gray-100"
        }`}
        onClick={() => onFilterChange("all")}
      >
        All ({tasksCount.all})
      </button>

      {/* completed  */}
      <button
        className={`px-4 py-1 rounded-full  font-medium border transition ${
          currentFilter == "completed"
            ? "bg-blue-600 text-white border-blue-600"
            : "bg-white text-gray-600 hover:bg-gray-100"
        }`}
        onClick={() => onFilterChange("completed")}
      >
        Completed ({tasksCount.completed})
      </button>

      {/* pending  */}
      <button
        className={`px-4 py-1 rounded-full  font-medium border transition ${
          currentFilter == "pending"
            ? "bg-blue-600 text-white border-blue-600"
            : "bg-white text-gray-600 hover:bg-gray-100"
        }`}
        onClick={() => onFilterChange("pending")}
      >
        Pending ({tasksCount.pending})
      </button>
    </div>
  );
}

export default TaskFilter;
