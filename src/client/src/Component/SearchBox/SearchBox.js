import classes from "./SearchBox.module.css";
import { useState } from "react";

function SearchBox(props) {
  const [search, setSearch] = useState("");
  return (
    <div>
      <input
        className="input"
        id="something"
        placeholder={props.name}
        onChange={(elem) => setSearch(elem.target.value)}
      ></input>
    </div>
  );
}

export default SearchBox;
