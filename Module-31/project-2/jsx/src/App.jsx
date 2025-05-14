import React, { useState } from "react";
import Child from "./components/Child";
import Card from "./components/Card";
import Form from "./components/Form";

function App() {
  const handleClick = (name) => {
    alert(`Hello,${name}`);
  };

  const [count, setCount] = useState(0);
  const handleIncrement = () => {
    setCount(count + 1);
  };

  const handleAdd = (value) => {
    setCount(count + value);
  };
  return (
    <div>
      <Child name={"Cryptic"} age={24} />
      <Child name={"Argha"} age={23} />

      <p>-------------------------</p>
      <Card>
        <Child name={"Ani"} age={23} />
      </Card>

      <Card>
        <Child name={"Arg"} age={23} />
      </Card>

      <Card>
        <Child name={"Abc"} age={23} />
      </Card>

      <div>
        <button onClick={() => handleClick("Argha")}>Greet Guest</button>
      </div>

      <h2>{count}</h2>
      <button onClick={handleIncrement}>Increment</button>
      <button onClick={() => handleAdd(100)}>Add any value</button>

      <Form />
    </div>
  );
}

export default App;
