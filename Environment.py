from random import uniform
from PIL import Image
import boids as boids_lib
import matplotlib.pyplot as plt
import math
import time
import glob
import os
import operator


def make_gif(location):
    frames = [Image.open(image) for image in glob.glob(f"{location}//*.PNG")]
    frame_one = frames[0]
    frame_one.save(
        "Boid_gif.gif",
        format="GIF",
        append_images=frames,
        save_all=True,
        duration=100,
        loop=0,
    )


class environment:
    iter_count = 0
    debug = False
    __timer = None
    max_coords = (500, 500)  # temporary workaround

    last_frame_time = time.time()
    boids_lst = []
    sight_distance = 90
    # find a set distance a boid can see
    # find a max distance a boid can fly

    def __init__(self, n: int, max_coords: list, min_max_magn: tuple):
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
        self.min_magn = min_max_magn[0]
        self.max_magn = min_max_magn[1]

        for _ in range(n):
            # give boids a random location

            # add magnitude random generation
            rand_magn = uniform(self.min_magn, self.max_magn)

            rand_cord = (uniform(0, max_coords[0]), uniform(0, max_coords[1]))

            rand_angle = uniform(0, 360)

            boid = boids_lib.boids(rand_cord, rand_magn, rand_angle)
            self.boids_lst.append(boid)

    def __gen_next_boid(self, cur_boid, own=False):
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
        # TODO Find index of current boid
        # start from there.

        for next_boid in self.boids_lst:
            if next_boid == cur_boid:
                continue
            yield next_boid

    def __find_neighbour_boid(self, cur_boid):
        # This can be done using MP.
        neighbour_lst = []
        for neighbour_boid in self.__gen_next_boid(cur_boid):
            # calculate euclidian distance with wrap around
            # https://blog.demofox.org/2017/10/01/calculating-the-distance-between-points-in-wrap-around-toroidal-space/
            cur_x, cur_y = cur_boid.get_coord()
            nei_x, nei_y = neighbour_boid.get_coord()

            dx = abs(cur_x - nei_x)
            dy = abs(cur_y - nei_y)

            if dx > (max_size[0] / 2):
                dx = max_size[0] - dx

            if dy > (max_size[1] / 2):
                dy = max_size[1] - dy

            dist = (dx * dx + dy * dy) ** 0.5

            # if in radius of sight.
            if dist <= self.sight_distance:
                neighbour_lst.append(neighbour_boid)
        return neighbour_lst

    def step(self):
        self.iter_count += 1
        self.last_frame_time = time.time()

        for cur_boid in self.boids_lst:
            # print(cur_boid)
            neighbours = self.__find_neighbour_boid(cur_boid)

            # TODO: add for all neighbours the cur_boid.

            # Pass the neighbours and delta time as parameter
            cur_boid.update(neighbours, (time.time()) - self.last_frame_time)
            # cur_boid.update(neighbours, 1)

            # Redraw boid at the other edge if exceeds
            cur_boid.coord = tuple(map(operator.mod,
                                       cur_boid.coord,
                                       self.max_coords))

    def visualise(self):
        # TODO: replace with pygame.

        # Circle wont plot without subplot.
        fig, ax = plt.subplots()
        for boid in self.boids_lst:
            x, y = boid.get_coord()

            # plot the boid itself
            ax.scatter(x, y, cmap="hsv")
            if self.debug:
                # plot its sight
                circle1 = plt.Circle(
                    (x, y),
                    radius=self.sight_distance,
                    fill=False,
                    color="White"
                )
                ax.add_patch(circle1)

            # plot direction
            angle = boid.get_angle()
            arrow_size = 20
            # polar coordinate system
            new_x = arrow_size * math.cos(math.radians(angle))
            new_y = arrow_size * math.sin(math.radians(angle))
            ax.plot((x, x + new_x), (y, y + new_y))

        # plot settings
        ax.set_aspect("equal", adjustable="box")
        plt.style.use("dark_background")
        plt.tight_layout()
        plt.axis("off")
        plt.xlim([0, self.max_coords[0]])
        plt.ylim([0, self.max_coords[1]])
        plt.savefig(
            f"images//image_{self.iter_count}.png",
        )
        plt.close()

    def __repr__(self):
        return_str = f"Amount of boids: {len(self.boids_lst)}"
        return return_str


if __name__ == "__main__":
    for filename in os.listdir("images"):
        os.remove(f"images\\{filename}")

    for file in os.listdir():
        if file.endswith(".gif"):
            os.remove(file)

    # Create an environment
    max_size = (1000, 1000)
    min_max_magnitude = (5, 5)

    env = environment(1, max_size, min_max_magnitude)
    for i in range(20):
        print(i)
        env.step()
        env.visualise()

    make_gif("images")
