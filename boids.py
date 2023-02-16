import vector
import time
import math


class boids:
    # def __init__(self, coord: tuple, angle: int, force: vector):
    def __init__(self, coord: tuple, magnitude: int, angle: int):
        self.max_vel = 10
        self.max_mag = 3

        self.neighbours = set()

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

        self.update(0)  # initial update
        pass

    def update(self, time_delta: float):
        self.seperation()
        self.alignment()
        self.cohesion()

        self.calc(time_delta)
        # return

    def seperation(self):
        def pyth(num1, num2):
            """Pythagoras theory

            Args:
                num1 (float): first number to be squared
                num2 (float): second number to be squared

            Returns:
                float: root square of sum of inputs
            """
            return math.sqrt(num1 * num1 + num2 * num2)

        # TODO: make collision_dist a variable in a global file
        collision_dist = 7

        for other in self.neighbours:

            dx = abs(self.get_coord()[0] - other.get_coord()[0])
            dy = abs(self.get_coord()[1] - other.get_coord()[1])

            distance = pyth(dx, dy)
            if(distance < collision_dist):
                inverse_dist = ((collision_dist - distance) * 5)/collision_dist
                # https://www.desmos.com/calculator/nflz1fbzgb

                # move away
                angle = vector.vector.get_angle(dx, dy, inverse_dist)
                push = vector.vector(inverse_dist,
                                    (angle + 180) % 360)
                self.set_force_v(self.force + push)

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

        # TODO: remove this commented line
        # self.timeout_force() screw you lmao

        # F=m*a, when m=1 => a=F
        self.acc = self.force

        # V = V0 + a * delta_T
        self.vel = self.vel + (self.acc * delta_time)
        self.vel.magnitude = min(self.max_vel,
                                 self.vel.magnitude)

        # Align object
        self.align()

        # Calculate the substitution
        # x = x0 + v * delta_t
        self.coord = (self.coord[0] + self.vel.get_sub_X() * delta_time,
                      self.coord[1] + self.vel.get_sub_Y() * delta_time)

    def get_coord(self) -> tuple:
        return self.coord

    def get_angle(self) -> int:
        return self.angle

    def add_neighbour(self, boid):
        self.neighbours.add(boid)

    def reset_neighbour(self):
        self.neighbours = set()

    def set_force(self, mag, ang):
        self.force.set_vector(mag, ang)
        self.set_counter()

    def set_force_v(self, new_vector: vector.vector):
        new_vector.magnitude = min(new_vector.magnitude,
                                   self.max_mag)
        self.force = new_vector
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
