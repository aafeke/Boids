from PIL import Image
import matplotlib.pyplot as plt
import math
import glob
import os
import time
import vector


class Object():
    # force = vector.vector()
    # acc = vector.vector()
    # vel = vector.vector()

    def __init__(self, mag=5, angle=0, coord=(5, 5), max_coord=(500, 500)):
        self.max_coords = max_coord
        self.acc = vector.vector()
        self.vel = vector.vector()
        self.force = vector.vector()

        self.angle = angle
        self.coord = coord

        self.acc.set_vector(0, 0)
        self.vel.set_vector(0, 0)
        self.force.set_vector(mag, angle)  # Angle 0

        self.counter = time.time()

        self.calc()  # Initially delta is 1

        return

    def calc(self, delta_time=1):  # Delta time will be told by env

        def tuple_modulo(tup1, tup2):
            x = tup1[0] % tup2[0]
            y = tup1[1] % tup2[1]
            return (x, y)

        # Set force to 0 if time treshold exceeded
        self.timeout_force()

        self.acc = self.force  # F=m.a, when m=1 => a=F
        self.vel = self.vel + (self.acc * delta_time)  # V = V0 + a * delta_T

        # Align object
        self.align()

        # Calculate the substitution
        # x = x0 + v * delta_t

        self.coord = (self.vel.get_sub_X() * delta_time + self.coord[0],
                      self.vel.get_sub_Y() * delta_time + self.coord[1])

        self.coord = tuple_modulo(self.coord, self.max_coords)
        return

    def get_coord(self):
        # print(self.coord)
        return self.coord

    def get_angle(self):
        return self.angle

    def set_force(self, mag, ang):
        self.force.set_vector(mag, ang)
        self.set_counter()

    def set_counter(self):
        self.counter = time.time()
        pass

    def timeout_force(self):
        if time.time() - self.counter >= 0.3:
            self.force.set_vector(0, 0)

    def align(self):
        self.angle = self.vel.angle


class environment:
    def __init__(self, n: int, max_coords: list, min_max_magn: tuple):
        self.max_coords = max_coords
        self.min_magn = min_max_magn[0]
        self.max_magn = min_max_magn[1]
        self.iter_count = 0

        magnitude = 5
        new_coords = (max_coords[0]/2,
                      max_coords[1]/2)

        angle = 0
        self.test_object = Object(mag=magnitude,
                                  coord=new_coords,
                                  angle=angle,
                                  max_coord=max_coords)

    def step(self):
        self.iter_count += 1
        self.test_object.calc()

    def visualise(self):
        fig, ax = plt.subplots()

        x, y = self.test_object.get_coord()

        ax.scatter(x, y, cmap="hsv")

        # plot direction
        angle = self.test_object.get_angle()
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
        plt.savefig(
            f"images//image_{self.iter_count}.png",
            bbox_inches='tight',
            pad_inches=0
            )
        
        plt.close()


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


if __name__ == "__main__":
    for filename in os.listdir("images"):
        os.remove(f"images\\{filename}")

    for file in os.listdir():
        if file.endswith(".gif"):
            os.remove(file)

    # Create an environment
    max_size = (500, 500)
    min_max_magnitude = (5, 5)

    env = environment(1, max_size, min_max_magnitude)

    # iterate 20 steps
    for i in range(20):
        print(i, end="\r")
        env.step()
        env.visualise()

    make_gif("images")
