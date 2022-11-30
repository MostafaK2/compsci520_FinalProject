import { Input, Button, Radio, Slider } from "antd";
import { SearchOutlined } from "@ant-design/icons";
import { useState } from "react";

export const InputFields = () => {
  const [value, setValue] = useState(1);
  const [inputValue, setInputValue] = useState(1);

  const onChange = (e) => {
    setValue(e.target.value);
  };

  const onChangeSlider = (newValue) => {
    setInputValue(newValue);
  };

  return (
    <div>
      <div className="feature_block">
        <Input placeholder="Start" className="input-field" />
        <Input placeholder="Destination" className="input-field" />
      </div>
      <div className="feature_block">
        <Slider
          min={1}
          max={100}
          onChange={onChangeSlider}
          value={typeof inputValue === "number" ? inputValue : 0}
        />
        <h4 className="field_text"> {inputValue} % Away from Shortest Path</h4>
      </div>
      <div className="feature_block">
        <Radio.Group onChange={onChange} value={value} className="radio_item">
          <Radio value={1}>Maximize Elevation</Radio>
          <Radio value={2}>Minimize Elevation</Radio>
          <Radio value={3}>No Elevation</Radio>
        </Radio.Group>
      </div>
      <Button type="primary" icon={<SearchOutlined />}>
        Search
      </Button>
    </div>
  );
};
