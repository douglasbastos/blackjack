from blackjack.players.player import Player


class HumanPlayer(Player):

    def will_continue(self):
        cmd = input('C = continue ou S = Stop\n')
        if cmd.lower() == 'c':
            return True
        elif cmd.lower() == 's':
            return False
        else:
            print('Opção inválida')
            return self.will_continue()
