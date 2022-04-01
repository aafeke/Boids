import time
import math


class vector:
    def __init__(self, magnitude=0, angle=0):
        # 0 : magnitude
        # 1 : angle (0-359)
        # 2 : x subvector
        # 3 : y subvector
        self.vector = [0, 0, 0, 0]
        self.set_vector(magnitude, angle)

    def set_vector(self, val: float, ang: int):
        if val != 0:   # user input
            self.vector[0] = val
            self.vector[1] = ang
            self.vector[2] = val * math.cos(self.vector[1])
            self.vector[3] = val * math.sin(self.vector[1])
        else:
            self.vector[0] = 0
            self.vector[1] = 0
            self.vector[2] = 0
            self.vector[3] = 0

    def get_delta(self, start_time):
        if self.start_time != 0:
            return time.time() - start_time
        else:
            pass

    def __repr__(self) -> str:
        return f"Mag: {self.vector[0]}, Ang: {self.vector[1]}"

    # if the + sign is used.
    def __add__(self, other):
        x = self.vector[2] + other.vector[2]
        y = self.vector[3] + other.vector[3]

        out_magnitude = (x**2 + y**2) ** (0.5)
        out_angle = math.acos(x/out_magnitude) * 180 / math.pi

        out = vector()
        out.set_vector(out_magnitude, out_angle)
        return out

    def __mult__(self, other):
        pass