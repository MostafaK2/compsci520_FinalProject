import { Layout } from "antd";

const { Header } = Layout;

export const TopHeader = () => (
  <Header
    data-testid = "topHeader"
    className="site-layout-sub-header-background"
    style={{
      padding: 0,
      height: "10vh",
    }}
  >
    <p className="header_name">520_SweSquad | ELeNa</p>
  </Header>
);
