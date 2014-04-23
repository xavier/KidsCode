#!/usr/bin/env python

import pygame
from pygame.locals import *

pygame.init()

font            = pygame.font.SysFont("calibri", 40)

blue            = (0,0,255)
red             = (255,0,0)
green           = (0,255,0)
white           = (255,225,255)
black           = (0,0,0)

bat_center_y    = 215.0
bat_up_limit    = 10.0
bat_down_limit  = 420.0
ball_up_limit   = 10.0
ball_down_limit = 457.5
left_limit      = 10.0
rigth_limit     = 620


screen = pygame.display.set_mode((640,480), 0, 32)
pygame.display.set_caption("Pyng!")

background = pygame.image.load("back.jpg")

bat_left       = pygame.Surface((10,50))
bat_left.fill(blue)
bat_left_x     = left_limit
bat_left_y     = bat_center_y
bat_left_move  = 0.0
bat_left_score = 0

bat_right       = pygame.Surface((10,50))
bat_right.fill(red)
bat_right_x     = rigth_limit
bat_right_y     = bat_center_y
bat_right_move  = 0.0
bat_right_score = 0

ball     = pygame.Surface((15,15))
pygame.draw.circle(ball, green, (15/2,15/2), 15/2)
ball.set_colorkey(black)
ball_x   = 307.5
ball_y   = 232.5

ball_speed_x = 250.0
ball_speed_y = 250.0
ball_speed   = 250.0

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_q:
                bat_left_move = -pad_speed
            elif event.key == K_a:
                bat_left_move = pad_speed
            elif event.key == K_UP:
                bat_right_move = -pad_speed
            elif event.key == K_DOWN:
                bat_right_move = pad_speed
        elif event.type == KEYUP:
            if event.key == K_q:
                bat_left_move = 0.0
            elif event.key == K_a:
                bat_left_move = 0.0
            elif event.key == K_UP:
                bat_right_move = 0.0
            elif event.key == K_DOWN:
                bat_right_move = 0.0

    screen.blit(background,  (0,0))
    frame = pygame.draw.rect(screen, white, Rect((5,5), (630,470)), 2)
    middle_line = pygame.draw.aaline(screen, white, (330,5), (330,475))

    score1 = font.render(str(bat_left_score), True, white)
    score2 = font.render(str(bat_right_score), True, white)
    screen.blit(score1, (250.0,210.0))
    screen.blit(score2, (380.0,210.0))
    
    bat_left_y += bat_left_move
    if bat_left_y >= bat_down_limit: 
        bat_left_y = bat_down_limit
    elif bat_left_y <= bat_up_limit : 
        bat_left_y = bat_up_limit
    screen.blit(bat_left, (bat_left_x, bat_left_y))

    bat_right_y += bat_right_move
    if bat_right_y >= bat_down_limit: 
        bat_right_y = bat_down_limit
    elif bat_right_y <= bat_up_limit:
        bat_right_y = bat_up_limit
    screen.blit(bat_right, (bat_right_x, bat_right_y))

    time_passed  = clock.tick(30)
    time_sec     = time_passed / 1000.0
    pad_speed    = ball_speed * time_sec

    ball_x      += ball_speed_x * time_sec
    ball_y      += ball_speed_y * time_sec
    screen.blit(ball, (ball_x, ball_y))

    # Bounce on up and down walls
    if ball_y <= ball_up_limit:
        ball_speed_y = -ball_speed_y
        ball_y       = ball_up_limit
    elif ball_y >= ball_down_limit:
        ball_speed_y = -ball_speed_y
        ball_y       = ball_down_limit

    # Bounce on bats
    if ball_x <= bat_left_x + 10.0:
        if ball_y >= bat_left_y - 7.5 and ball_y <= bat_left_y + 42.5:
            ball_x       = 20.0
            ball_speed_x = -ball_speed_x
            
    if ball_x >= bat_right_x - 15.:
        if ball_y >= bat_right_y - 7.5 and ball_y <= bat_right_y + 42.5:
            ball_x   = 605.0
            ball_speed_x  = -ball_speed_x

    # Detect points
    if ball_x < left_limit:
        bat_right_score += 1
        ball_x           = 320.0
        ball_y           = 232.5
        bat_left_y       = bat_center_y
        bat_right_y      = bat_center_y
    elif ball_x > rigth_limit:
        bat_left_score  += 1
        ball_x           = 307.5
        ball_y           = 232.5
        bat_left_y       = bat_center_y
        bat_right_y      = bat_center_y

    pygame.display.update()
