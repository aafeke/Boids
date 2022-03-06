class boids:
    def __init__(self, coord: tuple, angle: int, speed: int):
        # set starting angle -> direction boid will travel.
        # set speed? -> distance boid will travel
        # position (x, y) or seperate x / y
        self.coord = coord
        self.angle = angle
        self.neighbour_lst = []
        self.speed = speed
        pass

    def update(self):
        angle_lst = [0, 0, 0]
        speed_lst = [0, 0, 0]
        # calculate the angles
        angle_lst[0], speed_lst[0] = self.seperation()
        angle_lst[1], speed_lst[1] = self.alignment()
        angle_lst[2], speed_lst[2] = self.cohesion()

        self.temp_speed = sum(self.speed_lst)/len(self.speed_lst)
        self.temp_angle = sum(self.angle_lst)/len(self.angle_lst)
        # TODO pre calculate everything but set the action/ new angle
        # the boid wants.

    def step(self, coord=None, angle=None, speed=None):
        # if the environment tells us the action is legal, do it
        # otherwise follow the instructions from the environment.
        self.neighbour_lst = []
        if coord is None and Angle is None and Speed is None:
            # BUG: This might be a bug.
            self.speed = self.temp_speed
            self.angle = self.temp_angle
        else:
            if coord is not None:
                self.coord = coord

            if angle is not None:
                self.angle = angle

            if self.speed is not None:
                self.speed = speed

    def seperation(self):
        # go away from others too close
        # TODO
        pass

    def alignment(self):
        # align with neighbours
        # TODO

        angle_diff = self.angle % 180  # if alone
        for flockmate in self.neighbour_lst:
            angle_diff += flockmate.get_angle() % 180

        angle_diff = angle_diff / len(self.neighbour_lst)
        pass

    def cohesion(self):
        # move to average coordinate of neighbours
        # TODO
        pass

    def add_neighbour(self, neigh):
        self.neighbour_lst.append(neigh)

    def get_coord(self):
        return self.coord

    def set_coord(self, coord):
        self.coord = coord

    def get_angle(self):
        return self.angle

    def set_angle(self, angle):
        self.angle = angle

    def get_speed(self):
        return self.speed

    def set_speed(self, speed):
        self.speed = speed
