class BeatNode {
  constructor(radius, velocity, color, ledCount, key) {
    this.radius = radius
    this.velocity = velocity
    this.color = color
    this.ledCount = ledCount
    this.key = key
    this.location = 0
    this.alive = true
  }

  getInRange() {
    let distances = []
    for (let i = 0; i < this.ledCount; i ++) {
      distances.push(Math.abs(this.location-i))
    }

    return distances.map((distance) => distance < this.radius)
  }

  update(dt) {
    this.location += this.velocity * dt
    if (this.location > this.ledCount + this.radius) {
      this.alive = false
    }
  }



}