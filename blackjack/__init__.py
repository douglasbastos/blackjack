class Blackjack:
    PACK_SCORE_MAPPING = {
        'J': 10,
        'Q': 10,
        'K': 10,
        'A': 1
    }

    def score(self, cards):
        score = 0
        for card in cards:
            try:
                score += int(card.rank)
            except ValueError:
                if card.rank in self.PACK_SCORE_MAPPING:
                    score += self.PACK_SCORE_MAPPING[card.rank]

        return score

    def is_twenty_one(self, cards):
        score = self.score(cards)
        if score == 21:
            return True
        return False
