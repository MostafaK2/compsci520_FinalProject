import { Layout, Input, Radio, Slider, Button } from "antd";
import { SearchOutlined } from "@ant-design/icons";
import { useState } from "react";

const { Sider } = Layout;

export const SideHeader = () => {
  const [collapsed, setCollapsed] = useState(false);
  const [value, setValue] = useState(1);

  const onChange = (e) => {
    // console.log("radio checked", e.target.value);
    setValue(e.target.value);
  };
  return (
    <Sider
      collapsible
      collapsed={collapsed}
      onCollapse={(value) => setCollapsed(value)}
      width={300}
    >
      <Input placeholder="Start" className="input-field" />
      <Input placeholder="Destination" className="input-field" />
      <Button type="primary" icon={<SearchOutlined />}>
        Search
      </Button>

      <h4 className="field_text">% Away from Shortest Path</h4>
      <Slider
        defaultValue={30}
        tooltip={{
          open: true,
        }}
      />

      <h4 className="field_text">Elevation</h4>
      <Radio.Group onChange={onChange} value={value} className="radio_item">
        <Radio value={1}>Maximize Elevation</Radio>
        <Radio value={2}>Minimize Elevation</Radio>
        <Radio value={3}>No Elevation</Radio>
      </Radio.Group>
    </Sider>
  );
};
