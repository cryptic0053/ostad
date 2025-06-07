import React from "react";
import { useParams } from "react-router-dom";

function User() {
  const { id } = useParams();
  return (
    <div>
      <h1>I am from User</h1>
      <h2>User id: {id}</h2>
    </div>
  );
}

export default User;
