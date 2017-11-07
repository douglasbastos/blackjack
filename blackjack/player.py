class Player:
    score = 0
    opponent_score = 0

    def will_continue(self):
        cmd = input('C = continue ou S = Stop\n')
        if cmd.lower() == 'c':
            return True
        elif cmd.lower() == 's':
            return False
        else:
            # TODO: não temos teste nem implementação
            print('Comando inválido')
            return self.will_continue()
