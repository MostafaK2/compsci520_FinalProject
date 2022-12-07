import { Button, Radio, Slider, Select, Modal } from "antd";
import { SearchOutlined } from "@ant-design/icons";
import { useState } from "react";
import { Container } from "../Store/Provider";
import { getMatchedResults } from "../Services/Autocomplete";
import { getMetaData } from "../Services/services";

export const InputFields = () => {
  const [value, setValue] = useState(1);
  const [inputValue, setInputValue] = useState(0);
  const [startValue, setStartValue] = useState();
  const [startData, setStartData] = useState([]);
  const [endValue, setEndValue] = useState();
  const [endData, setEndData] = useState([]);
  const [isDisabled, setDisabled] = useState(false);
  const [isReset, setReset] = useState(false);
  const [isSameCity, setSameCity] = useState(false);

  const container = Container.useContainer();

  const onChange = (e) => {
    setValue(e.target.value);
  };

  const onChangeSlider = (newValue) => {
    setInputValue(newValue);
  };

  const handleStartSearch = async (newValue) => {
    if (newValue) {
      const results = await getMatchedResults(newValue);
      setStartData(results);
    }
  };

  const handleStartChange = (newValue) => {
    setStartValue(newValue);
  };

  const handleEndSearch = async (newValue) => {
    if (newValue) {
      const results = await getMatchedResults(newValue);
      setEndData(results);
    } else {
      setEndData([]);
    }
  };

  const handleEndChange = (newValue) => {
    setEndValue(newValue);
  };

  const handleStartSelect = (value) => {
    container.callStart(value);
  };

  const handleEndSelect = (value) => {
    container.callEnd(value);
  };

  const sendData = async (e) => {
    setDisabled(true);
    setReset(true);
    const path = await getMetaData(
      container.startCoordinate,
      container.endCoordinate,
      inputValue,
      value
    );
    if(path === "error") {
      setSameCity(true);
      setDisabled(false);
      setReset(false);
      reset();
      return;
    }
    container.callPath(path);
    setDisabled(false);
    setReset(false);
  };

  const reset = () => {
    setValue(1);
    setStartValue();
    setInputValue(0);
    setStartData([]);
    setEndValue();
    setEndData([]);
    container.callPath([]);
    container.callStart("");
    container.callEnd("");
  }

  return (
    <div data-testid="input-fields">
      <Modal open={isDisabled} title="Fetch path details..." footer={null} closable={false}/>
      <Modal open={isSameCity} 
      title="Please perform search in the same city." 
      cancelButtonProps={{ style: {"display": "none"} }} onOk={() => setSameCity(false)}/>
      <div className="feature_block">
        <Select
          data-testid="start"
          showSearch
          value={startValue}
          placeholder="Start"
          showArrow={false}
          filterOption={false}
          onSearch={handleStartSearch}
          onChange={handleStartChange}
          onSelect={handleStartSelect}
          className="input-field"
          notFoundContent={null}
          options={(startData || []).map((d) => ({
            value: d.x + "," + d.y,
            label: d.label,
          }))}
        />
        <Select
          data-testid="destination"
          showSearch
          value={endValue}
          placeholder="Destination"
          showArrow={false}
          filterOption={false}
          onSearch={handleEndSearch}
          onChange={handleEndChange}
          onSelect={handleEndSelect}
          className="input-field"
          notFoundContent={null}
          options={(endData || []).map((d) => ({
            value: d.x + "," + d.y,
            label: d.label,
          }))}
        />
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
        <Radio.Group
          data-testid="options"
          testValue={value}
          onChange={onChange}
          value={value}
          className="radio_item"
        >
          <Radio data-testid="max" value={1}>
            Maximize Elevation
          </Radio>
          <Radio data-testid="min" value={2}>
            Minimize Elevation
          </Radio>
          <Radio data-testid="no-elev" value={3}>
            No Elevation
          </Radio>
        </Radio.Group>
      </div>
      <Button
        data-testid="button"
        type="primary"
        icon={<SearchOutlined />}
        onClick={sendData}
        disabled={isDisabled}
      >
        Search
      </Button>
      <Button onClick={reset} disabled={isReset}>Reset</Button>
    </div>
  );
};
