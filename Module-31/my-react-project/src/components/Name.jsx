import React from "react";

function Name({ name, age }) {
  console.log("Hello");
  return (
    <div>
      <h1>
        Welcome to {name}--{age}
      </h1>
    </div>
  );
}

export default Name;
