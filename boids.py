import Environment
import vector
import math


class boids:
    mass = 1

    # def __init__(self, coord: tuple, angle: int, force: vector):
    def __init__(self, coord: tuple, angle: int):
        self.neighbours = []

        self.coord = coord
        self.angle = angle
        self.force = vector.vector(angle=angle)
        # self.force = force
        pass

    def update(self, neighbours: list, time_delta: float):
        # Assign neighbours
        self.neighbours = neighbours

        self.seperation()
        self.alignment()
        self.cohesion()

        # Calculate new speed
        self.acceleration = self.force / boids.mass
        self.acceleration[1] = self.force[1]  # angles are the same
        self.velocity += self.acceleration * time_delta
        # v_final = v0 + a * t_delta

        # Align boid
        self.angle = self.velocity[1]

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

        x = self.velocity * math.cos(self.angle) * time_diff
        y = self.velocity * math.sin(self.angle) * time_diff

        self.coord = (self.coord + (x, y))
        self.coord = tuple_modulo(self.coord, Environment.max_size)

    def get_coord(self) -> tuple:
        return self.coord

    def get_angle(self) -> int:
        return self.angle
