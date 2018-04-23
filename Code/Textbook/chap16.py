import random

class Card:
	suit_name = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
	rank_name = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
class Deck:
	def deal(self, hands, nCard = 999):
		nHands = len(hands)
		for i in range(nHands):
			if self.isEmpty(): break
			card = self.popCard()
			hand = hands[i%nHands]
			hand.addCard(card)

class Hand(Deck):
	def __init__(self, name = ''):
		self.cards = []
		self.name = name

	def __str__(self):
		s = "Hand" + self.name
		if self.isEmpty():
			return s + "is empty\n"
		else:
			return s + "contains\n" + Deck.__str__(self)

	def addCard(self, Card):
		self.cards.append(card)

class CardGame:
	def __init__(self):
		self.deck = Deck()
		self.deck.shuffle()

class OldMaidHand(Hand):
	def removeMatches(self):
		count = 0
		originalCards = self.cards[:]
		
		for card in originalCards:
			match = Card(3 - card.suit, card.rank)
			
			if match in self.cards:
				self.cards.remove(card)
				self.cards.remove(match)
				print "Hand %s: %s matches %s" % (self.name, card, match)
				count = count + 1
			
			return count

class OldMaidGame(CardGame):
	def removeAllMatches(self):
		count = 0
		for hand in self.hands:
			count = count + hand.removeMatches()

		return count

	def play(self, names):
		#Remove Queen of Clubs
		self.deck.removeCard(Card(0,12))

		#make a hand for each player
		self.hands = []
		for name in names:
			self.hands.append(OldMaidGame(name))

		#deal the cards
		self.deck.deal(self.hands)
		print "---------- Cards have been dealt"

		#remove initial mathches
		mathches = self.removeAllMatches()
		print "---------- Matches discarded, play begins"
		self.printHands()

		#play until all 50 cards are matched
		turn = 0
		numHands = len(self.hands)
		while matches < 25:
			matches = matches + self.playOneTurn(turn)
			turn = (turn + 1) % numHands

		print "---------- Game is over"
		self.printHands()

	def printHands(self):
		for hand in self.hands:
			print hand

	def playOneTurn(self, i):
		if self.hands[i].isEmpty():
			return 0

		neighbor = self.findNeighbor(i)
		pickedCard = self.hands[neighbor].popCard()
		self.hands[i].addCard(pickedCard)
		print "Hand", self.hands[i].name, "picked", pickedCard
		count = self.hands[i].removeMatches()
		self.hands[i].shuffle()
		return count

	def findNeighbor(self, i):
		numHands = len(self.hands)
		for next in range(1, numHands):
			neighbor = (i + next) % numHands
			if not self.hands[neighbor].isEmpty():
				return neighbor

game = OldMaidGame()
game.play(['Allen', 'Jeff', 'Chris'])