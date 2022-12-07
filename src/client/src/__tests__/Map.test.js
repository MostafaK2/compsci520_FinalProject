import "@testing-library/jest-dom";
import { render, screen, cleanup, queryByTestId } from "@testing-library/react";
import { Map } from "../Components/Map";
import { Slider, Input, Radio } from "antd";
import { fireEvent } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { Container } from "../Store/Provider";

test("Map renders",()=>{
	expect(render(<map />)).not.toBeNull;
});
