import board
import neopixel
from Led import Led
from BeatNode import BeatNode

ORDER = neopixel.GRB

class BeatLine:
    def __init__(self, ledCount, defaultColor):
        self.leds = []
        for i in range(ledCount):
            self.leds.append(Led(i, defaultColor))

        self.defaultColor = defaultColor

        self.beatNodes = []
        self.nextKey = 1

        self.pixels = neopixel.NeoPixel(board.D18, ledCount, auto_write=False, pixel_order=ORDER)

    def requestKey(self):
        self.nextKey += 1
        return self.nextKey - 1

    def createBeat(self, radius, velocity, color):
        key = self.requestKey()
        self.beatNodes.append(BeatNode(radius, velocity, color, len(self.leds), key))


    def update(self, dt):
        for led in self.leds:
            led.update(dt)

        for beatNode in self.beatNodes:
            beatNode.update(dt)
            inRange = beatNode.getInRange()
            for i in range(len(self.leds)):
                if inRange[i]:
                    self.leds[i].setColor(beatNode.color, 0, beatNode.key)

                else:
                    self.leds[i].clearColors(beatNode.key)

        for i in range(len(self.beatNodes)-1, -1, -1):
            if self.beatNodes[i].alive == False:
                self.beatNodes.pop(i)


    def render(self):
        for i, led in enumerate(self.leds):
            self.pixels[i] = led.render()

        self.pixels.show()