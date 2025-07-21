from .player import Player
from .card import Card
class Game():
    def __init__(self, p1: Player, p2: Player):
         self.p1 = p1 
         self.p2 = p2

    def compare(self, card1: Card, card2: Card):
        if card1.value > card2.value:
              pass ### add card to player's pile logic
        elif card2.value > card1.value:
              pass ### add card to player's pile logic
        else:
              pass ### handle_war
              
    def round(self):
        card_p1 : Card = None
        card_p2 : Card = None
        while True:
                print(f"{self.p1.name}'s turn!")
                card_p1 = self.p1.draw_card()
                if card_p1 == "error":
                     break
                print(f"{card_p1.number} of {card_p1.suit} card was drawn!")

                print(f"{self.p2.name}'s turn!")     
                card_p2 = self.p2.draw_card()
                if card_p2 == "error":
                     break
                print(f"{card_p2.number} of {card_p2.suit} card was drawn!")
                self.compare()
                print("")


