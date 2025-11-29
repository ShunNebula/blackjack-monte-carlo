class Card:
    def __init__(self, suit: str, rank: str):
        self.suit = suit
        self.rank = rank
        self.value = self._get_value(rank)
    
    def _get_value(self, rank: str) -> int:
        if rank in ["J","Q","K"]:
            return 10
        elif rank == "A":
            return 11
        else:
            return int(rank)
    
    def __repr__(self) -> str:
        return f"{self.rank} of {self.suit}"
