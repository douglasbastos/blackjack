from blackjack.pack import Pack
from blackjack.blackjack import Blackjack


class Run:
    def __init__(self):
        self.pack = Pack()
        self.main()

    def init_deck(self):
        return [self.pack.next(), self.pack.next()]

    def bust_card(self, twenty_one, cards):
        if twenty_one.score() > 21:
            return True
        return False

    def main(self):
        cards = self.init_deck()

        while True:
            twenty_one = Blackjack(cards)
            if self.bust_card(twenty_one=twenty_one, cards=cards):
                print('Você passou do limite de 21 pontos')
                break

            print(cards)
            print(f'Seu score é: {twenty_one.score()}')

            cmd = input('C = continue ou S = Stop')
            if cmd.lower() == 'c':
                cards.append(self.pack.next())
            elif cmd.lower() == 's':
                break

        print(f'Sua pontuação final é {twenty_one.score()}')


if __name__ == '__main__':
    Run()
