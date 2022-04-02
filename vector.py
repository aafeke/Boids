import math


class vector:
    def __init__(self, param_magnitude=0, param_angle=0):
        
        self.magnitude = 0
        self.angle = 0
        self.set_vector(param_magnitude, param_angle)

    def set_vector(self, mag: 0, ang: 0):
        self.magnitude = mag
        self.angle = ang

    def __repr__(self) -> str:
        return f"Mag: {self.magnitude}, Ang: {self.angle}"

    # if the + sign is used.
    def __add__(self, other):
        self_x = self.magnitude * math.cos(self.angle)
        self_y = self.magnitude * math.sin(self.angle)

        other_x = other.magnitude * math.cos(other.angle)
        other_y = other.magnitude * math.sin(other.angle)
        x = self_x + other_x
        y = self_y + other_y

        out_magnitude = (x**2 + y**2) ** (0.5)
        out_angle = math.acos(x/out_magnitude) * 180 / math.pi

        return vector(out_magnitude, out_angle)

    # if the * sign is used.
    def __mul__(self, const: int):
        return vector(self.magnitude * const, self.angle)
    
    def __truediv__(self, const: int):
        return vector(self.magnitude / const, self.angle)