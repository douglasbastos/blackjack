class TwentyOne:
    # TODO: trocar para blackjack
    def __init__(self, cards):
        self.cards = cards

    PACK_SCORE_MAPPING = {
        'J': 10,
        'Q': 10,
        'K': 10,
        'A': 1
    }

    def score(self):
        score = 0
        for card in self.cards:
            try:
                score += int(card.rank)
            except ValueError:
                if card.rank in self.PACK_SCORE_MAPPING:
                    score += self.PACK_SCORE_MAPPING[card.rank]

        return score

    def is_twenty_one(self):
        score = self.score()
        if score == 21:
            return True
        return False
