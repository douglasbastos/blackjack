class CpuPlayer():

    def __init__(self, cpu_score, player_score):
        self.cpu_score = cpu_score
        self.player_score = player_score
        self.decision()

    def decision(self):
        pass
        # se player começou jogando(score_player > 0), decisão de jogar fica se eu tenho menos pontos que ele
        # se cpu começar jogando, quando fizer 18 pontos não pegar mais carta
        # se player_score for igual a zero, significa que o player ainda não jogou
