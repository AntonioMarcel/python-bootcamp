from .card import Card
from .player import Player
import random

class Deck:
    def __init__(self):
        self.deck = []

    def create_deck(self):
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        suits = ["♠", "♥", "♦", "♣"]
        numbers = [2,3,4,5,6,7,8,9,10,11,12,13,14]
        
        for s in suits:
            for k, n in enumerate(numbers):
                card = Card(ranks[k], s, n)
                self.deck.append(card)
        
    def print_deck(self):
        for card in self.deck:
            print(card.rank)
            print(card.suit)
            print(card.number)
            print("")

    def shuffle_deck(self):
        random.shuffle(self.deck)
    
    def deal_cards(self, p1: Player, p2: Player):
        # Deal cards initially
        p1.pile = self.deck[0:26]
        p2.pile = self.deck[26:]


