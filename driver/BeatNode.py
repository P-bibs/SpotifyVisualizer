class BeatNode:
    def __init__(self, radius, velocity, color, ledCount, key):
        self.radius = radius
        self.velocity = velocity
        self.color = color
        self.ledCount = ledCount
        self.key = key
        self.location = 0
        self.alive = True

    def getInRange(self):
        distances = []
        for i in range(self.ledCount):
            distances.append(abs(self.location-i))
        return map((lambda distance : distance < self.radius), distances)

    def update(self, dt):
        self.location += self.velocity * dt
        if self.location > self.ledCount + self.radius:
            self.alive = False
