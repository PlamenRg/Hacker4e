import pygame

x= int(input("start"))
y= int(input("end"))
pygame.init()
screen = pygame.display.set_mode((720, 480))
done = False
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.draw.line(screen, (144, 255, 98), (x, y), (300, 200), 10)
    pygame.display.flip()