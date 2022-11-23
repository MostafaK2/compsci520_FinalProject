import axios from "axios";

const HTTP = axios.create({
  baseURL: "https://localhost:5000",
});

const headers = {
  "Content-Type": "application/json",
};

export const checkApi = (data) =>
  HTTP.post("/", JSON.stringify(data), {
    headers: headers,
  })
    .then((res) => {
      print(res);
    })
    .catch((error) => {
      return "error";
    });

export const getMinPath = (data) =>
  HTTP.post("/getpath", JSON.stringify(data), {
    headers: headers,
  })
    .then((res) => {
      print(res);
    })
    .catch((error) => {
        console.log(error)
      return "error";
    });
