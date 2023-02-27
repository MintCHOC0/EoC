from random import randrange

"""
chooseChoice() function of all classes is affected only by
current own score and list_choice,
current opponent's score and list_choice variables.
(Assume that Class dosen't know the result of previous opponent or future result.)
"""
class DefaultClass:
    def __init__(self):
        self.point = 0
        self.list_choice = []
    
    def chooseChoice(self):
        pass



class AllC(DefaultClass):
    def chooseChoice(self, opponent):
        return 1


class AllB(DefaultClass):
    def chooseChoice(self, opponent):
        return 0


class AllR(DefaultClass):
    def chooseChoice(self, opponent):
        return randrange(2)


class TitForTat(DefaultClass):
    def chooseChoice(self, opponent):
        if len(opponent.list_choice) < 1: return 1
        else: return opponent.list_choice[-1]