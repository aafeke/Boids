class boids:
    def __init__(self, coord: tuple, angle: int):
        # set starting angle -> direction boid will travel.
        # set speed? -> distance boid will travel
        # position (x, y) or seperate x / y
        self.coord = coord
        self.angle = angle
        pass

    def update(self, neighbours: list):
        angle = [0, 0, 0]
        # TODO: find neighbours

        # calculate the angles
        angle[0] = self.seperation(neighbours)
        angle[1] = self.alignment(neighbours)
        angle[2] = self.cohesion(neighbours)
        # set new angle / speed.

    def seperation(self, neighbours):
        pass

    def alignment(self, neighbours):
        pass

    def cohesion(self, neighbours):
        pass

    def get_coord(self):
        return self.coord

    def get_angle(self):
        return self.angle
