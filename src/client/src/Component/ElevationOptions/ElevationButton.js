import classes from "./ElevationButton.module.css";

// button name is going to be in props
function ElevationButton(props) {
  return (
    <div>
      <button className="" onClick={() => console.log(clickedButton)}>
        button Name is going to in props
      </button>
    </div>
  );
}

export default ElevationButton;
