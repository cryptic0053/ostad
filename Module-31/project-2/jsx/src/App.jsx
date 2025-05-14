import React from "react";
import Child from "./components/Child";
import Card from "./components/Card";

function App() {
  return (
    <div>
      <Child name={"Cryptic"} age={24} />
      <Child name={"Argha"} age={23} />

      <p>-------------------------</p>
      <Card>
        <Child name={"Ani"} age={23}/>
      </Card>
    </div>
  );
}

export default App;
