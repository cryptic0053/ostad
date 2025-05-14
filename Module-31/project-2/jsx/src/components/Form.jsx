import React, { useState } from "react";

function Form() {
  const [inputValue, setInputValue] = useState("");
  const handleForm = (event) => {
    event.preventDefault();
    alert(`You entered:${inputValue}`);
  };

  const handleInputChange = (event) => {
    setInputValue(event.target.value);
  };
  return (
    <div>
      <h1>Form</h1>

      <form onSubmit={handleForm}>
        <input
          type="text"
          placeholder="Enter something"
          onChange={handleInputChange}
        />
        <button type="submit">Submit</button>
      </form>
    </div>
  );
}

export default Form;
