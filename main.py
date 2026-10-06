import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Test")

x = 400
y = 300
speed = 5

clock = pygame.time.Clock()

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        y -= speed

    if keys[pygame.K_s]:
        y += speed

    if keys[pygame.K_a]:
        x -= speed

    if keys[pygame.K_d]:
        x += speed

    screen.fill((30, 30, 30))

    pygame.draw.rect(screen, (0, 255, 0), (x, y, 50, 50))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()