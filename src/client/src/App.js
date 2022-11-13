// import logo from './logo.svg';
import "./App.css";
import ElevationButton from "./Component/ElevationOptions/ElevationButton";
import SearchBox from "./Component/SearchBox/SearchBox";
import ScrollingElev from "./Component/ElevationOptions/ScrollingElev";

function App() {
  return (
    <div className="App">
      <div id="Purple_Side">
        <div id="search_functionalities">
          <SearchBox name="Start" />
          <SearchBox name="Destination" />
        </div>
        <div id="Elevation_Options">
          <ElevationButton name="Max Elevation"/>
          <ElevationButton name="Min Elevation"/>
          <ElevationButton name="No Elevation"/>
          <ScrollingElev/>
        </div>
      </div>
    </div>
  );
}

export default App;
