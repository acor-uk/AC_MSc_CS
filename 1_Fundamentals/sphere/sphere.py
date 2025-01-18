import math as m

class sphere:
    def __init__(self, radius):
        self.radius = radius
        self.circumference = 2 * m.pi * radius
        self.surface_area = 4 * (m.pi * (radius ** 2))
        self.volume = 4/3 * (m.pi * (radius ** 3))

    def __str__(self):
        f_radius = format(self.radius, '.2f')
        f_circumference = format(self.circumference, '.2f')
        f_surface_area = format(self.surface_area, '.2f')
        f_volume = format(self.volume, '.2f')
        return f"\nSphere VALUES:\nRadius: {f_radius}\nCircumference: {f_circumference}\nSurface Area: {f_surface_area}\nVolume: {f_volume}"