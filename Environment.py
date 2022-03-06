import boids as boids_lib
from random import uniform
import math
import matplotlib.pyplot as plt
import time


class environment:
    debug = True
    boids_lst = []
    sight_distance = 90
    angle_min_max = (-5, 5)
    # find a set distance a boid can see
    # find a max distance a boid can fly

    def __init__(self, n: int, max_coords: list, speed_settings: list):
        """__init__ Create  environment with N boids

        # min -> 0,0
        # Visualisation of square
        # 0,0           0, x_max
        #
        #
        #
        # 0,y_max       x_max, y_max

        Parameters
        ----------
        n : int
            Amount of Boids randomly initialised in the simulation
        """
        self.max_coords = max_coords

        for _ in range(n):
            # give boids a random location
            rand_cord = (uniform(0, max_coords[0]), uniform(0, max_coords[1]))
            rand_angle = uniform(0, 360)
            rand_speed = uniform(speed_settings[0], speed_settings[1])
            boid = boids_lib.boids(rand_cord, rand_angle, rand_speed)
            self.boids_lst.append(boid)

        # create N amount of agents
        # create a space where they can fly around

        # set upper and lower bounds of the flight zone.
        # (x_max,y_max) or x_max and y_max
        pass

    def gen_next_boid(self, cur_boid: boids_lib, own=False) -> boids_lib:
        """gen_next_boid generator for next boid

        A generator function that loops over every boid
        returns a boid back as a variable

        Parameters
        ----------
        boid : boids_lib
            the current boid
        own : bool, optional
            To give itself back, by default False

        Yields
        ------
        Iterator[boids_lib]
            a boid
        """
        self_index = self.boids_lst.index(cur_boid)
        for next_boid in self.boids_lst[self_index + 1:]:
            yield next_boid

    def step(self):
        for cur_boid in self.boids_lst:
            # This can be done using MP.

            for neighbour_boid in self.gen_next_boid(cur_boid):
                # calculate euclidian distance
                cur_x, cur_y = cur_boid.get_coord()
                nei_x, nei_y = neighbour_boid.get_coord()
                dist = ((cur_x - nei_x) ** 2 + (cur_y - nei_y) ** 2) ** 0.5

                # if in radius of sight.
                if dist <= self.sight_distance:
                    cur_boid.add_neighbour(neighbour_boid)
                    neighbour_boid.add_neighbour(cur_boid)

        # this is the update part

        # explanation:
        # We want to split the update and the step function.
        # otherwise we allow an action and use the performed action for our
        # calculations of the next boid.
        #
        # this can make it so that a bird is outside the X meter sight
        # and still be used for the calculations.
        #
        # It is slower computational wise but this way we won't deal with
        # updates states for older calculations.
        #
        # This can have drastic effects on example Game Of Life,
        # not sure for boids.

        # this is the step / set the action part
        for cur_boid in self.boids_lst:
            # Check if crossing the edge
            self.edge(cur_boid)

        # TODO for every boid, calculate if action is valid
        # if action is not valid, set the boid to a valid spot.
        # otherwise, allow the action of the boid

        # things to check:
        # if speed / size of the step allowed
        # if the angle allowed
        # min speed check
        # is the position allowed [outside grid -> go back inside back]

        pass

    def visualise(self):
        # Circle wont plot without subplot.
        fig, ax = plt.subplots()
        super_debug = True
        for boid in self.boids_lst:
            x, y = boid.get_coord()

            # plot the boid itself
            ax.scatter(x, y, cmap="hsv", marker="D")
            if self.debug and super_debug:
                super_debug = False
                # plot its sight
                circle1 = plt.Circle(
                    (x, y), radius=self.sight_distance,
                    fill=False, color="White"
                )
                ax.add_patch(circle1)

            # plot direction
            angle = boid.get_angle()
            arrow_size = 13
            # polar coordinate system
            new_x = arrow_size * math.cos(angle)
            new_y = arrow_size * math.sin(angle)
            ax.plot((x, x + new_x), (y, y + new_y))

        # plot settings
        ax.set_aspect("equal", adjustable="box")
        plt.style.use("dark_background")
        plt.tight_layout()
        plt.axis("off")
        plt.xlim([0, self.max_coords[0]])
        plt.ylim([0, self.max_coords[1]])
        plt.savefig(f"image_{str(time.time())}.png",
                    bbox_inches="tight", pad_inches=0)

    def edge(self, boid):
        """edge check borders of grid.

        min -> 0,0
        Visualisation of square
        0,0-------------0, x_max
        |               |
        |               |
        |               |
        0,y_max---------x_max, y_max

        The borders are WRAP around, meaning if a boid goes to far
        it wraps back to the other side.

        Parameters
        ----------
        boid : class Boids
            boids class
        """
        coord = boid.get_coord()

        for i in list(range(len(self.max_coords))):
            if coord[i] > self.max_coords[i]:  # above max
                coord[i] = coord[i] - self.max_coords[i]
            elif coord[i] < 0:  # below 0
                coord[i] = self.max_coords[i] - coord[i]

        boid.set_coord(coord)

    def __repr__(self):
        return_str = f"Amount of boids: {len(self.boids_lst)}"
        return return_str


# Create an environment
max_size = (500, 500)
speed_settings = (5, 25)
env = environment(25, max_size, speed_settings)
env.step()
env.visualise()
# print(env)
