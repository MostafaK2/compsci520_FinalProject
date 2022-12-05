import "@testing-library/jest-dom";
import { render, screen, cleanup, queryByTestId } from "@testing-library/react";
import { TopHeader } from "../Components/TopHeader";
import { SideHeader } from "../Components/SideHeader";
import { fireEvent } from "@testing-library/react";
import { Layout } from "antd";

// jest.mock("antd", () => ({
//   ...jest.requireActual("antd"),
//   defualt: jest.fn(() => 42),
// //   Layout: jest.fn(() => <section></section>),
// }));

// top header renders and will have the following text
test("Top Header renders and have required text", () => {
  render(<TopHeader />);
  const component = screen.getByTestId("topHeader");
  expect(component).toBeInTheDocument();
  expect(screen.getByText("520_SweSquad | ELeNa")).toBeInTheDocument();
});

// side header renders

test("side header renders", async () => {
  render(<SideHeader />);
  const visibleDiv = screen.getByTestId("checkVisible");
  const comp = screen.getByTestId("sider");
  expect(visibleDiv.className).toBe("visible");
  fireEvent.change(comp, { target: { collapsed: true } });
  expect(comp.collapsed).toBe(true);
  // expect(comp).not.toContainElement(visibleDiv);
  
});
