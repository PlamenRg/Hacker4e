import pygame

pygame.init()
screen = pygame.display.set_mode((720, 480))
done = False
clock = pygame.time.Clock()
x = int(input("x?"))
y = int(input("y?"))
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.draw.rect(screen, (100, 100, 100), pygame.Rect(x, y, 100, 100))
    pygame.display.flip()