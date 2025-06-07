import React, { useState } from "react";
import Name from "./components/Name";
import UserGreeting from "./components/UserGreeting";

function App() {
  const active = true;
  const [user, setUser] = useState({
    isLoggedIn: true,
    name: "Fahim",
    role: "student",
    isActive: true,
  });
  return (
    <div>
      {/* <h1>My APP</h1>

      {user?.isLogin ? (
        <div>{user.age > 18 && <Name name={user.name} age={user.age} />}</div>
      ) : (
        <div>
          <h1>Please Login</h1>
        </div>
      )} */}

      <UserGreeting user={user} />
    </div>
  );
}

export default App;
