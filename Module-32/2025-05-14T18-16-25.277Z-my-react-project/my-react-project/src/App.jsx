import React from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Home from "./pages/Home";
import About from "./pages/about";
import Users from "./pages/Users";
import Posts from "./pages/Posts";
import ContactForm from "./pages/ContactForm";
import Navbar from "./components/Navbar";
import User from "./pages/User";

function App() {
  return (
    <div>
      <BrowserRouter>
        <Navbar />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<About />} />
          <Route path="/user" element={<Users />} />
          <Route path="/user/:id" element={<User />} />
          <Route path="/post" element={<Posts />} />
          <Route path="/contact" element={<ContactForm />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
