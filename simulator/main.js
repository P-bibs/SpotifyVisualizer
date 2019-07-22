var boxAmt = 21
var stepDuration = 1000

function init(){
  for (let i = 0; i < boxAmt; i++) {
    let box = makeLedBox(i)
    let body = document.getElementById("container")
    //body.appendChild(box)
  }
}

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
