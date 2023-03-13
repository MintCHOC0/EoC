from random import randrange, random
from math import exp, exp2
"""
chooseChoice() function of all classes is affected only by
current own score and list_choice,
current opponent's score and list_choice variables.
(Assume that Class dosen't know the result of previous opponent or future result.)
"""
class TestClass:
    def __init__(self):
        self.point = 0
        self.list_choice = []


class DefaultClass:
    def __init__(self):
        self.point = 0
        self.list_choice = []
    
    def __len__(self):
        return len(self.list_choice)

    def chooseChoice(self, opponent):
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


class FriedMan(DefaultClass):
    def chooseChoice(self, opponent):
        if 0 in opponent.list_choice: return 0
        else: return 1


class Joss(DefaultClass):
    def chooseChoice(self, opponent):
        if len(opponent.list_choice):
            if (random() < 0.1): return 0
            else: return opponent.list_choice[-1]
        else: return 1


class XOR(DefaultClass):
    def chooseChoice(self, opponent):
        if (len(opponent.list_choice)):
            return not(opponent.list_choice[-1])


class BetrayExp(DefaultClass):
    def getStack(self, opponent):
        stack = 0
        length = len(opponent)
        for i in range(length):
            if opponent.list_choice[length - i - 1] == 0: break
            stack+=1
        return stack
    
    def formula(self, stack):
        return (exp2(stack/8) - 1) / 4
    
    def chooseChoice(self, opponent):
        stack = self.getStack(opponent)
        if self.formula(stack) > random(): return 0
        else: return 1