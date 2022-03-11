import vector


class boids:
    mass = 1

    def __init__(self, coord: tuple, angle: int, force: vector):
        self.coord = coord
        self.angle = angle
        self.force = force
        pass

    def update(self, neighbours: list):
        self.acceleration = self.force / boids.mass
        self.acceleration[1] = self.force[1]  # angles are the same
        self.velocity += self.acceleration * vector.get_delta()
        # v_final = v0 + a * t_delta
        pass

    def seperation(self, neighbours):
        pass

    def alignment(self, neighbours):
        pass

    def cohesion(self, neighbours):
        pass
