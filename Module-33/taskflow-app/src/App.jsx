import { Camera } from "lucide-react";
import React, { useEffect, useState } from "react";
import AppHeader from "./components/AppHeader";
import TaskForm from "./components/TaskForm";
import TaskFilter from "./components/TaskFilter";
import TaskList from "./components/TaskList";

function App() {
  const [tasks, setTasks] = useState([]);
  const [filter, setFilter] = useState("all");
  const handleTask = (newTask) => {
    // console.log(newTask);

    const updatedTasks = [...tasks, newTask];
    setTasks(updatedTasks);

    localStorage.setItem("tasks", JSON.stringify(updatedTasks));
  };

  const taskCounts = {
    all: tasks.length,
    completed: tasks.filter((t) => t.completed).length,
    pending: tasks.filter((t) => !t.completed).length,
  };

  const filteredTasks = tasks.filter((task) => {
    if (filter === "completed") return task.completed;
    if (filter === "pending") return !task.completed;
    return true;
  });

  const handleDelete = (id) => {
    const updatedTasks = tasks.filter((task) => task.id != id);
    setTasks(updatedTasks);
    localStorage.setItem("tasks", JSON.stringify(updatedTasks));
  };

  const handleToggleCompeleted = (id) => {
    const updatedTasks = tasks.map((task) =>
      task.id === id ? { ...task, completed: !task.completed } : task
    );

    setTasks(updatedTasks);
    localStorage.setItem("tasks", JSON.stringify(updatedTasks));
  };
  useEffect(() => {
    const storedTask = JSON.parse(localStorage.getItem("tasks")) || [];
    setTasks(storedTask);
  }, []);
  return (
    <div className="min-h-screen bg-gray-100 py-8 px-4">
      <div className="max-w-3xl mx-auto">
        <AppHeader />
        <TaskForm handleTask={handleTask} />
        <TaskFilter
          currentFilter={filter}
          onFilterChange={setFilter}
          tasksCount={taskCounts}
        />

        <TaskList
          tasks={filteredTasks}
          handleDelete={handleDelete}
          handleToggleCompeleted={handleToggleCompeleted}
        />
      </div>
    </div>
  );
}

export default App;
