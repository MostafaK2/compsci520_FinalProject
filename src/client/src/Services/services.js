import axios from "axios";

const HTTP = axios.create({
  baseURL: "http://localhost:5000",
});

const headers = {
  "Content-Type": "application/json",
};

export const checkApi = (data) =>
  HTTP.post("/", JSON.stringify(data), {
    headers: headers,
  })
    .then((res) => {
      console.log(res);
    })
    .catch((error) => {
      return "error";
    });

export const getMetaData = (src, dest, flag, percent) =>
  HTTP.get("/metadata", { params : {
    src: src[1].toString() + "," + src[0].toString(),
    dest: dest[1].toString() + "," + dest[0].toString(), 
    flag: flag, 
    percent: percent
  }})
    .then((res) => {
      // console.log(res)
      return res.data
    })
    .catch((error) => {
      console.log(error)
      return "error";
    });
