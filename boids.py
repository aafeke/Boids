import vector
import time


class boids:
    # def __init__(self, coord: tuple, angle: int, force: vector):
    def __init__(self, coord: tuple, magnitude: int, angle: int):
        print(f"param_magnitude {magnitude} |  param_angle {angle}")
        self.neighbours = []

        self.mass = 1

        self.acc = vector.vector()
        self.vel = vector.vector()
        self.force = vector.vector()

        self.angle = angle
        self.coord = coord

        self.acc.set_vector(0, 0)
        self.vel.set_vector(0, 0)
        self.force.set_vector(magnitude, angle)

        self.counter = time.time()

        self.update([], 0)  # initial update
        pass

    def update(self, neighbours: list, time_delta: float):
        # Assign neighbours
        self.neighbours = neighbours

        self.seperation()
        self.alignment()
        self.cohesion()

        self.calc(time_delta)
        # return

    def seperation(self):
        """GTFO togeher function"""
        pass

    def alignment(self):
        """All togeher function"""
        pass

    def cohesion(self):
        """GTFO 2 function"""
        pass

    def calc(self, delta_time):
        # debug
        delta_time = 1

        # Set force to 0 if time treshold exceeded
        self.timeout_force()

        self.acc = self.force  # F=m.a, when m=1 => a=F
        self.vel = self.vel + (self.acc * delta_time)  # V = V0 + a * delta_T

        # Align object
        self.align()

        # Calculate the substitution
        # x = x0 + v * delta_t

        self.coord = (self.vel.get_sub_X() * delta_time + self.coord[0],
                      self.vel.get_sub_Y() * delta_time + self.coord[1])

    def get_coord(self) -> tuple:
        return self.coord

    def get_angle(self) -> int:
        return self.angle

    def set_force(self, mag, ang):
        self.force.set_vector(mag, ang)
        self.set_counter()

    def set_counter(self):
        self.counter = time.time()
        pass

    def timeout_force(self):
        if time.time() - self.counter >= 0.3:
            self.force.set_vector(0, 0)

    def align(self):
        self.angle = self.vel.angle

    def __repr__(self):
        # return f"xy {self.coord} | force: {self.force} |
        #   acceleratio: {self.acceleration} | velocity: {self.velocity}"
        return f"xy {self.coord}  | velocity: {self.velocity}"
