import math
import functools

class Led:
    def __init__(self, led_id, defaultColor):
        self.led_id = led_id
        self.defaultColor = defaultColor
        self.colorStack = []

    def setColor(self, color, duration, key):
        if (key):
            if True in list(map(lambda item : item['key']==key, self.colorStack)):
                index = list(map(lambda item : item['key']==key, self.colorStack)).index(True)
                self.colorStack[index] = {
                    "color": color,
                    "key": key
                }
            else:
                self.colorStack.append({
                    "color": color,
                    "key": key
                })
        else:
            self.colorStack.append({
                "color": color,
                "duration": duration,
                "ttl": duration,
            })

    def clearColors(self, key):
        for i in range(len(self.colorStack)):
            if (self.colorStack[i]['key'] == key):
                self.colorStack.pop(i)

    def averageColors(self, color1, color2):
        r = math.floor((color1[0] + color2[0])/2)
        g = math.floor((color1[1] + color2[1])/2)
        b = math.floor((color1[2] + color2[2])/2)
        return [r, g, b]

    def update(self, dt):
        pass
        #for color in self.colorStack:
        #    color['ttl'] = color['ttl'] - dt

        # for i in range(len(self.colorStack)-1, -1, -1):
        #     if (self.colorStack[i].ttl < 0):
        #         self.colorStack.pop(i)
        #         print("Popped from loc " + i + " on led " + self.led_id)

    def render(self):

        if len(self.colorStack) == 0:
            color = self.defaultColor
        elif len(self.colorStack) == 1:
            color = self.colorStack[0]['color']
        else:
            colors = list(map(lambda item : item['color'], self.colorStack))
            color = functools.reduce(self.averageColors, colors)

        return color
