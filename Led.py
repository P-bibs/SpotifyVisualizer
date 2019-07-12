import functools


class Led():
    """Class that represents an abstracted NeoPixel"""

    def __init__(self, led_id, default_color=(255, 255, 255)):
        self.led_id = led_id
        self.color_stack = []

    def set_color(self, color, duration=0):
        self.color_stack.append({
            "color": color,
            "duration": duration,
            "ttl": duration
        })

    def update(self, dt):
        """Update lifecycle function"""

        for color in self.color_stack:
            color["ttl"] -= dt

        for i in range(len(self.color_stack)-1, 0, -1):
            if self.color_stack[i]["ttl"] < 0:
                print("removing " + str(self.color_stack[i]["color"]))
                self.color_stack.pop(i)

    def get_valid_layers(self):
        validColors = []

        for color in self.color_stack:
            if color["duration"] == color["ttl"]:
                validColors.append(color)
                break
            else:
                validColors.append(color)
        pass

    def combine_colors(self, top_color, bottom_color):
        """Combines two colors taking into acount opacity of top_color"""
        opacity = top_color.ttl/top_color.duration
        r = bottom_color + (top_color.color[0] - bottom_color.color[0])/opacity
        g = bottom_color + (top_color.color[0] - bottom_color.color[0])/opacity
        b = bottom_color + (top_color.color[0] - bottom_color.color[0])/opacity

        return (int(r), int(g), int(b))

    def average_colors_with_opacity(self):
        totalWeight = 0
        r, g, b = 0, 0, 0
        for color in self.color_stack:
            opacity = color["ttl"] / color["duration"]
            r += color["color"][0] * opacity
            g += color["color"][1] * opacity
            b += color["color"][2] * opacity
            totalWeight += opacity

        r = r / totalWeight
        g = g / totalWeight
        b = b / totalWeight
        return (int(r), int(g), int(b))

    def render(self):
        color = functools.reduce(self.combine_colors, self.get_valid_layers())

        # pixels[self.led_id] = self.color_stack[:-1].color
