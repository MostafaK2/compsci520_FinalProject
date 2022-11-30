// import logo from './logo.svg';
import "./App.css";
import { Layout } from "antd";
import { Map } from "./Components/Map";
import { TopHeader } from "./Components/TopHeader";
import { SideHeader } from "./Components/SideHeader";
import { Container } from "./Store/Provider";

const { Content } = Layout;

function App() {
  return (
    <Container.Provider>
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
    </Container.Provider>
  );
}

export default App;
