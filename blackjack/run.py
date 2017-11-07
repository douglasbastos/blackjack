import random

from blackjack.cpu_player import CpuPlayer
from blackjack.pack import Pack
from blackjack import Blackjack
from blackjack.player import Player


class Run:
    def __init__(self):
        self.pack = Pack()
        self.blackjack = Blackjack()

        self.players = random.sample([Player, CpuPlayer], k=2)
        self.players = [CpuPlayer] # todo: para test
        self.main()

    def init_deck(self):
        return [self.pack.next(), self.pack.next()]

    def bust_card(self, cards):
        if self.blackjack.score(cards) > 21:
            return True
        return False

    def player_score(self, cards):
        print([f'{card.rank} {card.suit}' for card in cards])
        print(f'Seu score é: {self.blackjack.score(cards)}\n')
        return self.blackjack.score(cards)

    # def play_again(self):
    #     # TODO: não temos teste para isso ainda
    #     cmd = input('Deseja jogar novamente: y/n\n')
    #     if cmd.lower() == 'y':
    #         self.main()
    #     elif cmd.lower() == 'n':
    #         print('\n!!! Jogo encerrado !!!\n')
    #     else:
    #         print('Comando inválido')
    #         self.play_again()

    def main(self):
        for player_time in self.players:
            cards = self.init_deck()
            player = player_time()

            while True:
                if self.bust_card(cards=cards):
                    print('Você passou do limite de 21 pontos')
                    break

                player.score = self.player_score(cards)
                player_will_continue = player.will_continue()
                if player_will_continue:
                    cards.append(self.pack.next())
                else:
                    break

        print(f'Sua pontuação final é {self.blackjack.score(cards)}')
        # self.play_again()


if __name__ == '__main__':
    Run()
