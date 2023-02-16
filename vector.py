import math


class vector:
    zero_precision = 10*(10**-10)

    def __init__(self, param_magnitude=0, param_angle=0):
        self.magnitude = 0
        self.angle = 0
        self.set_vector(param_magnitude, param_angle)

    def set_vector(self, mag: 0, ang: 0):
        self.magnitude = mag
        self.angle = ang

    def get_sub_X(self) -> int:
        """
        Returns the x-axis component vector's magnitude
        """
        val = math.cos(math.radians(self.angle))

        if abs(val) < self.zero_precision:
            return 0

        return self.magnitude * val

    def get_sub_Y(self) -> int:
        """
        Returns the y-axis component vector's magnitude
        """
        val = math.sin(math.radians(self.angle))

        if abs(val) < self.zero_precision:
            return 0

        return self.magnitude * val

    @classmethod
    def get_angle(cls, x: int, y: int, mag: int):
        # print(x, y)
        if mag == 0:
            return 0

        elif y >= 0:
            # quadrant 1 & 2
            angle = math.degrees(math.acos(x / mag))

        else:
            # quadrant 3 & 4
            angle = math.degrees(2 * math.pi - math.acos(x / mag))
        return angle

    def __repr__(self) -> str:
        return f"Mag: {self.magnitude}, Ang: {self.angle}"

    # if the + sign is used.
    def __add__(self, other, tup: tuple = None):
        if tup is not None:
            return (tup[0] * self.mag, tup[1] * self.mag)
        else:
            self_x = self.get_sub_X()
            self_y = self.get_sub_Y()

            other_x = other.get_sub_X()
            other_y = other.get_sub_Y()
            x = self_x + other_x
            y = self_y + other_y

            out_magnitude = (x ** 2 + y ** 2) ** (0.5)
            out_angle = vector.get_angle(x, y, out_magnitude)

            return vector(out_magnitude, out_angle)

        
    # if the * sign is used.
    def __mul__(self, const: int):
        return vector(self.magnitude * const, self.angle)

    def __truediv__(self, const: int):
        return vector(self.magnitude / const, self.angle)
