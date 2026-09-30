import pygame
from random import *
from game_code.colors_background import *
from game_code.background import *
from game_code.bird import *
from game_code.pipes import *
from game_code.neural_network import *
from game_code.sounds import *

def game_main():
	pygame.init()
	screen = pygame.display.set_mode((X,Y))
	pygame.display.set_caption("FlappyBird Neural Network")
	gameloop(screen)

def gameloop(screen):
	global bird_pos, bird_speed, bird_gravity, bird_jump
	global gen, score, record, pipe1_pos, pipe2_pos, x, y
	global pipes_speed, bird_sizeX, bird_sizeY, images_random
	global dx, dy1, dy2, size_hole, output, weights, biais
	global w_min, w_max, weights_nbr, bird_reset_pos
	global best_bird_list_color, best_bird_list_gen
	global Img_bird2, best_bird_list_weights, bird_values
	global X, Y, a, b
	game_over = False
	while not game_over:
		for event in pygame.event.get():
			if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
				if b == "Y":
					print(weights[0:3])
					print(weights[4:7])
					print(weights[8:11])
					print(weights[12:15])
				game_over = True

		if a == "ai":
			if output[0] <= 0.5:
				wing.set_volume(0.1)
				wing.play()
				bird_pos[1] -= bird_speed
			else:
				bird_pos[1] += bird_gravity

		# gravity and jumping
		if a == "m":
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					if not bird_jump <= 0:
						bird_gravity = bird_values[1]
						bird_speed += bird_values[4]
						bird_pos[1] -= bird_speed
						bird_jump -= 1
					else:
						bird_speed = bird_values[0]
						bird_gravity += 0.2
						bird_pos[1] += bird_gravity
				else:
					bird_jump = bird_values[2]
					bird_speed = bird_values[0]
					bird_gravity += bird_values[3]
					bird_pos[1] += bird_gravity
			else:
				bird_jump = bird_values[2]
				bird_speed = bird_values[0]
				bird_gravity += bird_values[3]
				bird_pos[1] += bird_gravity

		# velocity and speed of pipes
		pipe1_pos[0] -= pipes_speed
		pipe2_pos[0] -= pipes_speed
		# inputs data
		dx = pipe1_pos[0] - (bird_pos[0] + bird_sizeX)
		x, y = bird_pos[0] + bird_sizeX, bird_pos[1] + (bird_sizeY / 2)
		dy1 = (pipe1_pos[1] + Y) - bird_pos[1]
		dy2 = pipe2_pos[1] - (bird_pos[1] + bird_sizeY)

		# colisions of the top pipe
		if (pipe1_pos[0] <= bird_pos[0] <= pipe1_pos[0] + 100) and (bird_pos[1] <= pipe1_pos[1] + 675):
			bird_pos = [bird_reset_pos[0], bird_reset_pos[1]]
			bird_speed = bird_values[0]
			bird_gravity = bird_values[1]
			bird_jump = bird_values[2]
			gen += 1
			pipe1_pos = [600, randint(-Y,(-2)*size_hole)]
			pipe2_pos = [600, pipe1_pos[1] + 675 + size_hole]
			pipes_speed = 2
			score = 0
			images_random = randint(1,10)
			'''weights = [randint(w_min,w_max)/100, randint(w_min,w_max)/100, randint(w_min,w_max)/100, randint(w_min,w_max)/100,
					randint(w_min,w_max)/100, randint(w_min,w_max)/100, randint(w_min,w_max)/100, randint(w_min,w_max)/100,
					randint(w_min,w_max)/100, randint(w_min,w_max)/100, randint(w_min,w_max)/100, randint(w_min,w_max)/100,
					randint(w_min,w_max)/100, randint(w_min,w_max)/100, randint(w_min,w_max)/100, randint(w_min,w_max)/100]'''
			weights = [randint(w_min,w_max)/100] * weights_nbr
		if (pipe1_pos[0] <= bird_pos[0] + bird_sizeX <= pipe1_pos[0] + 100) and (bird_pos[1] <= pipe1_pos[1] + 675):
			bird_pos = [bird_reset_pos[0], bird_reset_pos[1]]
			bird_speed = bird_values[0]
			bird_gravity = bird_values[1]
			bird_jump = bird_values[2]
			gen += 1
			pipe1_pos = [600, randint(-Y,(-2)*size_hole)]
			pipe2_pos = [600, pipe1_pos[1] + 675 + size_hole]
			pipes_speed = 2
			score = 0
			images_random = randint(1,10)
			'''weights = [randint(w_min,w_max)/100, randint(w_min,w_max)/100, randint(w_min,w_max)/100, randint(w_min,w_max)/100,
					randint(w_min,w_max)/100, randint(w_min,w_max)/100, randint(w_min,w_max)/100, randint(w_min,w_max)/100,
					randint(w_min,w_max)/100, randint(w_min,w_max)/100, randint(w_min,w_max)/100, randint(w_min,w_max)/100,
					randint(w_min,w_max)/100, randint(w_min,w_max)/100, randint(w_min,w_max)/100, randint(w_min,w_max)/100]'''
			weights = [randint(w_min,w_max)/100] * weights_nbr
		# colisions of the bottom pipe
		if (pipe2_pos[0] <= bird_pos[0] <= pipe2_pos[0] + 100) and (bird_pos[1] + bird_sizeY >= pipe2_pos[1]):
			bird_pos = [bird_reset_pos[0], bird_reset_pos[1]]
			bird_speed = bird_values[0]
			bird_gravity = bird_values[1]
			bird_jump = bird_values[2]
			gen += 1
			pipe1_pos = [600, randint(-Y,(-2)*size_hole)]
			pipe2_pos = [600, pipe1_pos[1] + 675 + size_hole]
			pipes_speed = 2
			score = 0
			images_random = randint(1,10)
			'''weights = [randint(w_min,w_max)/100, randint(w_min,w_max)/100, randint(w_min,w_max)/100, randint(w_min,w_max)/100,
					randint(w_min,w_max)/100, randint(w_min,w_max)/100, randint(w_min,w_max)/100, randint(w_min,w_max)/100,
					randint(w_min,w_max)/100, randint(w_min,w_max)/100, randint(w_min,w_max)/100, randint(w_min,w_max)/100,
					randint(w_min,w_max)/100, randint(w_min,w_max)/100, randint(w_min,w_max)/100, randint(w_min,w_max)/100]'''
			weights = [randint(w_min,w_max)/100] * weights_nbr
		if (pipe2_pos[0] <= bird_pos[0] + bird_sizeX <= pipe2_pos[0] + 100) and (bird_pos[1] + bird_sizeY >= pipe2_pos[1]):
			bird_pos = [bird_reset_pos[0], bird_reset_pos[1]]
			bird_speed = bird_values[0]
			bird_gravity = bird_values[1]
			bird_jump = bird_values[2]
			gen += 1
			pipe1_pos = [600, randint(-Y,(-2)*size_hole)]
			pipe2_pos = [600, pipe1_pos[1] + 675 + size_hole]
			pipes_speed = 2
			score = 0
			images_random = randint(1,10)
			'''weights = [randint(w_min,w_max)/100, randint(w_min,w_max)/100, randint(w_min,w_max)/100, randint(w_min,w_max)/100,
					randint(w_min,w_max)/100, randint(w_min,w_max)/100, randint(w_min,w_max)/100, randint(w_min,w_max)/100,
					randint(w_min,w_max)/100, randint(w_min,w_max)/100, randint(w_min,w_max)/100, randint(w_min,w_max)/100,
					randint(w_min,w_max)/100, randint(w_min,w_max)/100, randint(w_min,w_max)/100, randint(w_min,w_max)/100]'''
			weights = [randint(w_min,w_max)/100] * weights_nbr
		# bird crash reset
		if bird_pos[1] + 10 >= 675:
			hit.set_volume(0.5)
			hit.play()
			bird_pos = [bird_reset_pos[0], bird_reset_pos[1]]
			bird_speed = bird_values[0]
			bird_gravity = bird_values[1]
			bird_jump = bird_values[2]
			gen += 1
			pipe1_pos = [600, randint(-Y,(-2)*size_hole)]
			pipe2_pos = [600, pipe1_pos[1] + 675 + size_hole]
			pipes_speed = 2
			score = 0
			images_random = randint(1,10)
			'''weights = [randint(w_min,w_max)/100, randint(w_min,w_max)/100, randint(w_min,w_max)/100, randint(w_min,w_max)/100,
					randint(w_min,w_max)/100, randint(w_min,w_max)/100, randint(w_min,w_max)/100, randint(w_min,w_max)/100,
					randint(w_min,w_max)/100, randint(w_min,w_max)/100, randint(w_min,w_max)/100, randint(w_min,w_max)/100,
					randint(w_min,w_max)/100, randint(w_min,w_max)/100, randint(w_min,w_max)/100, randint(w_min,w_max)/100]'''
			weights = [randint(w_min,w_max)/100] * weights_nbr
		# augmentation score and variables
		if pipe1_pos[0] <= -100:
			point.set_volume(0.3)
			point.play()
			pipes_speed += 0.1
			bird_jump += 0.2
			bird_speed += 0.5
			bird_gravity += 0.2
			score += 1
			pipe1_pos = [600, randint(-Y,(-2)*size_hole)]
			pipe2_pos = [600, pipe1_pos[1] + 675 + size_hole]
		# augmentation record score / best score / high-score
		if score > record:
			best_bird.set_volume(0.3)
			best_bird.play()
			record = score
			best_bird_list_color.append(images_random)
			best_bird_list_gen.append(gen)
			best_bird_list_weights[0] = weights[0:3]
			best_bird_list_weights[1] = weights[4:7]
			best_bird_list_weights[2] = weights[8:11]
			best_bird_list_weights[3] = weights[12:15]
			if b == "Y":
				print("*********************")
				print(weights[0:3])
				print(weights[4:7])
				print(weights[8:11])
				print(weights[12:15])
				print("score : " + str(record))

		screen.fill(BLUE)
		background_flappybird_draw(screen)
		bird_lines_draw(screen, bird_pos, pipe1_pos, bird_sizeX, bird_sizeY, pipe2_pos)
		bird_draw(screen, bird_pos, images_random)
		pipe1_draw(screen, pipe1_pos)
		pipe2_draw(screen, pipe2_pos)
		infos_grey_draw(screen)
		num_infos_draw(screen, gen, score, record, dx, dy1, dy2, x, y, best_bird_list_gen)
		best_bird_draw(screen, images_random, best_bird_list_color, Img_bird2, best_bird_list_weights)
		if a == "ai":
			bird_neural_network(screen, hidden_layer, weights, biais, output, dx, dy1, dy2)
		pygame.display.update()

	pygame.quit()

game_main()