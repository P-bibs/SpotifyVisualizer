class BeatNode:
    def __init__(self, radius, velocity, color, led_count, key):
        self.radius = radius
        self.velocity = velocity
        self.color = color
        self.led_count = led_count
        self.key = key
        self.location = 0
        self.alive = True

    def get_in_range(self):
        distances = []
        for i in range(self.led_count):
            distances.append(abs(self.location-i))
        return list(map((lambda distance : distance < self.radius), distances))

    def update(self, dt):
        self.location += self.velocity * dt
        if self.location > self.led_count + self.radius:
            self.alive = False
