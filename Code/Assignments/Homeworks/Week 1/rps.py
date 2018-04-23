player_1 = raw_input("Player 1?")
valid1 = player_1 == 'rock' or player_1 == 'scissors' or player_1 == 'paper'

if not valid1:
	print "This is not a valid object selection"

player_2 = raw_input("Player 2?")
valid2 = player_2 == 'rock' or player_2 == 'scissors' or player_2 == 'paper'

if not valid2:
	print "This is not a valid object selection"

if valid1 and valid2:
	if  player_1 == 'rock' and\
		player_2 == 'scissors':
		print "Player 1 wins"
	if  player_1 == 'scissors' and\
		player_2 == 'paper':
		print "Player 1 wins"
	if  player_1 == 'paper' and\
		player_2 == 'rock':
		print "Player 1 wins"
	if  player_2 == 'rock' and\
		player_1 == 'scissors':
		print "Player 2 wins"
	if  player_2 == 'scissors' and\
		player_1 == 'paper':
		print "Player 2 wins"
	if  player_2 == 'paper' and\
		player_1 == 'rock':
		print "Player 2 wins"
	elif player_1 == player_2:
		print "Tie"


