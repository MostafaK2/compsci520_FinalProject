import { createContainer } from "unstated-next";
import { useState } from "react";

function useCounter(
  initialState = {
    startResults: [],
    endResults: [],
    newLocation: [42.3754, -72.5193],
    path: []
  }
) {
  let [startCoordinate, setStartCoordinate] = useState(
    initialState.startResults
  );
  let [endCoordinate, setEndCoordinate] = useState(initialState.endResults);
  let [newLocation, setNewLocation] = useState(initialState.newLocation);
  let [path, setPath] = useState(initialState.path);

  let callStart = (value) => {
    let res = value.split(",").map(Number);
    res.reverse();
    setStartCoordinate(res);
    setNewLocation(res);
  };
  let callEnd = (value) => {
    let res = value.split(",").map(Number);
    res.reverse();
    setEndCoordinate(res);
    setNewLocation(res);
  };

  let callPath = (value) => {
    if(value === "error"){
       return;
    }
    path = []
    value.forEach(points => {
      if("geometry" in points) {
        points['geometry'].forEach(elem => {
          elem.reverse()
        })
        path.push(...points['geometry']);
        // path = points['geometry']
      }
      // path = points['geometry']
    })
    console.log(path)
    setPath(path);
  };

  return { startCoordinate, endCoordinate, newLocation, path, callStart, callEnd, callPath };
}

export const Container = createContainer(useCounter);
