import Environment as env
import vector
import math


class boids:
    mass = 1

    # def __init__(self, coord: tuple, angle: int, force: vector):
    def __init__(self, coord: tuple, magnitude: int, angle: int):
        self.neighbours = []

        self.coord = coord
        self.angle = angle
        self.force = vector.vector(param_magnitude=magnitude,
                                   param_angle=angle)
        self.acceleration = vector.vector()
        self.velocity = vector.vector()

        # self.update()
        pass

    def update(self, neighbours: list, time_delta: float):
        # print(time_delta)
        # Assign neighbours
        self.neighbours = neighbours

        self.seperation()
        self.alignment()
        self.cohesion()

        # Calculate new speed
        self.acceleration = self.force / boids.mass
        # a = F / m

        self.velocity += self.acceleration * max(time_delta, 1)
        # v_final = v0 + a * t_delta

        # Align boid
        self.angle = self.velocity.angle

        self.update_coord(time_delta)
        # return

    def seperation(self):
        pass

    def alignment(self):
        pass

    def cohesion(self):
        """GTFO function"""
        pass

    def update_coord(self, time_diff):
        def tuple_modulo(tup1, tup2):
            x = tup1[0] % tup2[0]
            y = tup1[1] % tup2[1]
            return (x, y)
        # (x, y) = self.v * environment * t_delta

        # x_final =  x0 + v * t_delta
        x = self.velocity.magnitude * math.cos(self.velocity.angle) * max(time_diff, 1)
        y = self.velocity.magnitude * math.sin(self.velocity.angle) * max(time_diff, 1)

        print(f"COORDS: {x}, {y} |\
                magnitude: {self.velocity.magnitude} |\
                angle: {self.velocity.angle}")
        self.coord = (self.coord + (x, y))
        self.coord = tuple_modulo(self.coord, env.environment.max_coords)
        # print(f"COORDS: {self.coord}")

    def get_coord(self) -> tuple:
        return self.coord

    def get_angle(self) -> int:
        return self.angle

    def __repr__(self):
        # return f"xy {self.coord} | force: {self.force} | 
        #   acceleratio: {self.acceleration} | velocity: {self.velocity}"
        return f"xy {self.coord}  | velocity: {self.velocity}"