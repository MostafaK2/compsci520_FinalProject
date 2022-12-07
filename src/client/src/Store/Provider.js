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
    if(value.length === 0) {
      reset();
      return;
    }
    let res = value.split(",").map(Number);
    res.reverse();
    setStartCoordinate(res);
    if(endCoordinate.length === 0) {
      setNewLocation(res);
    }
    else {
      setNewLocation([(res[0]+endCoordinate[0])/2, (res[1]+endCoordinate[1])/2]);
    }
    
  };
  let callEnd = (value) => {
    if(value.length === 0) {
      reset();
      return;
    }
    let res = value.split(",").map(Number);
    res.reverse();
    setEndCoordinate(res);
    if(startCoordinate.length === 0) {
      setNewLocation(res);
    }
    else {
      setNewLocation([(startCoordinate[0]+res[0])/2, (startCoordinate[1]+res[1])/2]);
    }
  };

  const reset = () => {
    setStartCoordinate(initialState.startResults);
    setEndCoordinate(initialState.endResults);
    setNewLocation(initialState.newLocation);
    setPath(initialState.path);
  }

  let callPath = (value) => {
    // if(value === "error"){
    //    return;
    // }
    // path = []
    // value.forEach(points => {
    //   path.push([points[1], points[0]])
    // })
    // console.log(path)
    setPath(value);
  };

  return { startCoordinate, endCoordinate, newLocation, path, callStart, callEnd, callPath };
}

export const Container = createContainer(useCounter);
