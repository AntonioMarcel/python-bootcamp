class Player:
    def __init__(self, name):
        self.name = name
        self.pile = []

    def draw_card(self):
        try: 
            card_drawn = self.pile.pop(0)
            return card_drawn
        except IndexError: 
            print(f"No more cards in {self.name}'s pile!")
            return "error"
