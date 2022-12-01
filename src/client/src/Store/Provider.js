import { createContainer } from "unstated-next"
import { useState } from "react"

function useCounter(initialState = {startResults: "", endResults: ""}) {

  let [startCoordinate, setStartCoordinate] = useState(initialState.startResults)
  let [endCoordinate, setEndCoordinate] = useState(initialState.endResults)

  let callStart = (value) => {
    setStartCoordinate(value)
  }
  let callEnd = (value) => {
    setEndCoordinate(value);
  }
  return { startCoordinate, endCoordinate, callStart, callEnd }
}

export const Container = createContainer(useCounter)