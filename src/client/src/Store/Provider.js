import { createContainer } from "unstated-next"
import { useState } from "react"

function useCounter(initialState = {start: "", end: ""}) {
  let [start, setStart] = useState(initialState.start)
  let [end, setEnd] = useState(initialState.end)
  let callStart = (e) => setStart(e.target.value)
  let callEnd = (e) => setEnd(e.target.value)
  return { start, end, callStart, callEnd }
}

export const Container = createContainer(useCounter)