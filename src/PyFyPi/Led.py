import math
import functools

class Led:
    def __init__(self, led_id, default_color):
        self.led_id = led_id
        self.default_color = default_color
        self.color_stack = []

    def set_color(self, color, duration, key):
        if (key):
            if True in list(map(lambda item : item['key']==key, self.color_stack)):
                index = list(map(lambda item : item['key']==key, self.color_stack)).index(True)
                self.color_stack[index] = {
                    "color": color,
                    "key": key
                }
            else:
                self.color_stack.append({
                    "color": color,
                    "key": key
                })
        else:
            self.color_stack.append({
                "color": color,
                "duration": duration,
                "ttl": duration,
            })

    def clear_colors(self, key):
        for i in range(len(self.color_stack)-1, -1, -1):
            if (self.color_stack[i]['key'] == key):
                self.color_stack.pop(i)

    def average_colors(self, color1, color2):
        r = math.floor((color1[0] + color2[0])/2)
        g = math.floor((color1[1] + color2[1])/2)
        b = math.floor((color1[2] + color2[2])/2)
        return [r, g, b]

    def update(self, dt):
        pass
        #for color in self.color_stack:
        #    color['ttl'] = color['ttl'] - dt

        # for i in range(len(self.color_stack)-1, -1, -1):
        #     if (self.color_stack[i].ttl < 0):
        #         self.color_stack.pop(i)
        #         print("Popped from loc " + i + " on led " + self.led_id)

    def render(self):

        if len(self.color_stack) == 0:
            color = self.default_color
        elif len(self.color_stack) == 1:
            color = self.color_stack[0]['color']
        else:
            colors = list(map(lambda item : item['color'], self.color_stack))
            color = functools.reduce(self.average_colors, colors)

        return color
