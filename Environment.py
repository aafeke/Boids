import boids
# from random import uniform
import math
import matplotlib.pyplot as plt
import time
# import vector


class environment:

    debug = True
    boids_lst = []
    sight_distance = 90
    # find a set distance a boid can see
    # find a max distance a boid can fly

    def __init__(self, n: int, max_coords: list):
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

        # for _ in range(n):
        #     give boids a random location

        #     TODO: CHANGE THESE TO A RANDOM VECTOR
        #     rand_cord = (uniform(0,max_coords[0]), uniform(0, max_coords[1]))
        #     rand_angle = uniform(0, 360)
        #     boid = boids.boids(rand_cord, rand_angle)

        #     self.boids_lst.append(boid)

        # create N amount of agents
        # create a space where they can fly around

        # set upper and lower bounds of the flight zone.
        # (x_max,y_max) or x_max and y_max
        pass

    def gen_next_boid(self, cur_boid: boids, own=False) -> boids:
        """gen_next_boid generator for next boid

        A generator function that loops over every boid
        returns a boid back as a variable

        Parameters
        ----------
        boid : boids
            the current boid
        own : bool, optional
            To give itself back, by default False

        Yields
        ------
        Iterator[boids]
            a boid
        """
        for next_boid in self.boids_lst:
            if next_boid == cur_boid:
                continue
            yield next_boid

    def step(self):
        for cur_boid in self.boids_lst:
            # This can be done using MP.

            neighbour_lst = []
            for neighbour_boid in self.gen_next_boid(cur_boid):

                # calculate euclidian distance
                cur_x, cur_y = cur_boid.get_coord()
                nei_x, nei_y = neighbour_boid.get_coord()
                dist = ((cur_x - nei_x) ** 2 + (cur_y - nei_y) ** 2) ** 0.5

                # if in radius of sight.
                if dist <= self.sight_distance:
                    neighbour_lst.append(neighbour_boid)

            print(len(neighbour_lst))
            break

        # call the update function in boid at the end
        # apply the actions the environment
        # If action is valid
        # If not set the boid in a different position.
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
        plt.savefig(f"images/image_{str(time.time())}.png",
                    bbox_inches="tight", pad_inches=0)

    def __repr__(self):
        return_str = f"Amount of boids: {len(self.boids_lst)}"
        return return_str


# Create an environment
# max_size = (500, 500)
# env = environment(25, max_size)
# env.step()
# env.visualise()
# print(env)
