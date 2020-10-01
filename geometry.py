class Sphere:
    pi = 3.1415

    def __init__(self, radius, volume):
        self.radius = radius
        self.volume = 4 * Sphere.PI * self.radius * self.radius * self.radius / 3

