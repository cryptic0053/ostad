import React from "react";

function Child({ name, age }) {
  return (
    <div>
      <h1>Hello,{name}</h1>
      <p>{age} years old</p>
    </div>
  );
}

export default Child;
