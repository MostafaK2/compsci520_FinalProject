// jest-dom adds custom jest matchers for asserting on DOM nodes.
// allows you to do things like:
// expect(element).toHaveTextContent(/react/i)
// learn more: https://github.com/testing-library/jest-dom
import "@testing-library/jest-dom";
import { render, screen, fireEvent } from "@testing-library/react";
import { InputFields } from "../Components/InputFields";
import { Slider, Input, Radio } from "antd";
import userEvent from "@testing-library/user-event";
import { Container } from "../Store/Provider";

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

test("InputField renders", () => {
  render(
    <Container.Provider>
      <InputFields />
    </Container.Provider>
  );

  const component = screen.getByTestId("input-fields");
  expect(component).toBeInTheDocument();
});

test("initial configurations", () => {
  render(
    <Container.Provider>
      <InputFields />
    </Container.Provider>
  );

  expect(screen.getByText("Start")).toBeInTheDocument();
  expect(screen.getByText("Destination")).toBeInTheDocument();
  expect(screen.getByText("Search")).toBeInTheDocument();
  expect(screen.getByText("0 % Away from Shortest Path")).toBeInTheDocument();
});

test("test Start works properly", async () => {
  render(
    <Container.Provider>
      <InputFields />
    </Container.Provider>
  );
  const selectStart = screen.getAllByRole("combobox");
  await fireEvent.click(selectStart[0]);
  await userEvent.type(selectStart[0], "Amherst");

  expect(selectStart[0]).toHaveValue("Amherst");
});

test("test Destination works properly", async () => {
  render(
    <Container.Provider>
      <InputFields />
    </Container.Provider>
  );
  const selectStart = screen.getAllByRole("combobox");
  await fireEvent.click(selectStart[1]);
  await userEvent.type(selectStart[1], "Amherst");

  expect(selectStart[1]).toHaveValue("Amherst");
});

test("test sliders changes properly", async () => {
  render(
    <Container.Provider>
      <InputFields />
    </Container.Provider>
  );
  expect(screen.getByText("0 % Away from Shortest Path")).toBeInTheDocument();
  const slider = screen.getByTestId("slider");
  userEvent.type(slider, "98");
  expect(screen.getByText("98 % Away from Shortest Path")).toBeInTheDocument();
});

jest.clearAllMocks();

test("test elevation options selects and deselects", async () => {
  render(
    <Container.Provider>
      <InputFields />
    </Container.Provider>
  );

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
