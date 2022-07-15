import time
import vector
import operator
import pygame


class Object():

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

    def calc(self, delta_time=1) -> None:  # Delta time will be told by env

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

        self.coord = tuple(map(operator.mod,
                               self.coord,
                               self.max_coords))

        return

    def get_coord(self):
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

        angle = int(input("how many degrees?\n"))
        self.test_object = Object(mag=magnitude,
                                  coord=new_coords,
                                  angle=angle,
                                  max_coord=max_coords)

    def step(self):
        self.iter_count += 1
        self.test_object.calc()
        # x, y = self.test_object.get_coord()
        # print(f"X: {x}, Y: {y}, Ang: {self.test_object.vel.angle}")

    def visualise(self):
        # TODO: return a surface for pygame
        pass


if __name__ == "__main__":
    pygame.init()

    # Enviroment variables
    n = 500
    canvas_size = (1000, 1000)
    screen_size = (750, 750)
    min_max_magnitude = (5, 5)

    # Make screen
    screen = pygame.display.set_mode(screen_size)

    env = environment(1, canvas_size, min_max_magnitude)

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        env.step()

        # Make surface
        surf1 = pygame.Surface(canvas_size)

        # make background
        surf1.fill((0, 0, 0))

        pygame.draw.circle(surf1,                       # Surface to draw on
                           (255, 255, 255),             # colour
                           env.test_object.coord,       # coordinate
                           3)                           # size
        # TODO: replace circle with actual sprite

        # Scale the grid to the size of the screen
        scaled_surface = pygame.transform.scale(surf1, screen_size)

        # flip screen
        scaled_surface = pygame.transform.flip(scaled_surface, False, True)

        # Draw screen?
        screen.blit(scaled_surface, (0, 0))

        # Show screen
        pygame.display.update()

        # FIXME
        # time.sleep 100 MS
        pygame.time.wait(50)

        # Get FPS
        # clock.tick()
        # print(clock.get_fps())
