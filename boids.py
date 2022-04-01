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
        self.force = vector.vector(magnitude=magnitude, angle=angle)
        self.acceleration = vector.vector()
        self.velocity = vector.vector()

        # self.update()
        pass

    def update(self, neighbours: list, time_delta: float):
        # Assign neighbours
        self.neighbours = neighbours

        self.seperation()
        self.alignment()
        self.cohesion()

        # Calculate new speed
        self.acceleration.vector[0] = self.force.vector[0] / boids.mass
        self.acceleration.vector[1] = self.force.vector[1]  # angles are the same
        self.velocity.vector[0] += self.acceleration.vector[0] * max(time_delta, 0.01) 
        #self.velocity.vector += self.acceleration.vector
        print(time_delta)
        # v_final = v0 + a * t_delta

        # Align boid
        self.angle = self.velocity.vector[1]

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

        x = self.velocity.vector[1] * math.cos(self.velocity.vector[1]) * time_diff
        y = self.velocity.vector[1] * math.sin(self.velocity.vector[1]) * time_diff

        self.coord = (self.coord + (x, y))
        self.coord = tuple_modulo(self.coord, env.environment.max_coords)

    def get_coord(self) -> tuple:
        return self.coord

    def get_angle(self) -> int:
        return self.angle

    def __repr__(self):
        return f"xy {self.coord} | force: {self.force} | acceleratio: {self.acceleration} | velocity: {self.velocity}"