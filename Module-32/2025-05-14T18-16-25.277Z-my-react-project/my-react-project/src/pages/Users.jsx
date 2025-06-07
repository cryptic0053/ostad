import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";

function Users() {
  const [users, setUsers] = useState([]);
  const [toggle, setToggle] = useState(false);
  useEffect(() => {
    fetch("https://jsonplaceholder.typicode.com/users")
      .then((response) => response.json())
      .then((data) => setUsers(data))
      .catch((err) => console.error(err));
  }, [toggle]);
  return (
    <div className="container mt-5">
      <h2 className="mb-4">Users</h2>
      <ul className="list-group">
        {users?.map((user) => (
          <Link key={user.id} to={`/user/${user.id}`}>
            <li className="list-group-item">
              {user.name}----{user.email}
            </li>
          </Link>
        ))}
      </ul>
      <button className="btn btn-primary" onClick={() => setToggle(!toggle)}>
        Toggle
      </button>
    </div>
  );
}

export default Users;
