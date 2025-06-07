import React from "react";

function UserGreeting({ user }) {
  return (
    <div>
      <h1>
        {user.isLoggedIn ? `Welcome Back, ${user.name}` : `Welcome, Guest!`}
      </h1>

      {(() => {
        if (!user.isLoggedIn) return null;
        if (user.role === "student") {
          return <p>Hope your studies are going well.</p>;
        }
        if (user.role === "mentor") {
          return <p>Thanks for helping students succeed!</p>;
        }

        return <p>Enjoy your time.</p>;
      })()}

      {user.isActive && <p>Status: Active ✅</p>}
    </div>
  );
}

export default UserGreeting;
