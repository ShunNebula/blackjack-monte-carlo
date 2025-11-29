from card import Card
import random

class Deck:
    def __init__(self):
        self.cards = self._generate_deck()
    
    def _generate_deck(self) -> list:
        cards = []
        suits = ["Hearts","Diamonds","Clubs","Spades"]
        ranks = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

        for suit in suits:
            for rank in ranks:
                new_card = Card(suit, rank)
                cards.append(new_card)

        return cards
    
    def __repr__(self) -> str:
        return "\n".join([str(card) for card in self.cards])
    
    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self) -> Card:
        return self.cards.pop()

# deck = Deck()
# print(deck)
# deck.shuffle()
# print(deck)
# print(len(deck.cards))
# print("Заберём первую карту:")
# print(deck.deal_card())
# print("Заберём вторую карту:")
# print(deck.deal_card())
# print(len(deck.cards))