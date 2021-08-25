# Dr Michaels
# card.py
# 4/5/21
# This file contains an implementation of the Card class.
# The Card class contains a constructor, accessor methods for suit and face,
# a tostring method, and a comparison method.

import random

class Card:

	def __init__(self, the_face, the_suit):
		self.face = the_face
		self.suit = the_suit
		
	def get_suit(self):
		return self.suit

	def get_face(self):
		return self.face
		
	def __eq__(self, other_card):
		return (self.face == other_card.get_face()) and (self.suit == other_card.get_suit())
		
	def __gt__(self, other_card):
		if self.face > other_card.get_face():
			return True
		elif (self.face == other_card.get_face()):
			return self.suit > other_card.get_suit()
		else:
			return False
			
	def __str__(self):
		return "%s of %s" % (self.face, self.suit)


def rand_card():
	face = [2,3,4,5,6,7,8,9,10,11,12,13,14]
	suit = ["Clubs", "Hearts", "Diamonds", "Spades"]
	return Card(random.choice(face), random.choice(suit))

def extra_credit(my_data):
    print("Place your code below to determine the number of triplets inside the input array.")
    print("Your code must at minimum find the base set, you do not need to calculate all permutations")

    if len(my_data) < 3:
        return "Not enough to form triplet"
    total = 0
    triplets = {}

    for i in range(len(my_data)):
        temp = str(my_data[i])
        if temp in triplets:
            triplets[temp] += 1
        else:
            triplets[temp] = 1

    for key in triplets:
        if triplets[key] == 3:
            total += 1
        elif triplets[key] > 3:
            total += nCk(triplets[key], 3)

            return total
    

def main():
    print("This main method will briefly test the card class!")
    print("It will manually make three cards, print them, and compare them")
    print("It will then generate 10 random cards and compare them")

    card_one = Card(2, "Clubs")
    card_two = Card(7, "Spades")
    card_three = Card(7, "Hearts")
    card_four = Card(7, "Spades")

    print("The three manually created cards are: %s, %s, and %s" % (card_one, card_two, card_three))
    print("Card one is equal to card two: %s" % (card_one == card_two))
    print("Card four is equivalent to Card two. Are they equal: %s" % (card_two == card_four))
    print("Is %s greater than %s: %s" % (card_one, card_two, card_one > card_two))
    print("Is %s greater than %s: %s" % (card_two, card_one, card_two > card_one))
    print("Is %s less than %s: %s" % (card_one, card_three, card_one < card_three))
    print("Is %s Less than %s: %s" % (card_two, card_three, card_two < card_three))
    print("Is %s Less than %s: %s" % (card_three, card_two, card_three < card_two))
    
    print("\n\nNow we will make 10 random cards and compare them all")
    my_cards = []
    for i in range(10):
        my_cards.append(rand_card())
    print("The cards we have selected are:")
    result = ""
    for item in my_cards:
        result += "%s\t" % item
    print(result)
        
    print("We will now do 30 random comparisons")
    for i in range(30):
        card_one = random.choice(my_cards)
        card_two = random.choice(my_cards)
        print("%s > %s: %s" % (card_one, card_two, card_one > card_two))
        print("%s < %s: %s" % (card_one, card_two, card_one < card_two))
        print("%s == %s: %s" % (card_one, card_two, card_one == card_two))
        
    # hand_one = [card_one, card_two, card_three, card_four, Card(7, "Spades"), Card(14, "Hearts")]
    # print("In hand one we have three instances of %s. When we call extra_credit, it should return one." % card_two)
    # hand_two = [card_one, card_two, card_three, card_four, Card(7, "Spades"), Card(14, "Hearts"), card_one, card_one, card_two]
    # print("In hand two we have four instances of %s and three of %s. Our return value must be at least two, preferably three (or more if you count all possible permutations)" % (card_two, card_one))
    # hand_three = hand_two
    # hand_four = hand_two
    # for i in range(10):
        # hand_three.append(rand_card())
    # for i in range(100):
        # hand_four.append(rand_card())
    # print("Hand three contains the exact contents of hand two, with ten random cards. Hand four is similar, except with 100 additional cards.")
    
    
main()