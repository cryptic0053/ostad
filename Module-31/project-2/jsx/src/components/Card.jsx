import React from "react";

function Card({ children }) {
  return (
    <div
      
        style={{ border: "1px solid gray", margin: "10px", padding: "10px" }}
      >
        {children}
    </div>
  );
}

export default Card;
