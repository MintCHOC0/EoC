import random
rl = [("p1",100),
      ("p2",80),
      ("p3",700),
      ("p4",80),
      ("p5",190),
      ("p6",500),
      ("p7",500),
      ("p8",400),
      ("p9",400),
      ("p10",900),
      ("p11",400),
      ("p12",50),
      ("p13",100),
      ("p14",100),
      ("p15",350),
      ("p16",100),]

def getBest(result_list):
    winner_list = []
    result_list.sort(key=lambda x : x[1])

    for i in range(3-1):
        if (result_list[-i-1][1] > result_list[-3][1]): winner_list.append(result_list[-i-1])
    temp_winner = [target for target in result_list if result_list[-3][1] == target[1]]
    winners = random.sample(temp_winner, 3 - len(winner_list))
    for winner in winners: winner_list.append(winner)

    return winner_list

def getWorst(result_list):
    loser_list = []
    result_list.sort(key=lambda x : x[1])

    for i in range(3-1):
          if (result_list[i][1] < result_list[3-1][1]) : loser_list.append(result_list[i])
    temp_loser = [target for target in result_list if result_list[3-1][1] == target[1]]
    losers = random.sample(temp_loser,3-len(loser_list))
    for loser in losers : loser_list.append(loser)

    return loser_list

class Referee:
    def __init__(self):
        self.p1_choice_log = []
        self.p2_choice_log = []
        self.p1_point = 0
        self.p2_point = 0

    def getData(self):
        data0 = self.p1_choice_log
        data1 = self.p2_choice_log
        data2 = self.p1_point
        data3 = self.p2_point
        return [data0,data1,data2,data3]

    def resetData(self):
        self.p1_choice_log = []
        self.p2_choice_log = []
        self.p1_point = 0
        self.p2_point = 0
