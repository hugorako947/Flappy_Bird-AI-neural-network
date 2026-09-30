import pygame
import decimal
from random import *

dx = 0
x, y = 0, 0
dy1 = 0
dy2 = 0
w_min, w_max = 0, 100
weights_nbr = 16
weights = [randint(w_min,w_max)/100] * weights_nbr
'''weights = [randint(w_min,w_max)/100, randint(w_min,w_max)/100, randint(w_min,w_max)/100, randint(w_min,w_max)/100,
		randint(w_min,w_max)/100, randint(w_min,w_max)/100, randint(w_min,w_max)/100, randint(w_min,w_max)/100,
		randint(w_min,w_max)/100, randint(w_min,w_max)/100, randint(w_min,w_max)/100, randint(w_min,w_max)/100,
		randint(w_min,w_max)/100, randint(w_min,w_max)/100, randint(w_min,w_max)/100, randint(w_min,w_max)/100]'''
output, hidden_layer = [0], [0] * 4
biais = 0

decimal.getcontext().prec = 100

def bird_neural_network(screen, hidden_layer, weights, biais, output, dx, dy1, dy2):
	# hidden layer - middle neurons
	hidden_layer[0] = dx *  weights[0] + dy1 * weights[1] + dy2 * weights[2] + biais
	hidden_layer[1] = dx * weights[3] + dy1 * weights[4] + dy2 * weights[5] + biais
	hidden_layer[2] = dx * weights[6] + dy1 * weights[7] + dy2 * weights[8] + biais
	hidden_layer[3] = dx * weights[9] + dy1 * weights[10] + dy2 * weights[11] + biais
	'''
	hidden_layer[0] = decimal.Decimal(dx) *  int(weights[0]) + decimal.Decimal(dy1) * int(weights[1]) + decimal.Decimal(dy2) * int(weights[2]) + biais
	hidden_layer[1] = decimal.Decimal(dx) * int(weights[3]) + decimal.Decimal(dy1) * int(weights[4]) + decimal.Decimal(dy2) * int(weights[5]) + biais
	hidden_layer[2] = decimal.Decimal(dx) * int(weights[6]) + decimal.Decimal(dy1) * int(weights[7]) + decimal.Decimal(dy2) * int(weights[8]) + biais
	hidden_layer[3] = decimal.Decimal(dx) * int(weights[9]) + decimal.Decimal(dy1) * int(weights[10]) + decimal.Decimal(dy2) * int(weights[11]) + biais
	'''
	# hidden layer - sigmoid function
	hidden_layer[0] = 1 / (1 + 10**(-hidden_layer[0]))
	hidden_layer[1] = 1 / (1 + 10**(-hidden_layer[1]))
	hidden_layer[2] = 1 / (1 + 10**(-hidden_layer[2]))
	hidden_layer[3] = 1 / (1 + 10**(-hidden_layer[3]))
	# output - exit neuron
	output[0] = hidden_layer[0] * weights[12] + hidden_layer[1] * weights[13] + hidden_layer[2] * weights[14] + hidden_layer[3] * weights[15] + biais
	'''
	output[0] = decimal.Decimal(hidden_layer[0]) * int(weights[12]) + decimal.Decimal(hidden_layer[1]) * int(weights[13]) + decimal.Decimal(hidden_layer[2]) * int(weights[14]) + decimal.Decimal(hidden_layer[3]) * int(weights[15]) + biais
	'''
	# output - sigmoid function
	output[0] = 1 / (1 + 10**(-output[0]))