import pygame

rgb1 = int(input("rgb1"))
rgb2 = int(input("rgb2"))
rgb3 = int(input("rgb3"))
x= int(input("start"))
y= int(input("end"))
z= int(input("cod1"))
s= int(input("cod2"))
w= int(input("width"))
pygame.init()
screen = pygame.display.set_mode((720, 480))
done = False
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.draw.line(screen, (rgb1, rgb2, rgb3), (x, y), (z, s), w)
    pygame.display.flip()