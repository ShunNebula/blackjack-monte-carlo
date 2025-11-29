from card import Card
# from deck import Deck

class Hand:
    def __init__(self):
        self.cards = []
        
    def __repr__(self) -> str:
        return "\n".join([str(card) for card in self.cards])
    
    def add_card(self, card: Card):
        self.cards.append(card)

    def get_value(self) -> int:
        res = sum([card.value for card in self.cards])
        A_count = sum([1 for card in self.cards if card.rank == "A"])
        
        while res > 21 and A_count > 0:
            res -= 10
            A_count -= 1

        return res

# new_deck = Deck()
# new_deck.shuffle()
# new_hand = Hand()
# # проверка
# for i in range(5):
#     new_card = new_deck.deal_card()
#     new_hand.add_card(new_card)
#     print(new_hand.get_value())
# print(new_hand)