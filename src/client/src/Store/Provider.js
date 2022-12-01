import { createContainer } from "unstated-next"
import { useState } from "react"

function useCounter(initialState = {startResults: [42.3754, -72.5193], endResults: [42.3754, -72.5193], newLocation: [42.3754, -72.5193]}) {

  let [startCoordinate, setStartCoordinate] = useState(initialState.startResults)
  let [endCoordinate, setEndCoordinate] = useState(initialState.endResults)
  let [newLocation, setNewLocation] = useState(initialState.newLocation)

  let callStart = (value) => {
    let res = value.split(",").map(Number);
    res.reverse();
    setStartCoordinate(res);
    setNewLocation(res);
  }
  let callEnd = (value) => {
    let res = value.split(",").map(Number);
    res.reverse();
    setEndCoordinate(res);
    setNewLocation(res);
  }
  return { startCoordinate, endCoordinate, newLocation, callStart, callEnd }
}

export const Container = createContainer(useCounter)