import pygame
from random import *
from game_code.colors_background import *

X, Y = 1000, 675

Img_pipe1 = pygame.image.load('sprites/pipe1.png')
Img_pipe2 = pygame.image.load('sprites/pipe2.png')

size_hole = 200
pipe1_pos = [600, randint(-Y,(-2)*size_hole)]
pipe2_pos = [600, pipe1_pos[1] + 675 + size_hole]
pipes_speed = 1

def pipe1_draw(screen, pipe1_pos):
	pygame.draw.rect(screen, GREEN, (pipe1_pos[0], pipe1_pos[1], 100, Y))
	screen.blit(Img_pipe1, (pipe1_pos[0],pipe1_pos[1]))

def pipe2_draw(screen, pipe2_pos):
	pygame.draw.rect(screen, GREEN, (pipe2_pos[0], pipe2_pos[1], 100, Y))
	screen.blit(Img_pipe2, (pipe2_pos[0],pipe2_pos[1]))