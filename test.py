class CelestialBody:
    """Represents a celestial body"""
    def __init__(self, name, diameter, distance, moons):
        self.name = name
        self.diameter = diameter
        self.distance = distance
        self.moons = moons
        
    @classmethod
    def make_earth(cls):
        return CelestialBody("Earth", 12756.3, 149600000, 1)

    @staticmethod
    def closer_to_sun(body1, body2):
        """Returns the name of the body
        that is closest to the sun"""
        if body1.distance < body2.distance:
            return body1.name
        else:
            return body2.name

a = CelestialBody.make_earth()
b = CelestialBody.make_earth()
print(CelestialBody.closer_to_sun(a, b))