import pygame

pygame.init()
screen = pygame.display.set_mode((720, 480))
done = False
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.draw.rect(screen, (100, 100, 100), pygame.Rect(100, 100, 100, 100))
    pygame.draw.circle(screen , (50, 100, 200), (300, 200), 50)
    pygame.draw.line(screen, (234, 132, 153), (0, 0), (300, 200), 20)
    pygame.display.flip()