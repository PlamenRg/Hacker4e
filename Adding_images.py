import pygame

pygame.init()
screen = pygame.display.set_mode((720, 480))
done = False
clock = pygame.time.Clock()
filename = input("filename = ")
image = pygame.image.load(filename)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.blit(image, (100, 100))
    pygame.display.flip()