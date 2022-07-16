from random import randint, uniform
from PIL import Image
import boids as boids_lib
import matplotlib.pyplot as plt
import math
import time
import glob
import os
import operator
import pygame
import random

# SOME GLOBAL STUFF
max_vel = 10
max_mag = 3
#  ---------------


def make_gif(location):
    frames = [Image.open(image) for image in glob.glob(f"{location}/*.png")]
    frame_one = frames[0]
    frame_one.save(
        "Boid_gif.gif",
        format="GIF",
        append_images=frames,
        save_all=True,
        duration=50,
        loop=0,
    )


class environment:
    iter_count = 0
    debug = False
    __timer = None

    # TODO: make max_coords a variable in a global file
    max_coords = (500, 500)  # temporary workaround

    last_frame_time = time.time()
    boids_lst = []

    # TODO: make sight_distance a variable in a global file
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

    def __find_neighbour_boid(self, cur_boid):
        next_boids_lst = self.boids_lst.index(cur_boid)
        for neighbour_boid in self.boids_lst[next_boids_lst:]:
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
                cur_boid.add_neighbour(neighbour_boid)
                neighbour_boid.add_neighbour(cur_boid)

    def step(self):
        self.iter_count += 1
        self.last_frame_time = time.time()

        for boid in self.boids_lst:
            boid.reset_neighbour()

        for cur_boid in self.boids_lst:
            self.__find_neighbour_boid(cur_boid)

            # Pass the neighbours and delta time as parameter
            cur_boid.update(time.time() - self.last_frame_time)

            # Redraw boid at the other edge if exceeds
            cur_boid.coord = tuple(map(operator.mod,
                                       cur_boid.coord,
                                       self.max_coords))

    def __repr__(self):
        return_str = f"Amount of boids: {len(self.boids_lst)}"
        return return_str


if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))

    for filename in os.listdir(f"{dir_path}/images"):
        if filename is not None:
            os.remove(f"{dir_path}/images/{filename}")

    for file in os.listdir(f"{dir_path}"):
        if file.endswith(".gif"):
            os.remove(file)

    # size of visualisation
    screen_size = (750, 750)

    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode(screen_size)
    clock = pygame.time.Clock()

    # Create an environment
    # TODO: make boid_amount a variable in a global file
    boid_amount = 50

    # TODO: make max_size a variable in a global file
    max_size = (1000, 1000)

    # TODO: make min_max_magnitude a variable in a global file
    min_max_magnitude = (5, 5)

    env = environment(boid_amount,
                      max_size,
                      min_max_magnitude)
    try:
        # main loop
        image_counter = -1
        while True:
            image_counter += 1
            print(image_counter)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    raise KeyboardInterrupt


            env.step()
            # make new layer
            surf1 = pygame.Surface(max_size)

            # set background colour
            surf1.fill((0, 0, 0))

            # for every boid
            for boid in env.boids_lst:
                x, y = boid.get_coord()

                # Generate random colour
                rgb = (randint(0, 255), randint(0, 255), randint(0, 255))

                # draw boid itself
                pygame.draw.circle(surf1,               # surface to draw on
                                   rgb,                 # colour
                                   (x, y),              # coordinate
                                   5)                   # size

                # draw direction
                angle = boid.get_angle()
                arrow_size = 20
                new_x = arrow_size * math.cos(math.radians(angle))
                new_y = arrow_size * math.sin(math.radians(angle))
                pygame.draw.line(surf1, rgb,
                                 (x, y),
                                 (x + new_x, y + new_y),
                                 3)

            # Scale the grid to the size of the screen
            scaled_surface = pygame.transform.scale(surf1, screen_size)

            # flip screen
            scaled_surface = pygame.transform.flip(scaled_surface, False, True)

            pygame.image.save(scaled_surface,
                              f"images/image_{image_counter}.png")

            # draw screen
            screen.blit(scaled_surface, (0, 0))

            # show screen'
            pygame.display.update()

            # time.sleep
            # pygame.time.wait(50)

    except KeyboardInterrupt:
        make_gif(f"{dir_path}/images/")
        exit(0)
