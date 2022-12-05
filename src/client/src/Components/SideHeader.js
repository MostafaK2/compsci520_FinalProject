import { Layout } from "antd";
import { useState } from "react";
import { InputFields } from "./InputFields";

const { Sider } = Layout;

export const SideHeader = () => {
  const [collapsed, setCollapsed] = useState(false);
  const [isVisible, setVisible] = useState(true);

  const doCollapse = (value) => {
    setCollapsed(value);
    setVisible(!isVisible);
  };
  return (
    <Sider
      data-testid="sider"
      collapsible
      collapsed={collapsed}
      onCollapse={(value) => doCollapse(value)}
      width={300}
    >
      <div
        
        data-testid="checkVisible"
        className={isVisible ? "visible" : "invisible"}
      >
        <InputFields />
      </div>
    </Sider>
  );
};
