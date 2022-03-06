import vector


class boids:
    mass = 1

    def __init__(self, coord: tuple, angle: int, force: vector):
        self.coord = coord
        self.angle = angle
        self.force = force

        self.delta_start = 0
        pass

    def update(self, neighbours: list):
        self.acceleration = self.force / boids.mass
        self.velocity = self.acceleration * vector.get_time()
        pass

    def seperation(self, neighbours):
        pass

    def alignment(self, neighbours):
        pass

    def cohesion(self, neighbours):
        pass
