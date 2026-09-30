import pygame
from game_code.colors_background import *

gen = 1
score = 0
record = 0
police_normale = 'fonts/normale.ttf'
Img_background_flappybird = pygame.image.load('sprites/background_flappybird.png')
best_bird_list_color = [0]
best_bird_list_gen = [0]
best_bird_list_weights = [0] * 4
Img_bird2 = pygame.image.load('sprites/flappybird_gris.png')

def best_bird_draw(screen, images_random, best_bird_list_color, Img_bird2, best_bird_list_weights):
	images_random = best_bird_list_color[-1]
	if images_random == 1:
		Img_bird2 = pygame.image.load('sprites/flappybird_jaune.png')
	if images_random == 2:
		Img_bird2 = pygame.image.load('sprites/flappybird_bleu.png')
	if images_random == 3:
		Img_bird2 = pygame.image.load('sprites/flappybird_rouge.png')
	if images_random == 4:
		Img_bird2 = pygame.image.load('sprites/flappybird_vert.png')
	if images_random == 5:
		Img_bird2 = pygame.image.load('sprites/flappybird_violet.png')
	if images_random == 6:
		Img_bird2 = pygame.image.load('sprites/flappybird_orange.png')
	if images_random == 7:
		Img_bird2 = pygame.image.load('sprites/flappybird_marron.png')
	if images_random == 8:
		Img_bird2 = pygame.image.load('sprites/flappybird_noir.png')
	if images_random == 9:
		Img_bird2 = pygame.image.load('sprites/flappybird_blanc.png')
	if images_random == 10:
		Img_bird2 = pygame.image.load('sprites/flappybird_rose.png')
	screen.blit(Img_bird2, (900,350))

def infos_grey_draw(screen):
	pygame.draw.rect(screen, GREY, (600, 0, 400, 675))
	pygame.draw.line(screen, GREY2, (600,115), (1000,115), 2)
	pygame.draw.line(screen, GREY2, (600,285), (1000,285), 2)

def num_infos_draw(screen, gen, score, record, dx, dy1, dy2, x, y, best_bird_list_gen):
	police1 = pygame.font.Font(police_normale, 20)
	police2 = pygame.font.Font(police_normale, 25)
	# generations
	texte_gen = police1.render("Generations : ", True, WHITE)
	texte_gen_num = police1.render(str(gen), True, ORANGE)
	# score
	texte_score = police1.render("Score : ", True, WHITE)
	texte_score_num = police1.render(str(score), True, ORANGE)
	# record
	texte_record = police1.render("Record : ", True, WHITE)
	texte_record_num = police1.render(str(record), True, ORANGE)
	# game title
	texte_game = police2.render("GAME", True, GREY2)
	# inputs title
	texte_data = police2.render("DATA", True, GREY2)
	# distance x bird - pipes
	texte_dx = police1.render("Distance x bird - pipes : ", True, WHITE)
	texte_dx_num = police1.render(str(dx), True, ORANGE)
	# distance y bird - top pipe
	texte_dy1 = police1.render("Distance y bird - top pipe : ", True, WHITE)
	texte_dy1_num = police1.render(str(dy1), True, ORANGE)
	# distance y bird - bottom pipe
	texte_dy2 = police1.render("Distance y bird - bottom pipe : ", True, WHITE)
	texte_dy2_num = police1.render(str(dy2), True, ORANGE)
	# x
	texte_x = police1.render("Bird x : ", True, WHITE)
	texte_x_num = police1.render(str(x), True, ORANGE)
	# y
	texte_y = police1.render("Bird y : ", True, WHITE)
	texte_y_num = police1.render(str(y), True, ORANGE)
	# best bird title
	texte_best_bird = police2.render("BEST BIRD", True, GREY2)
	# color
	texte_best_bird_color = police1.render("Best bird - color : ", True, WHITE)
	# best bird score
	texte_best_bird_score = police1.render("Best bird - score : ", True, WHITE)
	texte_best_bird_score_num = police1.render(str(record), True, ORANGE)
	# best bird generation
	texte_best_bird_gen = police1.render("Best bird - generation : ", True, WHITE)
	texte_best_bird_gen_num = police1.render(str(best_bird_list_gen[-1]), True, ORANGE)
	# best bird weights
	texte_best_bird_weights = police1.render("Best bird - weights : ", True, WHITE)
	texte_best_bird_weights_num1 = police1.render(str(best_bird_list_weights[0]), True, ORANGE)
	texte_best_bird_weights_num2 = police1.render(str(best_bird_list_weights[1]), True, ORANGE)
	texte_best_bird_weights_num3 = police1.render(str(best_bird_list_weights[2]), True, ORANGE)
	texte_best_bird_weights_num4 = police1.render(str(best_bird_list_weights[3]), True, ORANGE)
	screen.blit(texte_gen, [605,30])
	screen.blit(texte_gen_num, [745,30])
	screen.blit(texte_score, [605,55])
	screen.blit(texte_score_num, [680,55])
	screen.blit(texte_record, [605,80])
	screen.blit(texte_record_num, [690,80])
	screen.blit(texte_game, [775,0])
	screen.blit(texte_data, [775,120])
	screen.blit(texte_dx, [605,150])
	screen.blit(texte_dx_num, [843,150])
	screen.blit(texte_dy1, [605,175])
	screen.blit(texte_dy1_num, [870,175])
	screen.blit(texte_dy2, [605,200])
	screen.blit(texte_dy2_num, [905,200])
	screen.blit(texte_x, [605,225])
	screen.blit(texte_x_num, [685,225])
	screen.blit(texte_y, [605,250])
	screen.blit(texte_y_num, [685,250])
	screen.blit(texte_best_bird, [750,295])
	screen.blit(texte_best_bird_color, [605,350])
	screen.blit(texte_best_bird_score, [605,400])
	screen.blit(texte_best_bird_score_num, [900,400])
	screen.blit(texte_best_bird_gen, [605,450])
	screen.blit(texte_best_bird_gen_num, [900,450])
	screen.blit(texte_best_bird_weights, [605,500])
	screen.blit(texte_best_bird_weights_num1, [605,550])
	screen.blit(texte_best_bird_weights_num2, [605,575])
	screen.blit(texte_best_bird_weights_num3, [605,600])
	screen.blit(texte_best_bird_weights_num4, [605,625])

def background_flappybird_draw(screen):
	screen.blit(Img_background_flappybird, (0,475))