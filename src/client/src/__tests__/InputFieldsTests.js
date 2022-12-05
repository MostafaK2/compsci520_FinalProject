// jest-dom adds custom jest matchers for asserting on DOM nodes.
// allows you to do things like:
// expect(element).toHaveTextContent(/react/i)
// learn more: https://github.com/testing-library/jest-dom
import "@testing-library/jest-dom";
import { render, screen, cleanup, queryByTestId } from "@testing-library/react";
import { InputFields } from "../Components/InputFields";
import { Slider, Input, Radio } from "antd";
import { fireEvent } from "@testing-library/react";
import userEvent from "@testing-library/user-event";

jest.mock("antd", () => {
  const antd = jest.requireActual("antd");

  const Slider = (props) => {
    return (
      <input
        data-testid="slider"
        onChange={(e) => props.onChange(parseInt(e.target.value))}
        min={1}
        max={100}
      ></input>
    );
  };

  return {
    ...antd,
    Slider,
  };
});

// failing because axios error
test("InputField renders", () => {
  render(<InputFields />);
  const component = screen.getByTestId("input-fields");
  expect(component).toBeInTheDocument();
});

// failing because axios error
test("initial configurations", () => {
  render(<InputFields />);
  const start = screen.getByTestId("start");
  const destination = screen.getByTestId("destination");
  const button = screen.getByTestId("button");

  // start and destination fields should not have any value and have placeholders
  expect(start).not.toHaveValue();
  expect(destination).not.toHaveValue();
  expect(start).toHaveAttribute("placeholder", "Start");
  expect(destination).toHaveAttribute("placeholder", "Destination");

  expect(button).toHaveTextContent("Search");
  expect(screen.getByText("1 % Away from Shortest Path")).toBeInTheDocument();
});

// test("test inputs fields", () => {
//   render(<InputFields />);
//   const start = screen.getByTestId("start");
//   const destination = screen.getByTestId("destination");

//   userEvent.type(start, "someplace");
//   userEvent.type(destination, "otherplace");

//   expect(start.value).toBe("someplace");
//   expect(destination.value).toBe("otherplace");
// });

// test sliders works
test("test sliders", async () => {
  render(<InputFields />);
  expect(screen.getByText("1 % Away from Shortest Path")).toBeInTheDocument();
  const slider = screen.getByTestId("slider");
  userEvent.type(slider, "98");
  expect(screen.getByText("98 % Away from Shortest Path")).toBeInTheDocument();
});

jest.clearAllMocks();

test("test elevation options", async () => {
  render(<InputFields />);

  const radioGroup = screen.getByTestId("options");
  const max = screen.getByTestId("max");
  const min = screen.getByTestId("min");
  const noElev = screen.getByTestId("no-elev");
  expect(radioGroup).toBeInTheDocument();

  expect(max).toBeChecked();
  expect(min).not.toBeChecked();
  expect(noElev).not.toBeChecked();

  fireEvent.click(min);
  expect(min).toBeChecked();

  fireEvent.click(noElev);
  expect(noElev).toBeChecked();
});
