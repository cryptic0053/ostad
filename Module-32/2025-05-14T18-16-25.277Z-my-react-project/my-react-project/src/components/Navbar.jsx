import React from "react";
import { Link, NavLink } from "react-router-dom";

function Navbar() {
  return (
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
      <div class="container-fluid">
        <a class="navbar-brand" href="#">
          Navbar
        </a>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNav"
          aria-controls="navbarNav"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav">
            <li class="nav-item">
              <NavLink
                to="/"
                style={({ isActive }) => ({
                  fontWeight: isActive ? "bold" : "normal",
                  color: isActive ? "blue" : "black",
                })}
              >
                Home
              </NavLink>
            </li>
            <li class="nav-item">
              <NavLink
                to="/about"
                style={({ isActive }) => ({
                  fontWeight: isActive ? "bold" : "normal",
                  color: isActive ? "blue" : "black",
                })}
              >
                About
              </NavLink>
            </li>
            <li class="nav-item">
              <NavLink
                to="/post"
                style={({ isActive }) => ({
                  fontWeight: isActive ? "bold" : "normal",
                  color: isActive ? "blue" : "black",
                })}
              >
                Posts
              </NavLink>
            </li>
            <li class="nav-item">
              <NavLink
                to="/contact"
                style={({ isActive }) => ({
                  fontWeight: isActive ? "bold" : "normal",
                  color: isActive ? "blue" : "black",
                })}
              >
                Contact
              </NavLink>
            </li>
            <li class="nav-item">
              <Link to="/user">Users</Link>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;
