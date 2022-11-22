// import logo from './logo.svg';
import "./App.css";
import { Layout } from "antd";
import { Map } from "./Components/Map";
import { TopHeader } from "./Components/TopHeader";
import { SideHeader } from "./Components/SideHeader";

const { Content } = Layout;

function App() {
  return (
    <div className="App">
      <Layout>
        <TopHeader/>
        <Layout>
          <Content>
            <Map />
          </Content>
          <SideHeader/>
        </Layout>
      </Layout>
    </div>
  );
}

export default App;
