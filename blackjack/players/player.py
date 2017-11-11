from blackjack import Blackjack


# TODO algumas coisas podem ser herdadas
class Player:
    cards = []
    opponent_cards = []

    def __init__(self):
        self.blackjack = Blackjack()

    @property
    def score(self):
        return self.blackjack.score(self.cards)

    @property
    def opponent_score(self):
        return self.blackjack.score(self.opponent_cards)

    def will_continue(self):
        cmd = input('C = continue ou S = Stop\n')
        if cmd.lower() == 'c':
            return True
        elif cmd.lower() == 's':
            return False
        else:
            print('Comando inválido')
            return self.will_continue()
