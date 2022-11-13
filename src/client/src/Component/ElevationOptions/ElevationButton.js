import { useState } from "react";
import classes from "./ElevationButton.module.css";

// button name is going to be in props
function ElevationButton(props) {
  const [buttonClicked, setButtonClicked] = useState(false);

  function callback() {}

  return (
    <div>
      <button className="" onClick={callback}>
        {props.name}
      </button>
    </div>
  );
}

export default ElevationButton;
