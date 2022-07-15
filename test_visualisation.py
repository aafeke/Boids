import numpy as np
import random
import pygame
# import operator

n = 500
canvas_size = (1000, 1000)
screen_size = (750, 750)

# mimicks a group of boids
random_points = np.array(
    [(random.randint(0, canvas_size[0]),
      random.randint(0, canvas_size[1])) for _ in range(n)]
)


# mimicks a group of boids movement
def add_movement(array):
    for count, i in enumerate(array):
        x, y = i

        # randomly add values
        x += random.randint(-2, 2)
        y += random.randint(-2, 2)

        # check if in bounds
        if x > canvas_size[0]:
            x = canvas_size[0]
        elif x < 0:
            x = 0

        # check if in bounds
        if y > canvas_size[1]:
            y = canvas_size[1]
        elif y < 0:
            y = 0

        # overwrite new value
        array[count] = (x, y)
    return array


# # main loop
pygame.init()
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    random_points = add_movement(random_points)
    surf1 = pygame.Surface(canvas_size)
    surf1.fill((0, 0, 0))

    for boid_coord in random_points:
        # boid_coord_plus1 = tuple(map(operator.add,
        #                              boid_coord,
        #                              (1, 1)))

        pygame.draw.circle(surf1, (255, 255, 255), boid_coord, 1)
        # pygame.draw.line(surf1, (255, 255, 255),
        #                   boid_coord, boid_coord_plus1, 1)
        # line(surface, color, start_pos, end_pos, width=1)

    scaled_surface = pygame.transform.scale(surf1, screen_size)
    screen.blit(scaled_surface, (0, 0))
    pygame.display.update()
    clock.tick()
    # print(clock.get_fps())
