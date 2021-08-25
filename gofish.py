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

class Fish_Player:
    
    def __init__(self):
        self.hand = []
        self.points = 0

    def get_points(self):
        return self.points

    def check_for_four(self):
        maxIndex = self.num_cards()
        counts = []
        for i in range (len(self.hand)):
            counts.append(0)
            for c in self.hand:
                if self.hand[i].face == c.face:
                    counts[i] += 1
        print(counts)
        idxadj = 0
        for i in range (len(counts)):
            if counts [i] == 4:
                self.hand.pop(i-idxadj)
                idxadj += 1 
                self.points += 1
                

    def num_cards(self):
        return len(self.hand)
    
    def add_card(self, card):
        self.hand.append(card)

    def get_card(self, val):
        return self.hand.pop(val)

    def find_card(self, card):
        cards = []
        for c in self.hand:
            if c.face == card.face:
                self.hand.remove(c)
                cards.append(c)
        return cards
     
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
    
    
class Fish_Game:
    
    def __init__(self):
        self.players = [Fish_Player(), Fish_Player()]
        self.lastcard = 0
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
        turn = 0 
        for i in range(7):
            for player in self.players:
                card = self.Deck.deal()
                player.add_card(card)
                
        while(len(self.players[0].hand) > 0 and len(self.players[1].hand) > 0):
            print("player[0] %s" % self.players[0])
            print("player[1] %s" % self.players[1])
            print("_______________")
            if turn == 0:
                self.human_play()
                self.players[0].check_for_four()
                turn = 1
            else:
                self.computer_play()
                self.players[1].check_for_four()
                turn = 0
            
        if (self.players[0].get_points() > self.players[1].get_points()):            
            print("\n\nTHE HUMAN HAS WON!")        
        elif (self.players[0].get_points() < self.players[1].get_points()):            
            print("\n\nTHE COMPUTER HAS WON!")        
        else:            
            print("\n\nTHE GAME IS A TIE!")

    def computer_play(self):
        index = self.computer_ask_index()
        card = self.players[1].get_card(index)
        print("Computer asked for %s " % card)
        gotcards = self.players[0].find_card(card)
        if len(gotcards) == 0:
            self.players[1].add_card(card)
            card = self.Deck.deal()

            self.players[1].add_card(card)
            return 
        for c in gotcards:
            self.players[1].add_card(c) 
        self.players[1].add_card(card) 
        
    def computer_ask_index(self):
        maxIndex = self.players[1].num_cards
        counts = []
        for i in range (len(self.players[1].hand)):
            counts.append(0)
            for c in self.players[1].hand:
                if self.players[1].hand[i].face == c.face:
                    counts[i] += 1
        #print(counts)
        max = 0
        idx = 0
        for i in range (len(counts)):
            if counts [i] > max:
                max = counts[i]
                idx = i
        return idx     


    def human_play(self):
        val = input("Enter your value: ")
        card = self.players[0].get_card(int(val))
        print("Human asked for %s " % card)
        gotcards = self.players[1].find_card(card)
        print("Found cards %s " % gotcards)
        if len(gotcards) == 0:
            print("Go Fish")
            self.players[0].add_card(card)
            card = self.Deck.deal()
            self.players[0].add_card(card)
            return
        for c in gotcards:
            self.players[0].add_card(c)   
        self.players[0].add_card(card)  

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
    game = Fish_Game()
    game.play_game()
   
	
	
main()