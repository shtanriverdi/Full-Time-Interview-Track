class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        minimum_consecutive_cards = float("inf")
        index_lookup = {}
        
        for index, card in enumerate(cards):
            if card in index_lookup:
                difference = index - index_lookup[card] + 1
                if difference < minimum_consecutive_cards:
                    minimum_consecutive_cards = difference
            index_lookup[card] = index

        if minimum_consecutive_cards == float("inf"):
            return -1
        
        return minimum_consecutive_cards
