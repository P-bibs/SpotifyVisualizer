var boxAmt = 21
var stepDuration = 1000

function makeLedBox(index){
  var topNode = document.createElement("div")
  topNode.id
  topNode.setAttribute("id", "LedBox" + index)
  topNode.setAttribute("class", "LedBox")

  return topNode
}

function setBoxColor(index, color, duration) {
  if (index >= boxAmt || index < 0) return

  var box = document.getElementById("LedBox" + index)

  if (duration) {
    let oldColor = box.style.color
    setTimeout(() => {
      box.style.backgroundColor = color
      box.style.boxShadow = ""
    }, duration)
  }

  box.style.backgroundColor = color
  box.style.boxShadow = "0 0 10px 10px " + color
}

function setBoxColorAll(color) {
  for (let i = 0; i < boxAmt; i++) {
    setBoxColor(i, color)
  }
}

function addColors(color1, color2){
  let r = Math.floor((color1[0] + color2[0])/2)
  let g = Math.floor((color1[1] + color2[1])/2)
  let b = Math.floor((color1[2] + color2[2])/2)
  return "rgb(" + r + "," + g + "," + b + ")"
}

function init(){
  for (let i = 0; i < boxAmt; i++) {
    let box = makeLedBox(i)
    let body = document.getElementById("container")
    //body.appendChild(box)
  }
}

function ripple(color){
  cssColor = "rgb(" + color[0] + "," + color[1] + "," + color[2] + ")"
  middle = Math.floor(boxAmt/2)
  pos = 0

  id = setInterval(propagate, stepDuration)

  function propagate() {
    if (pos > boxAmt/2) {
      console.log("clearing")
      clearInterval(id)
    }
    pos += 1


    //setBoxColor(middle + pos-1, "white")
    setBoxColor(Math.max(middle, middle + pos - 1), addColors(color, [255, 255, 255]), stepDuration)
    setBoxColor(middle + pos, cssColor, stepDuration)
    setBoxColor(Math.max(middle, middle + pos + 1), addColors(color, [255, 255, 255]), stepDuration)

    //setBoxColor(middle-pos+1, "white")
    setBoxColor(Math.min(middle, middle - pos + 1), addColors(color, [255, 255, 255]), stepDuration)
    setBoxColor(middle-pos, cssColor, stepDuration)
    setBoxColor(Math.min(middle, middle - pos - 1), addColors(color, [255, 255, 255]), stepDuration)
  }
}

function threePulses(){
  let colors = [
    [255,0,0],
    [0,255,0],
    [0,0,255]
  ]
  let index = 0;
  setInterval(() => {

    ripple(colors[index%3])
    index+=1
  }, 4000)
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