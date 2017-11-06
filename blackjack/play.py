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
        print([f'{card.rank} {card.suit}' for card in cards])
        print(f'Seu score é: {self.blackjack.score(cards)}\n')

    def cpu_score(self, cards):
        print([f'{card.rank} {card.suit}' for card in cards])
        print(f'CPU score é: {self.blackjack.score(cards)}\n')

    def play_again(self):
        # TODO: não temos teste para isso ainda
        cmd = input('Deseja jogar novamente: y/n\n')
        if cmd.lower() == 'y':
            self.main()
        elif cmd.lower() == 'n':
            print('\n!!! Jogo encerrado !!!\n')
        else:
            print('Comando inválido')
            self.play_again()

    def cpu_player(self):
        cpu_cards = [self.pack.next(), self.pack.next()]
        while True:
            self.cpu_score(cpu_cards)

    def main(self):
        cards = self.init_deck()

        while True:
            if self.bust_card(cards=cards):
                print('Você passou do limite de 21 pontos')
                break

            self.my_score(cards)

            cmd = input('C = continue ou S = Stop\n')
            if cmd.lower() == 'c':
                cards.append(self.pack.next())
            elif cmd.lower() == 's':
                break
            else:
                # TODO: não temos teste nem implementação
                print('Comando inválido')

        print(f'Sua pontuação final é {self.blackjack.score(cards)}')
        self.cpu_player()
        # self.play_again()


if __name__ == '__main__':
    Run()
