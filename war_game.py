#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """
    def __init__(self):
        self.deck = [(i, j) for i in SUITE for j in RANKS] 
     
    def shuffle_deck(self):
        shuffle(self.deck)     
     
    def __str__(self):
        return f'Full_deck {self.deck}'
        
    def cutting_deck(self):
        return self.deck[:len(self.deck)//2], self.deck[len(self.deck)//2:]

class Hand:
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    def __init__(self, deck):
        self.deck = deck
        
    def add_cards(self, cards):
        self.deck.extend(cards)
        
    def remove_card(self):
        return self.deck.pop(0)

class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """
    def __init__(self, player_deck):
        self.player_deck = player_deck
        self.hand = Hand(self.player_deck)
        self.name = input("Insert your name: ").lower().capitalize()
        self.card = None
        
    def __str__(self):
        return f'Player {self.name} has {len(self.player_deck)} cards in hand'

    def card_out(self):
        try:
            self.card = self.hand.remove_card()
                      
        except IndexError:
            self.card = False
                      
    def cards_in(self, cards):
        self.hand.add_cards((cards))
        
          
def status():
    return f'{player_one} and {player_two}\n'
    
def grab_cards():
    player_one.card_out()
    player_two.card_out()
    
######################
#### GAME PLAY ######
######################
print("Welcome to War, let's begin...\n")

# deck spliting for players
deck = Deck()
deck.shuffle_deck()
deck1, deck2 = deck.cutting_deck()

# player objects definition

player_one = Player(deck1)
player_two = Player(deck2)

# first cards in hands report
print(status())

# first card on the table
grab_cards()

# start playing loop
war_counter = 0
round_counter = 0

while player_one.card and player_two.card:
    # list for the war
    table_cards = []
    
    print(f'{player_one.name} has: {player_one.card}')
    print(f'{player_two.name} has: {player_two.card}')
    
    # war exception definition
    # RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'
    round_counter += 1
    if RANKS.index(player_one.card[1]) == RANKS.index(player_two.card[1]):
        war_counter += 1
        print('Cards are same. The war is starting!\n')
        table_cards.extend((player_one.card, player_two.card))
        
        if len(player_one.player_deck) < 3 or len(player_two.player_deck) <3:
            print("Nedostatek karet v balíčku.")
            break
        else:
            for i in range(3):
                grab_cards()
                table_cards.extend((player_one.card, player_two.card))
                
        # who is winner of this war?        
            grab_cards()        

            if RANKS.index(player_one.card[1]) > RANKS.index(player_two.card[1]):
                table_cards.extend((player_one.card, player_two.card))
                player_one.cards_in(table_cards)
                print(f"{player_one.name} is winner!!!\n")
               
                                     
            else: 
                table_cards.extend((player_one.card, player_two.card))
                player_two.cards_in(table_cards)
                print(f"{player_two.name} is winner!!!\n")
                
                
        
    else:
        if RANKS.index(player_one.card[1]) > RANKS.index(player_two.card[1]):
            player_one.cards_in((player_one.card, player_two.card))
            print(f"{player_one.name} is winner!!!\n")
            
        else: 
            player_two.cards_in((player_one.card, player_two.card))
            print(f"{player_two.name} is winner!!!\n")
            
        

    print(status())
    grab_cards()

print(f"Rounds: {round_counter}")    
print(f"War loop is happen: {war_counter}")

    
# Use the 3 classes along with some logic to play a game of war!
