from .card import Card

class Player:
    def __init__(self, name):
        self.name = name
        self.pile = []

    def play_card(self):
        return self.pile[0]
    
    def receive_card(self, c: Card):
        self.pile.append(c)

    def lose_card(self, c: Card):
        self.pile.remove(c)

    def move_card(self):
        # Moves played card to last position in list
        self.pile.append(self.pile.pop(0))

