from utils import Deck, Game, Player

p1 = Player("xarope")
p2 = Player("marquito")

d = Deck()

d.deal_cards(p1,p2)
#d.print_deck()

g = Game()
g.round(p1,p2)


# print(p1.pile[0].suit)
# print(p1.pile[0].number)
# print(p1.pile[0].value)
# print(p2.pile[0].suit)
# print(p2.pile[0].number)
# print(p2.pile[0].value)