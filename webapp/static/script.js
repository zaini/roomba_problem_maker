let height = 10;
let width = 15;
let type = "_";

const postData = async (url = "", data = {}) => {
  const response = await fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Accept: "application/json",
    },
    body: JSON.stringify(data),
  });
  return response.json();
};

let generateRandomPDDL = async () => {
  let res = await postData((url = "http://localhost:5000/problem/random/new"));
  alert(`Generated random problem.`);
  document.getElementById("result").value = res;
  document.getElementById("result").rows = "50";
};

let generatePDDL = async () => {
  let grid = "";
  for (var i = 0; i < height; i++) {
    for (var j = 0; j < width; j++) {
      cell = document.getElementById(`${i}-${j}`);
      if (cell.innerText === "") {
        grid += "_";
      } else {
        grid += cell.innerText;
      }
    }
    if (i != height - 1) {
      grid += ",";
    }
  }

  charge = document.getElementById("charge").value;
  trash = document.getElementById("trash").value;

  let res = await postData(
    (url = "http://localhost:5000/problem/new"),
    (data = { grid, charge, trash })
  );

  alert(`Generated your problem.`);
  document.getElementById("result").value = res;
  document.getElementById("result").rows = "50";
};

let setGridSize = () => {
  height = document.getElementById("height").value;
  width = document.getElementById("width").value;
  updateGrid();
};

let setType = () => {
  type = document.getElementById("type-selector").value;
};

let setGrid = (x, y) => {
  cell = document.getElementById(`${x}-${y}`);

  // <option value="_" default>Empty grid</option>
  // <option value="X">Starting (Roomba)</option>
  // <option value="C">Charger</option>
  // <option value="T">Trash</option>
  // <option value="O">Obstacle</option>
  let color = "white";
  switch (type) {
    case "_":
      color = "white";
      type = "";
      break;
    case "X":
      color = "lime";
      break;
    case "C":
      color = "yellow";
      break;
    case "T":
      color = "blue";
      break;
    case "O":
      color = "red";
      break;
    default:
      color = "white";
      break;
  }

  cell.style.backgroundColor = color;
  cell.innerHTML = `<div style="text-align: center; top: 50%">${type}</div>`;
};

let updateGrid = () => {
  let grid = document.getElementById("grid");
  let tbl = document.createElement("table");
  tbl.style.border = "1px solid #262626";

  for (var i = 0; i < height; i++) {
    var tr = tbl.insertRow();
    for (var j = 0; j < width; j++) {
      let td = tr.insertCell();
      let cell = document.createElement("div");
      cell.id = `${i}-${j}`;
      cell.setAttribute("onclick", `setGrid(${i}, ${j})`);
      cell.style.border = "1px solid #262626";
      cell.style.height = "50px";
      cell.style.width = "50px";
      td.appendChild(cell);
    }
  }
  grid.innerHTML = "";
  grid.appendChild(tbl);
};
