from collections import Counter

class AnalysisTool:
    def __init__(self, players):
        self.players = players
    
    def showSummary(self):
        counter = Counter([player.__class__.__name__ for player in self.players])
        print(counter)

    def showAll(self):
        for player in self.players:
            print(f"NAME : {player.__class__.__name__}")
            print(f"POINT : {player.point}\n")