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
<<<<<<< HEAD
    <div className="App" data-testid = "app">
=======
    <Container.Provider>
    <div className="App">
>>>>>>> 54f526fa9ee63070447b3a2046ca3087fec8754f
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
