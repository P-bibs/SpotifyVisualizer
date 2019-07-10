var boxAmt = 11

function makeLedBox(index){
  var topNode = document.createElement("div")
  topNode.id
  topNode.setAttribute("id", "LedBox" + index)
  topNode.setAttribute("class", "LedBox")

  return topNode
}

function setBoxColor(index, color) {
  var box = document.getElementById("LedBox" + index)
  box.style.backgroundColor = color
}

function init(){
  for (let i = 0; i < boxAmt; i++) {
    let box = makeLedBox(i)
    let body = document.getElementById("container")
    body.appendChild(box)
  }
}

function ripple(){
  middle = Math.floor(boxAmt/2)
  current = middle

  id = setInterval(propagate, 1000)

  function propagate() {
    if (current === boxAmt) {
      clearInterval(id)
    }
    current += 1
    setBoxColor(current-1, "white")
    setBoxColor(current, "red")
  }
}










function makeChordTile(members, name) {
    var topNode = document.createElement("div")
    topNode.setAttribute("class", "col-md-5 chord-tile chord-tile-inactive")
  
    var row1 = document.createElement("div")
    row1.setAttribute("class", "row")
    var membersDiv = document.createElement("div")
    membersDiv.setAttribute("class", "column chord-members")
    membersDiv.appendChild(document.createTextNode(members.map(a => a + "").toString().replace(/,/g, "\n")))
    row1.appendChild(membersDiv);
  
    var row2 = document.createElement("div")
    row2.setAttribute("class", "row")
    var nameDiv = document.createElement("div");
    nameDiv.setAttribute("class", "column chord-name")
    nameDiv.appendChild(document.createTextNode(name))
    row2.appendChild(nameDiv);
  
    var row3 = document.createElement("div")
    row3.classList.add("row")
    var outer = document.createElement("div")
    outer.classList.add("column")
    outer.classList.add("progress")
  
    var inner = document.createElement("div")
    inner.setAttribute("class", "progress-bar tile-progress-inner")
    inner.setAttribute("role", "progressbar")
    inner.setAttribute("aria-valuenow", "0")
    inner.setAttribute("aria-valuemin", "0")
    inner.setAttribute("aria-valuemax", "100")
  
    outer.appendChild(inner);
    row3.appendChild(outer)
  
    topNode.appendChild(row1);
    topNode.appendChild(row2);
    topNode.appendChild(row3);
  
    topNode.addEventListener("click", function (e) {
      var tiles = Array.from(document.getElementsByClassName("chord-tile"));
      playProg(tiles.indexOf(this));
    });
  
    return topNode;
  }