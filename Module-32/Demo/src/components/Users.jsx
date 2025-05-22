import React, { useEffect,useState } from 'react'

function Users() {
    const [users, setUsers] = useState([]);

    useEffect(() => {
        fetch('https://jsonplaceholder.typicode.com/users')
        .then((res) =>res.json())
        .then((data) => setUsers(data))
        .catch((err) => console.error(err));

    }, []);
  return <div>Users</div>;
}

export default Users
