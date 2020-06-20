import pygame

pygame.init()
screen = pygame.display.set_mode((720,480))
done = False
is_blue = True
x = 30
y = 30
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue
    if is_blue:
        color = (0,120,255)
    else:
        color = (144, 247, 178)
    pressed = pygame.key.get_pressed()
    if pressed [pygame.K_UP]:
        y = y-3
    if pressed [pygame.K_DOWN]:
        y = y+3
    if pressed [pygame.K_LEFT]:
        x = x-3
    if pressed [pygame.K_RIGHT]:
        x = x+3
    screen.fill((0,0,0))
    pygame.draw.rect(screen, color, pygame.Rect(x,y,60,60))
    pygame.display.flip()
    clock.tick(60)