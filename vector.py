import math


class vector:
    def __init__(self, param_magnitude=0, param_angle=0):
        self.magnitude = 0
        self.angle = 0
        self.set_vector(param_magnitude, param_angle)

    def set_vector(self, mag: 0, ang: 0):
        self.magnitude = mag
        self.angle = ang

    def get_sub_X(self):
        if(self.angle == 0 or self.angle == 360): return 1
        elif(self.angle == 90 or self.angle == 270): return 0
        elif(self.angle == 180): return -1
        else:
            return self.magnitude * math.cos( math.radians(self.angle) )

    def get_sub_Y(self):
        if(self.angle == 0 or self.angle == 360 or self.angle == 180) : return 0
        elif(self.angle == 90): return 1
        elif(self.angle == 270): return -1
        else:
            return self.magnitude * math.sin( math.radians(self.angle) )

    @classmethod
    def __get_angle(cls, x: int, y: int, mag: int):
        if (x >= 0 and y >= 0):
            # area 1
            angle = math.degrees( 0 + math.acos(x/mag) )

        elif (x <= 0 and y >= 0):
            # area 2
            angle = math.degrees( 180 - math.acos(x/mag) )

        elif (x <= 0 and y <= 0):
            # area 3
            angle = math.degrees( 180 + math.acos(x/mag) )

        else:
            # area 4
            angle = math.degrees( 2 * 180 - math.acos(x/mag) )
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

            out_magnitude = (x**2 + y**2) ** (0.5)
            out_angle = vector.__get_angle(x, y, out_magnitude)

            return vector(out_magnitude, out_angle)

    # if the * sign is used.
    def __mul__(self, const: int):
        return vector(self.magnitude * const, self.angle)
    
    def __truediv__(self, const: int):
        return vector(self.magnitude / const, self.angle)