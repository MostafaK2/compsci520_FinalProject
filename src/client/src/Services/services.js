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

export const getMinPath = (data) =>
  HTTP.post("/path", JSON.stringify(data), {
    headers: headers,

  })
    .then((res) => {
      const polygon = [
        [51.515, -0.09],
        [51.52, -0.1],
        [51.52, -0.12],
      ]
      return polygon
    })
    .catch((error) => {
        console.log(error)
      return "error";
    });

export const getMetaData = (src, dest, flag, percent) =>
  HTTP.get("/metadata", { params : {
    src: src.toString(),
    dest: dest.toString(), 
    flag: flag, 
    percent: percent
  }})
    .then((res) => {
      return res.data
    })
    .catch((error) => {
        console.log(error)
      return "error";
    });

export const getFakePath = (start, end, percent, elevation) => {
  console.log(start, end, percent, elevation);
  let polygon = [
    [
      -72.52741318938568,
      42.351571857820915
    ],
    [
      -72.52584677932091,
      42.35160357332603
    ],
    [
      -72.52439838645293,
      42.3518335102587
    ],
    [
      -72.52355080840422,
      42.35222995127128
    ],
    [
      -72.52314311263358,
      42.35274532084901
    ],
    [
      -72.52256749731475,
      42.353485459659026
    ],
    [
      -72.52196192299469,
      42.3542505714602
    ],
    [
      -72.52120190559842,
      42.355539254299174
    ],
    [
      -72.52086627132924,
      42.35575972188104
    ],
    [
      -72.52090356402601,
      42.35716518453327
    ],
    [
      -72.52086627132924,
      42.35859817291259
    ],
    [
      -72.52075439323957,
      42.359810676018384
    ],
    [
      -72.52075442857516,
      42.360995600159015
    ],
    [
      -72.52071713587895,
      42.362373390214486
    ],
    [
      -72.52064255048545,
      42.36394403402403
    ],
    [
      -72.52053067774318,
      42.3650342915183
    ],
    [
      -72.52030692156374,
      42.3665773151576
    ],
    [
      -72.52000857999082,
      42.3685611470049
    ],
    [
      -72.51982211650761,
      42.369966323324405
    ],
    [
      -72.51963565302492,
      42.371702085967826
    ],
    [
      -72.51978482381139,
      42.373134742806656
    ],
    [
      -72.51982214404835,
      42.37438126064487
    ],
    [
      -72.51982214404835,
      42.37573120750548
    ],
    [
      -72.51989813553861,
      42.377034259009264
    ],
    [
      -72.5199727209321,
      42.37846679421503
    ],
    [
      -72.51963708666241,
      42.37978910540022
    ],
    [
      -72.51922687616822,
      42.381345484909446
    ],
    [
      -72.51986085201034,
      42.38214434795441
    ],
    [
      -72.5207220824967,
      42.38328411590379
    ],
    [
      -72.52139335103557,
      42.384661417108106
    ],
    [
      -72.52213920496737,
      42.385763236316535
    ],
    [
      -72.52645810955397,
      42.38524371532918
    ],
    [
      -72.52888014642305,
      42.384738130117825
    ],
    [
      -72.53103891841549,
      42.385204824304
    ],
    [
      -72.53325034338282,
      42.38458256461817
    ],
    [
      -72.53577768620315,
      42.383999190561326
    ],
    [
      -72.53962135340818,
      42.384154757506536
    ],
    [
      -72.54309644978605,
      42.38438810720132
    ],
    [
      -72.54794052352422,
      42.38481591272284
    ],
    [
      -72.54846097495584,
      42.38184214650232
    ],
    [
      -72.54863716885188,
      42.37780739883283
    ],
    [
      -72.55286582235955,
      42.37633226507583
    ],
    [
      -72.56892721775692,
      42.37040177053996
    ],
    [
      -72.5697539795094,
      42.36884440610808
    ],
    [
      -72.56904948414511,
      42.36685692671935
    ],
    [
      -72.56975749051912,
      42.363119629704016
    ],
    [
      -72.57399213253557,
      42.361234640068375
    ],
    [
      -72.57763338846878,
      42.35963629357147
    ],
    [
      -72.57967420370876,
      42.3568939520554
    ],
    [
      -72.58291502841854,
      42.35543313170558
    ],
    [
      -72.58705169323066,
      42.35457213296766
    ],
    [
      -72.5884449894324,
      42.355295495144844
    ]
  ];
  return polygon
}