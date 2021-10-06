import pygame
import random

pygame.init()

def draw_eye(x, y, w, h, surface, color):
    dx = x - (w/2) # in the middle
    dy = y - h
    pygame.draw.rect(surface, color, pygame.Rect(dx, dy, w, h),  0, 20)

surface_w = 800
surface_h = 600
surface_mid_x = surface_w/2
surface_mid_y = surface_h/2

eye_w = 60
eye_h = 120
eye_sep = 50
eye_h_mult = 1.0

eye_baseline_y = surface_mid_y + (eye_h/2)

surface = pygame.display.set_mode([800, 600])
color = (255, 255, 255)
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # left
    eye_lx = surface_mid_x - eye_sep
    eye_ly = eye_baseline_y
    draw_eye(eye_lx, eye_ly, eye_w, eye_h, surface, color)

    # right
    eye_rx = surface_mid_x + eye_sep
    eye_ry = eye_baseline_y
    draw_eye(eye_rx, eye_ry, eye_w, eye_h, surface, color)

    pygame.display.flip()

pygame.quit()