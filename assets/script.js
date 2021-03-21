let setGrid = () => {
  let height = document.getElementById("height").value;
  let width = document.getElementById("width").value;
  pywebview.api.print(height, width);
};
