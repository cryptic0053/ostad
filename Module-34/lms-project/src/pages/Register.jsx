import { Lock, Mail, User } from "lucide-react";
import React, { useState } from "react";

function Register() {
  const [form, setForm] = useState({ username: "", email: "", password: "" });
  const [message, setMessage] = useState("");

  const handleChanges = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };
  const handleSubmit = async (e) => {
    e.preventDefault();
    console.log(form);
    try {
      const payload = {
        ...form,
        role: "student",
      };
      const res = await fetch(
        "https://lms-backend-xpwc.onrender.com/api/user/auth",
        {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(payload),
        }
      );

      const data = await res.json();
      if (res.ok) {
        console.log(data);
      }
    } catch (error) {}
  };
  return (
    <div className="min-h-screen flex justify-center items-center bg-gray-50 px-4">
      <div className="max-w-md bg-white p-8 rounded-2xl shadow-md">
        <h2 className="text-2xl font-semibold text-gray-800 mb-6 text-center">
          Create an Account
        </h2>
        <form onSubmit={handleSubmit} className="space-y-4">
          <div className="relative">
            <User size={20} className="absolute left-3 top-3 text-gray-400" />
            <input
              type="text"
              name="username"
              placeholder="User Name"
              onChange={handleChanges}
              className="w-full pl-10 pr-3 border border-teal-300 rounded-lg text-lg py-2 focus:outline-none focus:ring-2 focus:ring-teal-500"
            />
          </div>
          <div className="relative">
            <Mail size={20} className="absolute left-3 top-3 text-gray-400" />
            <input
              type="email"
              name="email"
              placeholder="Email"
              onChange={handleChanges}
              className="w-full pl-10 pr-3 border border-teal-300 rounded-lg text-lg py-2 focus:outline-none focus:ring-2 focus:ring-teal-500"
            />
          </div>
          <div className="relative">
            <Lock size={20} className="absolute left-3 top-3 text-gray-400" />
            <input
              type="password"
              name="password"
              placeholder="Password"
              onChange={handleChanges}
              className="w-full pl-10 pr-3 border border-teal-300 rounded-lg text-lg py-2 focus:outline-none focus:ring-2 focus:ring-teal-500"
            />
          </div>

          <button className="w-full bg-teal-600 hover:bg-teal-700 text-white py-2 rounded-full font-semibold">
            Register
          </button>
        </form>

        {message && (
          <p className="text-center mt-4 text-sm text-gray-600">{message}</p>
        )}
      </div>
    </div>
  );
}

export default Register;
