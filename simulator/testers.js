
function beatNodeTester() {
  //init
  let ledCount = 60
  let myBeatLine = new BeatLine(ledCount, [255, 255, 255])

  setInterval(() => {
    myBeatLine.createBeat(4, 15, [0, 0, 255])
  }, 4000)

  setTimeout(() => {
    setInterval(() => {
      setTimeout(() => {
        myBeatLine.createBeat(4, 40, [0, 255, 0])
      }, 0000)
    }, 1000)
  }, 3000)

  setTimeout(() => {
    setInterval(() => {
      setTimeout(() => {
        myBeatLine.createBeat(4, 30, [255, 0, 0])
      }, 0000)
    }, 2000)
  }, 2000)

  //update
  updateLoop = setInterval(() => {
    myBeatLine.update(.01)



    //render
    myBeatLine.render()
  }, 10)
}

function beatLineTester() {
  //init
  let ledCount = 100
  let beatLines = [new BeatLine(ledCount, ledCount, 3, 10)]
  let leds = []
  for (let i = 0; i<ledCount; i++) {
    led = new Led(i, [255, 0, 255])
    leds.push(led)
  }

  //update
  updateLoop = setInterval(() => {
    beatLines.forEach(() => {
      myBeatLine.update(.01)
      myBeatLine.getDistances()
      let thresholdMap = distances.map((distance) => distance < 1)
      for (let i = 0; i < leds.length; i++) {
        if (thresholdMap[i] === true) {

          leds[i].setColor([0,0,255])
        }
        else {
          leds[i].clearColors()
        }
      }
    })

    let distances =

    //render
    leds.forEach((led) => {
      led.render()
    })
  }, 10)
}

function ledTesterCallbacks(){
  let leds = []
  for (let i = 0; i<10; i++) {
    led = new Led(i, [255, 0, 255])
    leds.push(led)
  }

  index1 = 1
  id1 = setInterval(() => {
    console.log("Set colors at " + totalTime)
    leds[index1-1].setColor([0, 255, 0], 1)
    leds[index1].setColor([0, 255, 0], 1)
    leds[index1+1].setColor([0, 255, 0], 1)
    index1++
  }, 1000)

  index2 = 1
  setTimeout(() => {
    id2 = setInterval(() => {
        console.log("Set colors at " + totalTime)
        leds[index2-1].setColor([0, 0, 255], .25)
        leds[index2].setColor([0, 0, 255], .25)
        leds[index2+1].setColor([0, 0, 255], .25)
        index2++
    }, 250)
  }, 2000)

  totalTime += .01
  setInterval(() => {
    totalTime += .01
    leds.forEach((led) => {
      led.update(.01)
      led.render()
    })

    if (index1 >= 9) clearInterval(id1)
    if (index2 >= 9) clearInterval(id2)
  }, 10)
}