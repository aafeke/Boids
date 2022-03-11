import vector


class boids:
    mass = 1

    # def __init__(self, coord: tuple, angle: int, force: vector):
    def __init__(self, coord: tuple, angle: int):
        self.neighbours = []

        self.coord = coord
        self.angle = angle
        self.force = vector.vector()
        # self.force = force
        pass

    def update(self, neighbours: list):
        # Assign neighbours
        # self.seperation(neighbours)
        # self.alignment(neighbours)
        # self.cohesion(neighbours)

        self.neighbours = neighbours

        # Calculate new speed
        self.acceleration = self.force / boids.mass
        self.acceleration[1] = self.force[1]  # angles are the same
        self.velocity += self.acceleration * vector.get_delta()
        # v_final = v0 + a * t_delta

        # Align boid
        self.angle = self.velocity[1]
        pass

    def seperation(self, neighbours):
        pass

    def alignment(self, neighbours):
        pass

    def cohesion(self, neighbours):
        """GTFO function"""
        pass

    def get_coord(self):
        return self.coord

    def get_angle(self):
        return self.angle
