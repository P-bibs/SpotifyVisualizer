import board
import neopixel
from Led import Led
from BeatNode import BeatNode

ORDER = neopixel.GRB

class BeatLine:
    def __init__(self, led_count, default_color):
        self.leds = []
        for i in range(led_count):
            self.leds.append(Led(i, default_color))

        self.default_color = default_color

        self.beat_nodes = []
        self.next_key = 1

        self.pixels = neopixel.NeoPixel(board.D18, led_count, auto_write=False, pixel_order=ORDER)

    def _request_key(self):
        self.next_key += 1
        return self.next_key - 1

    def create_beat(self, radius, velocity, color):
        key = self._request_key()
        self.beat_nodes.append(BeatNode(radius, velocity, color, len(self.leds), key))

    def clear(self):
        print("Clearing leds")
        self.beat_nodes = []
        for i in range(len(self.leds)):
                self.pixels[i] = [0, 0, 0]
        self.pixels.show()

    def update(self, dt):
        for led in self.leds:
            led.update(dt)

        for beat_node in self.beat_nodes:
            beat_node.update(dt)
            in_range = beat_node.get_in_range()
            for i in range(len(self.leds)):
                if in_range[i]:
                    self.leds[i].set_color(beat_node.color, 0, beat_node.key)

                else:
                    self.leds[i].clear_colors(beat_node.key)

        for i in range(len(self.beat_nodes)-1, -1, -1):
            if self.beat_nodes[i].alive == False:
                self.beat_nodes.pop(i)


    def render(self):
        if len(self.beat_nodes) == 0:
            for i, led in enumerate(self.leds):
                self.pixels[i] = [0, 0, 0]
        else:
            for i, led in enumerate(self.leds):
                self.pixels[i] = led.render()

        self.pixels.show()