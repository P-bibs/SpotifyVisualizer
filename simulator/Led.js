var totalTime = 0

class Led {
  constructor(led_id, defaultColor) {
    this.led_id = led_id
    this.defaultColor = defaultColor
    this.colorStack = []

    var node = document.createElement("div")
    node.setAttribute("id", "Led" + led_id)
    node.setAttribute("class", "LedBox")

    let body = document.getElementById("container")
    body.appendChild(node)
  }

  setColor(color, duration, key){
    if (key) {
      if (this.colorStack.map((item) => item.key===key).includes(true)) {
        let index = this.colorStack.map((item) => item.key===key).indexOf(true)
        this.colorStack[index] = {
          color: color,
          key: key
        }
      }
      else {
        this.colorStack.push({
          color: color,
          key: key
        })
      }
    }
    else {
      this.colorStack.push({
        color: color,
        duration: duration,
        ttl: duration,
      })
    }
  }

  clearColors(key) {
    for (let i = 0; i < this.colorStack.length; i += 1) {
      if (this.colorStack[i].key === key) {
        this.colorStack.splice(i, 1)
      }
    }
  }

  update(dt){
    this.colorStack.forEach((color) => {
      color.ttl -= dt
    })

    for (let i = this.colorStack.length-1; i >= 0; i -= 1){
      if (this.colorStack[i].ttl < 0) {
        this.colorStack.splice(i, 1)
        console.log("Popped from loc " + i + " on led " + this.led_id + " at time " + totalTime)
      }
    }
  }

  render() {
    let box = document.getElementById("Led" + this.led_id)

    let cssColor
    if (this.colorStack.length === 0) {
      cssColor = colorToCss(this.defaultColor)
    }
    else if (this.colorStack.length === 1) {
      cssColor = colorToCss(this.colorStack[0].color)
    }
    else {
      let colors = this.colorStack.map((item) => item.color)
      cssColor = colorToCss(colors.reduce(averageColors))
    }

    box.style.backgroundColor = cssColor
    box.style.boxShadow = "0 0 3px 3px " + cssColor


    let ttl
    if (this.colorStack[this.colorStack.length-1] !== undefined) {
      ttl = this.colorStack[this.colorStack.length-1].ttl
    }
    else {
      ttl = ""
    }
    //box.innerHTML = this.colorStack.length + " " + Math.round(ttl*100)/100
  }
}

function colorToCss(color) {
  return "rgb(" + color[0] + "," + color[1] + "," + color[2] + ")"
}

function averageColors(color1, color2) {
  let r = Math.floor((color1[0] + color2[0])/2)
  let g = Math.floor((color1[1] + color2[1])/2)
  let b = Math.floor((color1[2] + color2[2])/2)
  return [r, g, b]
}
