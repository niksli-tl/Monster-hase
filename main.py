import pygame
from pygame import *


FPS = 60
x1 = 150
y1 = 250
x2 = 550
y2 = 250
clock = time.Clock()
window = display.set_mode((700,500))
display.set_caption("Monster Chase")
background = transform.scale(image.load("images/starfield2.png"),(700,500))
sprite1 = transform.scale(image.load("images/sprite1.png"),(50,50))
sprite2 = transform.scale(image.load("images/sprite2.png"),(50,50))


def do_squares_overlap(x1, y1, x2, y2, side=50):
    if x1 + side <= x2 or x2 + side <= x1:
        return False
    if y1 + side <= y2 or y2 + side <= y1:
        return False

    return True

pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)
text_surface = my_font.render("You've been caught up, restart", False, (255, 255, 255))
reset_time = 0
game_reset = False
game = True
while game:
    window.blit(background,(0,0))
    if game_reset:
        reset_time += 1
        x1 = 150
        y1 = 250
        x2 = 550
        y2 = 250
        window.blit(text_surface, (100,220))
        if reset_time == 90:
            game_reset = False
            reset_time = 0
    else:
        window.blit(sprite1,(x1,y1))
        window.blit(sprite2,(x2,y2))
        keys_pressed = key.get_pressed()
        for e in event.get():
            if e.type == QUIT:
                game = False
        if keys_pressed[K_UP] and y2 > 0:
            y2 -= 10
        if keys_pressed[K_DOWN] and y2 < 450:
            y2 += 10
        if keys_pressed[K_LEFT] and x2 > 0:
            x2 -= 10
        if keys_pressed[K_RIGHT] and x2 < 650:
            x2 += 10
        if keys_pressed[K_w] and y1 > 0:
            y1 -= 10
        if keys_pressed[K_s] and y1 < 450:
            y1 += 10
        if keys_pressed[K_a] and x1 > 0:
            x1 -= 10
        if keys_pressed[K_d] and x1 < 650:
            x1 += 10
        if do_squares_overlap(x1,y1,x2,y2):
            game_reset = True


    clock.tick(FPS)
    display.update()


