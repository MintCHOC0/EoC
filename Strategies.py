#args order : my_choice_log,opponent_choice_log,.. <- give dictionary
from random import randrange

class DummyClass:
    def __init__(self):
        self.my_point = 0
        self.my_choice_log = []
        self.code = "AR"

    def choice(self,data):
        pass

class AllR:
    def __init__(self):
        self.my_point = 0
        self.my_choice_log = []
        self.code = "AR"

    def choice(self,self_p,data):
        return randrange(2)


class TitForTat:
    def __init__(self):
        self.my_point = 0
        self.my_choice_log = []
        self.code = "TFT"

    def choice(self,self_p,data):
        if (self_p == 1): oppo_list = data[1]
        else : oppo_list = data[0]
        if (len(oppo_list) < 1): return 1
        else : return oppo_list[-1]

class Friedman:
    def __init__(self):
        self.my_point = 0
        self.my_choice_log = []
        self.code = "FM"

    def choice(self,data):
        return 0 if 0 in data[1] else 1

