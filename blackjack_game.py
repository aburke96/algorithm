# Alexandra Burke
# blackjack_game.py
# 4/20/21
# This file contains information on a card and deck class.
# Together we will build a player class
# Then begin designing rules for a game

# Global variables used to create a new deck
face = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
suit = ["Clubs", "Diamonds", "Hearts", "Spades"]

import random

class Card:
    # Constructor method for Card.
    # Takes as input a face and suit value. 
    # If they are not found in the global variables above, the card will be set to a 2 of clubs
    def __init__(self, the_face, the_suit):
        global face, suit
        if (the_face in face and the_suit in suit):
            self.face = the_face
            self.suit = the_suit
        else:
            #print("Illegal card value, creating a 2 of Clubs")
            self.face = -1
            self.suit = "ILLEGAL CARD"

    # Retuns the suit value of the calling card
    def get_suit(self):
        return self.suit

    # Returns the face value of the calling card
    def get_face(self):
        return self.face

    # Compares the face and suit attributes of other_card to those possessed by the calling card
    def __eq__(self, other_card):
        return (self.face == other_card.get_face()) and (self.suit == other_card.get_suit())

    # Returns the value of self > other_card
    # The first comparison is on face value. If the faces are different, we return the result of
    # self.face > other_card.get_face()
    # If they are tied, we return the result of self.suit > other_card.get_suit()
    def __gt__(self, other_card):
        if self.face > other_card.get_face():
            return True
        elif (self.face == other_card.get_face()):
            return self.suit > other_card.get_suit()
        else:
            return False

    # Card tostring. Will return the card in the format "Face of Suit"
    def __str__(self):
        return "%s of %s" % (self.face, self.suit)
		
		
class Deck:
	
    # The constructor method for the Deck.
    # It takes no parameters.
    # It fills a deck with 52 unique card, and then uses random.shuffle to randomly order the deck
    # The counter will be used to indicate which card is at the "top" of the deck
    # i.e. all cards above counter will have been dealt
    def __init__(self):
        self.deck = []
        self.counter = 0
        global face
        global suit
        for the_face in face:
            for the_suit in suit:
                self.deck.append(Card(the_face, the_suit))
        for i in range(7):
            random.shuffle(self.deck)

    # Returns the top card of the deck if it exists (if we have not previously dealt 52 cards)
    # We could add in a method to automatically shuffle the deck if we reach this point
    def deal(self):
        if self.counter < 52:
            result = self.deck[self.counter]
            self.counter += 1
            return result

    # Randomly shuffles the deck array seven times.
    def shuffle(self):
        self.counter = 0
        for i in range(7):
            random.shuffle(self.deck)

    # tostring method for deck class.
    # Prints out all 52 cards in the deck, one per line.
    # We indicate with an X cards that have been dealt
    # << Current Top Card indicates which card is the current top of the deck.
    def __str__(self):
        result = ""
        for i in range(52):
            if i == self.counter:
                result += "%s << Current Top Card\n" % self.deck[i]
            elif i < self.counter:
                result += "%s X\n" % self.deck[i]
            else:
                result += "%s\n" % self.deck[i]
        return result

class Blackjack_Player:
    
    def __init__(self):
        self.hand = []
    

    def first_card(self):
        if(len(self.hand) > 0):
            return self.hand[0]
        else:
            return "Game not started"
    
    def add_card(self, card):
        self.hand.append(card)
     
    def get_hand(self):
        return self.hand
     
    def score(self):
        totalB = 0
        totalA = 0
        for card in self.hand:
            if(card.face <= 10):
                totalA = totalA + card.face
                totalB = totalB + card.face
            elif(card.face >= 11 and card.face <= 13):
                totalA = totalA + 10
                totalB = totalB + 10
            elif(card.face == 14):
                totalA = totalA + 11
                totalB = totalB + 1
        return (totalA, totalB)

    def __str__(self):
        # Change the tostring to include the value calculation!
        if(len(self.hand) == 0):
            return "No cards in hand"
        else:
            result = "%s" % self.hand[0]
            for i in range(1, len(self.hand)):
                result += ", %s" % self.hand[i]
            a, b = self.score()
            result += ", score=(%s, %s)" % (str(a), str(b))
            return result
    
    
class Blackjack_Game:
    
    def __init__(self):
        self.players = []
        self.activePlayers = 0
        self.player = Blackjack_Player()
        self.dealer = Blackjack_Player()
        self.Deck = Deck()
      
    def play_game(self):



        game_done = False
        card = self.Deck.deal()
        self.dealer.add_card(card)

        card = self.Deck.deal()
        self.player.add_card(card)
        while (not game_done):
           
       
            print("This is your current hand: %s" % self.player)
            print("This is what you see of the dealer: %s" % self.dealer)
            val = input("Do you want to get another card? (Y/N)")
            if(val == "Y" or val == "y"):
     
                a, b = self.dealer.score() 
                if(a < 17 and b < 17):
                    card = self.Deck.deal()
                    self.dealer.add_card(card)
                    if(a > 21 and b > 21):
                        print("player wins dealder busted")
                        return

                # Deal another card to the player here
                card = self.Deck.deal()
                self.player.add_card(card)
                a, b = self.player.score() 
                if(a > 21 and b > 21):
                    print("dealer wins player busted")
                    game_done = True
                    return
               
            else:
    
                scorep1, scorep2 = self.player.score()
                scored1, scored2 = self.dealer.score()
                if(scorep1 > scored1 and scorep1 > scored2 and scorep2 > scored1 and scorep2 > scored2):
                    print("player wins higher score")
                else:
                    print("dealer wins higher score")
                game_done = True
                

    def play_game_multiple(self, players):

        # create players and deal card
        for i in range(players):
            player = Blackjack_Player()
            self.players.append(player)
            card = self.Deck.deal()
            player.add_card(card)
            self.activePlayers += 1

        game_done = False
   

        while (not game_done):
            if(self.activePlayers <= 0):
                for i in range(len(self.players)):
                    self.isWinner(self.players[i], self.dealer, i)
                return

            a, b = self.dealer.score() 
            if(a < 17 and b < 17):
                card = self.Deck.deal()
                self.dealer.add_card(card)
                if(a > 21 and b > 21):
                    print("dealder busted")
                    return
            print("---------------")
            print("This is what you see of the dealer: %s" % self.dealer)

            for i in range(players):
                
                print("This is PLAYER %s current hand: %s" % (str(i), self.players[i]))
                a, b = self.players[i].score() 
                if(a <= 21 and b <= 21):
                    
                    val = input("Do you want to get another card? (Y/N)")
                    if(val == "Y" or val == "y"):

                # Deal another card to the player her

                        card = self.Deck.deal()
                        print("player %s got card: %s" % (str(i), card))
                        self.players[i].add_card(card)
                        a, b = self.players[i].score() 
                        if(a > 21 and b > 21):
                            print("player %s busted" % str(i))
                            self.activePlayers -= 1
                    else:
                        self.activePlayers -= 1
                    
                        
               
         

    def isWinner(self, p, d, i):
        scorep1, scorep2 = p.score()
        scored1, scored2 = d.score()
        if(scorep1 > scored1 and scorep1 > scored2 and scorep2 > scored1 and scorep2 > scored2):
            print("player %s wins higher score" % str(i))

        else:
            print("dealer beats player %s has higher score" % str(i))
         
       
    def __str__(self):
        return "Nothing to see here!"



def main():
    print("This will be our blackjack simulator!")
    print("Let us test the game!")
    #my_game = Blackjack_Game()
    #my_game.play_game_multiple(3)

    val = input("How many games?")
    for i in range(int(val)):
        print("_______")
        my_game = Blackjack_Game()
        my_game.play_game()
	
	
	
main()