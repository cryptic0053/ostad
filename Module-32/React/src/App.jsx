import React, { useRef, useState } from "react";
import "./App.css";

function App() {
  const paraRef = useRef();
  const divRef = useRef();
  const inputRef = useRef();
  const boxRef = useRef();
  const [value, setValue] = useState(0);

  const showText = () => {
    alert("InnerText: " + paraRef.current.innerText);
    alert("InnerHTML: " + paraRef.current.innerHTML);
    
  };

  const handleClick = () => {
    const title = divRef.current.getAttribute("title");
    alert("Title: " + title);
    divRef.current.setAttribute("title","Now I am changed");
    divRef.current.setAttribute("id","hover");
  };

  const showValue = () => {
    const value = inputRef.current.value;
    alert("Input Value: " + value);
  }

  const toggle = () => {
    boxRef.current.classList.toggle("highlight");
  };

  const increase = () => {
    setValue(value+1);alert("Count: " + value);
  };

  return (
    <div>
      <p ref={paraRef}>
        <h1>Hello</h1>
        <strong>bro</strong>
      </p>
      <button onClick={showText}>Show text</button>
      <div ref={divRef} title="Hello">
        Hover over me
      </div>
      <button onClick={handleClick}>Click attribute</button>
      <div>
        <input ref={inputRef} type="text" placeholder="Type something" />
        <button onClick={showValue}>Show Value</button>
      </div>
      <div ref={boxRef} className="box">
        I am a box
      </div>
      <button onClick={toggle}>Toggle highlight</button>
      <div>
        <h1>Count: {value}</h1>
        <button onClick={increase}>Increase Count</button>
      </div>
    </div>
  );
}

export default App;
