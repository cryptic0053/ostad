import React, { useState } from "react";
import Name from "./components/Name";
import UserGreeting from "./components/UserGreeting";

function App() {
  const active = true;

  const [user, setUser] = useState({
    isLogin: false,
    name: "Argha",
    age: 23,
    active: false,
  });

  return (
    <div>
      <h1>My App</h1>

      {user?.isLogin ? (
        <div>
          <Name name={user.name} />
        </div>
      ) : (
        <div>
          <h1>Please login</h1>
        </div>
      )}

      <Name name={"BD"} age={20} />
      <Name name={"Raj"} age={10} />

      <UserGreeting
        user={{
          isLoggedIn: true,
          name: "Argha",
          role: "mentor",
          isActive: true,
        }}
      />
    </div>
  );
}

export default App;
