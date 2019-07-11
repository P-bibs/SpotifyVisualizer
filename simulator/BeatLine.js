class BeatLine {
  constructor(ledCount, defaultColor){
    this.leds = []
    for (let i = 0; i < ledCount; i +=1 ) {
      this.leds.push(new Led(i, defaultColor))
    }
    this.defaultColor = defaultColor

    this.beatNodes = []
    this.nextKey = 1

  }

  requestKey() {
    console.log("pulled key " + this.nextKey)
    this.nextKey += 1
    return this.nextKey - 1
  }

  getDistances() {
    let distances = []
    for (let i = 0; i < this.nodes; i++) {
      let nodeLocation = (this.length/this.nodes)*i
      distances.push(Math.abs(this.location-nodeLocation))
    }
    return distances
  }

  createBeat(radius, velocity, color) {
    let key = this.requestKey()
    this.beatNodes.push(new BeatNode(radius, velocity, color, this.leds.length, key))
  }

  update(dt) {
    this.leds.forEach((led) => {
      led.update(dt)
    })
    this.beatNodes.forEach((beatNode) => {
      beatNode.update(dt)
      let inRange = beatNode.getInRange()
      for (let i = 0; i < this.leds.length; i += 1) {
        if (inRange[i]) {
          this.leds[i].setColor(beatNode.color, 0, beatNode.key)
        }
        else {
          this.leds[i].clearColors(beatNode.key)
        }
      }
    })

    for (let i = this.beatNodes.length-1; i >= 0; i -= 1) {
      if (this.beatNodes[i].alive === false) {
        this.beatNodes.splice(i, 1)
      }
    }
  }

  render() {
    this.leds.forEach((led) => {
      led.render()
    })
  }
}