import pygame

rgb1 = int(input("rgb1"))
rgb2 = int(input("rgb2"))
rgb3 = int(input("rgb3"))
pygame.init()
screen = pygame.display.set_mode((720, 480))
done = False
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.draw.circle(screen , (rgb1, rgb2, rgb3), (30, 60), 50)
    pygame.display.flip()