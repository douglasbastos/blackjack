import random
import uuid

from blackjack import Blackjack
from blackjack.pack import Pack
from blackjack.players.cpu_player import CpuPlayer
from blackjack.players.human_player import HumanPlayer


class Run:
    def __init__(self):
        self.pack = Pack()
        self.blackjack = Blackjack()
        self.players = []

        available_players = random.sample([HumanPlayer, CpuPlayer], k=2)
        for available_player in available_players:
            player = available_player()
            player.cards = self.init_deck()

            obj_player = {
                'player': player,
                'cards': player.cards,
                'score': player.score,
                'name': str(uuid.uuid4())
            }

            self.players.append(obj_player)

        self.main()

    def init_deck(self):
        return [self.pack.next(), self.pack.next()]

    def bust_card(self, cards):
        if self.blackjack.score(cards) > 21:
            return True
        return False

    def show_scores(self):
        for player in self.players:
            print(f"Player: {player['name']}")
            print([f'{card.rank} {card.suit}' for card in player['cards']])
            print(f"Score é: {player['player'].score}\n")
        print("/\/\/\/\//\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\\")
        print("VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV")

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
        for i, player_time in enumerate(self.players):
            player = player_time['player']

            if i != 0:
                player.opponent_cards = self.players[i-1]['cards']

            while True:
                self.show_scores()

                if self.bust_card(cards=player_time['cards']):
                    print('Você passou do limite de 21 pontos')
                    break

                player.cards = player_time['cards']
                if player.will_continue():
                    player_time['cards'].append(self.pack.next())
                else:
                    break


if __name__ == '__main__':
    Run()
