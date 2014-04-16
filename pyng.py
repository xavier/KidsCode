#!/usr/bin/env python
#
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#   It's my first actual game-making attempt. I know code could be much better
#   with classes or defs but I tried to make it short and understandable with very
#   little knowledge of python and pygame(I'm one of them). Enjoy.

import pygame
from pygame.locals import *

pygame.init()

font  = pygame.font.SysFont("calibri", 40)

screen = pygame.display.set_mode((640,480), 0, 32)
pygame.display.set_caption("Pyng!")

#Creating 2 bars, a ball and background.
background = pygame.image.load('back.jpg')

bar1 = pygame.Surface((10,50))
bar1.fill((0,0,255))

bar2 = pygame.Surface((10,50))
bar2.fill((255,0,0))

circle = pygame.Surface((15,15))
pygame.draw.circle(circle, (0,255,0), (15/2,15/2), 15/2)
circle.set_colorkey((0,0,0))

# some definitions
bar1_x, bar2_x               = 10. , 620.
bar1_y, bar2_y               = 215. , 215.
circle_x, circle_y           = 307.5, 232.5
bar1_move, bar2_move         = 0. , 0.
speed_x, speed_y, speed_circ = 250., 250., 250.
bar1_score, bar2_score       = 0,0
pad_speed = 8
time_sec = 0.01


while True:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_q:
                bar1_move = -pad_speed
            elif event.key == K_w:
                bar1_move = pad_speed
            elif event.key == K_UP:
                bar2_move = -pad_speed
            elif event.key == K_DOWN:
                bar2_move = pad_speed
        elif event.type == KEYUP:
            if event.key == K_q:
                bar1_move = 0.
            elif event.key == K_w:
                bar1_move = 0.
            elif event.key == K_UP:
                bar2_move = 0.
            elif event.key == K_DOWN:
                bar2_move = 0.

    score1 = font.render(str(bar1_score), True, (255,255,255))
    score2 = font.render(str(bar2_score), True, (255,255,255))

    screen.blit(background,  (0,0))
    frame = pygame.draw.rect(screen, (255,255,255), Rect((5,5), (630,470)), 2)
    middle_line = pygame.draw.aaline(screen, (255,255,255), (330,5), (330,475))
    screen.blit(bar1, (bar1_x,bar1_y))
    screen.blit(bar2, (bar2_x,bar2_y))
    screen.blit(circle, (circle_x,circle_y))
    screen.blit(score1, (250.,210.))
    screen.blit(score2, (380.,210.))

    bar1_y += bar1_move
    bar2_y += bar2_move

    circle_x += speed_x * time_sec
    circle_y += speed_y * time_sec

    # Put bar to center
    if bar1_y >= 420.: 
        bar1_y = 420.
    elif bar1_y <= 10. : 
        bar1_y = 10.
    
    if bar2_y >= 420.: 
        bar2_y = 420.
    elif bar2_y <= 10.: bar2_y = 10.

    # collision detection
    if circle_x <= bar1_x + 10.:
        if circle_y >= bar1_y - 7.5 and circle_y <= bar1_y + 42.5:
            circle_x = 20.
            speed_x = -speed_x
    if circle_x >= bar2_x - 15.:
        if circle_y >= bar2_y - 7.5 and circle_y <= bar2_y + 42.5:
            circle_x = 605.
            speed_x = -speed_x
    if circle_x < 5.:
        bar2_score += 1
        circle_x, circle_y = 320., 232.5
        bar1_y,bar_2_y = 215., 215.
    elif circle_x > 620.:
        bar1_score += 1
        circle_x, circle_y = 307.5, 232.5
        bar1_y, bar2_y = 215., 215.
    if circle_y <= 10.:
        speed_y = -speed_y
        circle_y = 10.
    elif circle_y >= 457.5:
        speed_y = -speed_y
        circle_y = 457.5

    pygame.display.update()