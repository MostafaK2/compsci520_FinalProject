import { createContainer } from "unstated-next";
import { useState } from "react";

function useCounter(
  initialState = {
    startResults: [42.3754, -72.5193],
    endResults: [42.3754, -72.5193],
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
    value.forEach(elem => {
      elem.reverse()
    });
    setPath(value);
  };

  return { startCoordinate, endCoordinate, newLocation, path, callStart, callEnd, callPath };
}

export const Container = createContainer(useCounter);
