# Name: Quang
# Section: 2
# hw2.py

##### Template for Homework 2, exercises 2.0 - 2.5  ######
import math
import random
# **********  Exercise 2.0 ********** 

def f1(x):
    print x + 1

def f2(x):
    return x + 1

# **********  Exercise 2.1 ********** 

def rps_game(player_1, player_2):
	valid1 = player_1 == 'rock' or player_1 == 'scissors' or player_1 == 'paper'

	if not valid1:
		print "This is not a valid object selection"

	valid2 = player_2 == 'rock' or player_2 == 'scissors' or player_2 == 'paper'

	if not valid2:
		print "This is not a valid object selection"

	if valid1 and valid2:
		if  player_1 == 'rock' and\
			player_2 == 'scissors':
			return "Player 1 wins"
		if  player_1 == 'scissors' and\
			player_2 == 'paper':
			return "Player 1 wins"
		if  player_1 == 'paper' and\
			player_2 == 'rock':
			return "Player 1 wins"
		if  player_2 == 'rock' and\
			player_1 == 'scissors':
			return "Player 2 wins"
		if  player_2 == 'scissors' and\
			player_1 == 'paper':
			return "Player 2 wins"
		if  player_2 == 'paper' and\
			player_1 == 'rock':
			return"Player 2 wins"
		elif player_1 == player_2:
			return "Tie"

# Test Cases for Exercise 2.1
##### YOUR CODE HERE #####

print rps_game('rock', 'paper')
print rps_game('scissors', 'paper')
print rps_game('rock', 'scissors')

# ********** Exercise 2.2 ********** 

# Define is_divisible function here
##### YOUR CODE HERE #####
def is_divisible(m, n):
	if m % n == 0:
		return True
	else:
		return False
# Test cases for is_divisible
## Provided for you... uncomment when you're done defining your function

print is_divisible(10, 5)  # This should return True
print is_divisible(18, 7)  # This should return False
#print is_divisible(42, 0)  # What should this return? Error! not contain zero division or modulo


# Define not_equal function here
##### YOUR CODE HERE #####
def not_equal(a, b):
	return not (a == b)
#Test cases for not_equal
##### YOUR CODE HERE #####

print not_equal(1, 1) #return False
print not_equal(2, 3) #return True

# ********** Exercise 2.3 ********** 

## 1 - multadd function
##### YOUR CODE HERE #####
def multadd(a, b, c):
	return a*b + c

## 2 - Equations
##### YOUR CODE HERE #####
# Test Cases
angle_test = multadd(math.cos(math.pi/4), 1/2, math.sin(math.pi/4))
print "sin(pi/4) + cos(pi/4)/2 is:"
print angle_test

ceiling_test =multadd(2, math.log(12, 7), 276/19)
print "ceiling(276/19) + 2 log_7(12) is:"
print ceiling_test

## 3 - yikes function
##### YOUR CODE HERE #####
def yikes(x):
	return multadd(x, math.exp(-x), (1 - math.exp(-x))**1/2)

# Test Cases
x = 5
print "yikes(5) =", yikes(x)

# ********** Exercise 2.4 **********

## 1 - rand_divis_3 function
##### YOUR CODE HERE #####
def rand_divis_3():
	n = random.randint(0, 100);
	return n % 3 == 0

# Test Cases
##### YOUR CODE HERE #####
print rand_divis_3()
## 2 - roll_dice function - remember that a die's lowest number is 1;
                            #its highest is the number of sides it has
##### YOUR CODE HERE #####
def roll_dice(sides, dices):
	for i in range(dices):
		print random.randint(1, sides)
# Test Cases
##### YOUR CODE HERE #####                            
roll_dice(6, 3)
# ********** Exercise 2.5 **********

# code for roots function
##### YOUR CODE HERE #####   
def roots(a, b, c):
	if a == 0:
		print "This isn't a quadratic equation"
	else:
		delta = b**2 - 4*a*c
		if delta > 0:
			print "Root 1:", (-b + delta**1/2)/2*a
			print "Root 2:", (-b - delta**1/2)/2*a
		elif delta == 0:
			print "Root:", -b/2*a
		else:
			print "The roots are complex"
# Test Cases
##### YOUR CODE HERE #####   

roots(1, 2, 3)
roots(1, -2, 1)