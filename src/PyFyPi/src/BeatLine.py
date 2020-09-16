from .BeatNode import BeatNode
from .Led import Led


class BeatLine:
    def __init__(self, pixels, default_color):
        self.leds = []
        for i in range(len(pixels)):
            self.leds.append(Led(i, default_color))

        self.default_color = default_color

        self.beat_nodes = []
        self.next_key = 1

        self.pixels = pixels

    def _request_key(self):
        self.next_key += 1
        return self.next_key - 1

    def create_beat(self, radius, position, velocity, color):
        if len(self.beat_nodes) > 15:
            self.beat_nodes.pop(0)
        
        key = self._request_key()
        self.beat_nodes.append(BeatNode(radius, position, velocity, color, len(self.leds), key))

    def clear(self):
        print("Clearing leds")
        self.beat_nodes = []
        for i in range(len(self.leds)):
            self.pixels[i] = [0, 0, 0]
            self.leds[i].color_stack = []
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

    def exit(self):
        print("Clearing pixels")
        self.clear()
        print("Pixels cleared")
