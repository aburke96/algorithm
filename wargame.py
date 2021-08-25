# Alexandra Burke
# cardgame.py
# 4/28/2021

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

class War_Player:
    
    def __init__(self):
        self.hand = []

    def num_cards(self):
        return len(self.hand)
    
    def add_card(self, card):
        self.hand.append(card)

    def get_card(self):
        return self.hand.pop()
     
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
    
    
class War_Game:
    
    def __init__(self):
        self.players = [War_Player(), War_Player(), War_Player(), War_Player()]
        self.activePlayers = 0
        self.Deck = Deck()
      
    def score_card(self, card):
        
        if(card.face <= 10):
            return card.face
        elif(card.face >= 11 and card.face <= 13):
            return 10
        elif(card.face == 14):
            return 11

    def score_table(self, cards):
       
        scores = [self.score_card(card) for card in cards]
        maxScore = max(scores)
        if scores[0] == maxScore:
            return 0
        if scores[1] == maxScore:
            return 1
        if scores[2] == maxScore:
            return 2
        return 3

    def play_game(self):

        end_game = False
        for i in range(13):
            for player in self.players:
                card = self.Deck.deal()
                player.add_card(card)
                
        while(end_game == False):

            cards = []
            for player in self.players:
                card = player.get_card()
                cards.append(card)

            winner = self.score_table(cards)
            player_winner = self.players[winner]
            for card in cards:
                player_winner.add_card(card)
            
            for player in self.players:
                if player.num_cards() == 0 or player.num_cards() > 34:
                    end_game = True
                    winner = self.check_winner(self.players)
                    print("The winner is player " + str(winner))
                

            

    def check_winner(self, players):

        num_cards = [player.num_cards() for player in players]
        maxScore = max(num_cards)
        if num_cards[0] == maxScore:
            return 0
        if num_cards[1] == maxScore:
            return 1
        if num_cards[2] == maxScore:
            return 2
        return 3        
        
    def __str__(self):
        return "Nothing to see here!"



def main():
    game = War_Game()
    game.play_game()
   
	
	
main()