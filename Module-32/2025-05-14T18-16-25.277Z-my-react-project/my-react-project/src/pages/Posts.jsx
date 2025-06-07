import React, { useEffect, useState } from "react";

function Posts() {
  const [posts, setPosts] = useState([]);

  const fetchUser = async () => {
    try {
      const res = await fetch("https://jsonplaceholder.typicode.com/posts");
      const data = await res.json();
      console.log(data);
      setPosts(data);
    } catch (error) {
      console.error(error);
    }

    console.log("Hello from posts");
  };

  useEffect(() => {
    fetchUser();
  }, []);
  return (
    <div className="container mt-5">
      <h2 className="mb-4">Posts</h2>
      <div>
        {posts?.map((post) => (
          <div class="card text-bg-primary mb-3">
            <div class="card-header">
              <b>{post?.title}</b>
            </div>
            <div class="card-body">
              <p class="card-text">{post.body}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Posts;
