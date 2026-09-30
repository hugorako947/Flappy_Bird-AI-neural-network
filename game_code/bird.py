import pygame
from random import *
from game_code.colors_background import *
from game_code.pipes import *

a = input("manual or AI ? (m/ai) : ")
b = input("show results ? (Y/N) : ")
bird_sizeX = 2
bird_sizeY = 25
bird_reset_pos = [80, (Y / 2) - (bird_sizeY / 2)]
bird_pos = [bird_reset_pos[0], bird_reset_pos[1]]
if a == "ai":
	bird_values = [15, 7, 3, 0.2, 1]
else:
	bird_values = [40, -5, 1, 0.07, 1]
bird_speed = bird_values[0]
bird_gravity = bird_values[1]
bird_jump = bird_values[2]

images_random = randint(1,10)

def bird_draw(screen, bird_pos, images_random):
	if images_random == 1:
		Img_bird = pygame.image.load('sprites/flappybird_jaune.png')
	if images_random == 2:
		Img_bird = pygame.image.load('sprites/flappybird_bleu.png')
	if images_random == 3:
		Img_bird = pygame.image.load('sprites/flappybird_rouge.png')
	if images_random == 4:
		Img_bird = pygame.image.load('sprites/flappybird_vert.png')
	if images_random == 5:
		Img_bird = pygame.image.load('sprites/flappybird_violet.png')
	if images_random == 6:
		Img_bird = pygame.image.load('sprites/flappybird_orange.png')
	if images_random == 7:
		Img_bird = pygame.image.load('sprites/flappybird_marron.png')
	if images_random == 8:
		Img_bird = pygame.image.load('sprites/flappybird_noir.png')
	if images_random == 9:
		Img_bird = pygame.image.load('sprites/flappybird_blanc.png')
	if images_random == 10:
		Img_bird = pygame.image.load('sprites/flappybird_rose.png')
	pygame.draw.rect(screen, BLUE, (bird_pos[0], bird_pos[1], bird_sizeX, bird_sizeY))
	screen.blit(Img_bird, (bird_pos[0] - 7,bird_pos[1] - 3))

def bird_lines_draw(screen, bird_pos, pipe1_pos, bird_sizeX, bird_sizeY, pipe2_pos):
	pygame.draw.line(screen, RED, (bird_pos[0] + bird_sizeX,bird_pos[1]), (pipe1_pos[0],pipe1_pos[1] + 675), 2)
	pygame.draw.line(screen, RED, (bird_pos[0] + bird_sizeX,bird_pos[1] + bird_sizeY), (pipe2_pos[0],pipe2_pos[1]), 2)
	pygame.draw.line(screen, YELLOW, (bird_pos[0] + (bird_sizeX / 2),0), (bird_pos[0] + (bird_sizeX / 2),bird_pos[1] + (bird_sizeY / 2)), 2)
	pygame.draw.line(screen, BLUE2, (0,bird_pos[1] + (bird_sizeY / 2)), (bird_pos[0] + (bird_sizeX / 2),bird_pos[1] + (bird_sizeY / 2)), 2)