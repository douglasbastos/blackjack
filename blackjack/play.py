from blackjack.pack import Pack
from blackjack import Blackjack


class Run:
    def __init__(self):
        self.pack = Pack()
        self.blackjack = Blackjack()
        self.main()

    def init_deck(self):
        return [self.pack.next(), self.pack.next()]

    def bust_card(self, cards):
        if self.blackjack.score(cards) > 21:
            return True
        return False

    def my_score(self, cards):
        print(cards)
        print(f'Seu score é: {self.blackjack.score(cards)}\n')

    def main(self):
        cards = self.init_deck()

        while True:
            if self.bust_card(cards=cards):
                print('Você passou do limite de 21 pontos')
                break

            self.my_score(cards)

            cmd = input('C = continue ou S = Stop')
            if cmd.lower() == 'c':
                cards.append(self.pack.next())
            elif cmd.lower() == 's':
                break

        print(f'Sua pontuação final é {self.blackjack.score(cards)}')


if __name__ == '__main__':
    Run()
