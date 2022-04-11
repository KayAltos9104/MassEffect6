import pygame
from Model.characters import Character, Bullet
from Model.physics import *

bullets = []

def shoot (target):
    b = Bullet(hero.Pos, Vector2D.dif(target, hero.Pos))
    bullets.append(b)

BLACK = (0, 0, 0)
LIGHT_BLUE = (66, 170, 255)

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
FPS = 60
cycle_is_running = True

hero = Character(Vector2D(WIDTH//2, HEIGHT//2), 'images/hero.png', 85, 40)

while cycle_is_running:
    hero_direction = Vector2D(0, 0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #pygame.quit()
            #cycle_is_running = False
            exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        hero_direction = Vector2D.sum(hero_direction, Vector2D(-1, 0))
    if keys[pygame.K_RIGHT]:
        hero_direction = Vector2D.sum(hero_direction, Vector2D(1, 0))
    if keys[pygame.K_UP]:
        hero_direction = Vector2D.sum(hero_direction, Vector2D(0, -1))
    if keys[pygame.K_DOWN]:
        hero_direction = Vector2D.sum(hero_direction, Vector2D(0, 1))
    pressed = pygame.mouse.get_pressed()
    m_pos = pygame.mouse.get_pos()
    if pressed[0]:
        shoot(Vector2D(m_pos[0], m_pos[1]))
    screen.fill(LIGHT_BLUE)
    hero.move(hero_direction)
    for b in bullets:
        b.move()
        pygame.draw.circle(screen, BLACK, (b.Pos.x, b.Pos.y), 5)
    screen.blit(hero.sprite.image, hero.collider)
    pygame.display.update()
    clock.tick(FPS)

