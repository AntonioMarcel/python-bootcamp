from .card import Card
from .player import Player
import random 

class Deck:
    def __init__(self):
        self.deck = []

    def create_deck(self):
        numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        values = [2,3,4,5,6,7,8,9,10,11,12,13,14]
        suits = ["♠", "♥", "♦", "♣"]
        for k, suit in enumerate(suits):         
            card = {}
            for l, value in enumerate(values):
                card = Card(suit, value, numbers[l])
                self.deck.append(card)


        # for k, suit in enumerate(suits):         
        #     card = {}
        #     for l, value in enumerate(values):
        #         card = {'suit': suit, 'value': value, 'number': numbers[l]}
        #         deck.append(card)

    def shuffle_deck(self):
        random.shuffle(self.deck)
    
    def print_deck(self):
        for card in self.deck:
            print(card.suit)
            print(card.value)
            print(card.number)
            print("")

    def deal_cards(self, p1: Player, p2: Player):
        # Create and shuffle deck
        self.create_deck()
        self.shuffle_deck()
        # Divide the cards evenly
        p1.pile = self.deck[0:26]
        p2.pile = self.deck[26:]





