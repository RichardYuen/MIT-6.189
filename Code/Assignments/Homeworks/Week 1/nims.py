# Name:Quang 
# Section: 2
# nims.py

def play_nims(pile, max_stones):
    '''
    An interactive two-person game; also known as Stones.
    @param pile: the number of stones in the pile to start
    @param max_stones: the maximum number of stones you can take on one turn
    '''
    ## Basic structure of program (feel free to alter as you please):
    while pile != 0:
    	
    	player1 = 0
    	player2 = 0
        
        while not (player1 >= 1 and player1 <= max_stones) or player1 > pile:
            player1 = int(raw_input("Player 1 move: "))
        pile -= player1
        print pile, "stones left"
        current = "Player 1"
        
        if pile == 0: break

        while not (player2 >= 1 and player2 <= max_stones) or player2 > pile:
            player2 = int(raw_input("Player 2 move: "))
        pile -= player2
        print pile, "stones left"

        current = "Player 2"

    print  current, "wins!"
    print "Game over"

play_nims(10, 3)