from .player import Player
from .deck import Deck
from .card import Card

class Game:
    def __init__(self):
        self.p1 = Player("xarope_wars")
        self.p2 = Player("p.diddy")

    def compare(self, c1: Card, c2: Card):
        # print(c1.number) 
        # print(c2.number)

        if c1.number > c2.number:
            print(f"{self.p1.name} (P1) wins this turn!")
            # Move played card to last position
            self.p1.move_card()
            # Remove and receive card
            self.p2.lose_card(c2)
            self.p1.receive_card(c2)

        if c2.number > c1.number: 
            print(f"{self.p2.name} (P2) wins this turn!")
            # Move played card to last position
            self.p2.move_card()
            # Remove and receive card
            self.p1.lose_card(c1)
            self.p2.receive_card(c1)

        if c1.number == c2.number: 
            print("War!!!")

    def setup(self):
        # Create and shuffle deck
        d = Deck()
        d.create_deck()
        d.shuffle_deck()
        # Deal cards
        d.deal_cards(self.p1, self.p2)

        turn = 0
        while True:
            print(self.p1.pile)
            print(self.p2.pile)
            c1 = self.p1.play_card()
            c2 = self.p2.play_card()
            self.compare(c1, c2)
            print(turn)
            turn += 1
            if turn == 10:
                break

                #next: logic for war 
