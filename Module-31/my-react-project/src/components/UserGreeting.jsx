import React from "react";

function UserGreeting({ user }) {
  const hello = () => {
    return 0;
  };
  return (
    <div>
      <h1>
        {user.isLoggedIn ? `Welcome back, ${user.name}` : `Welcome,Guest`}
      </h1>
      {(() => {
        if (user.isLoggedIn) return null;
        if (user.role === "Student") {
          return <p>Studies well</p>;
        }
        if (user.role === "mentor") {
          return <p>Thanks for teaching</p>;
        }
        return <p>Enjoy</p>;
      })()}

      {user.isActive && <p>Status:Active</p>}
    </div>
  );
}

export default UserGreeting;
