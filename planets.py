# Here are a class Planet and a few instances of that class:
# Match the attributes and their values. Take into account that one option is extra.

class Planet:
    all_moons = []

    def __init__(self, name):
        self.name = name
        self.moons = []


earth = Planet("Earth")
jupiter = Planet("Jupiter")

earth.moons.append("Moon")
earth.all_moons.append("Moon")

jupiter.moons.append("Io")
jupiter.moons.append("Europa")
jupiter.all_moons.append("Io")

print(Planet.all_moons)
print(earth.moons)
print(jupiter.moons)