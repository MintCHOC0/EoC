from AnalysisTools import getPopulation
from Strategies import AllR, TitForTat
from GameTools import getWorst, getBest, Referee
from itertools import combinations

#Before Games Phase
p1 = AllR()
p2 = AllR()
p3 = AllR()
p4 = AllR()
p5 = AllR()
p6 = AllR()
p7 = AllR()
p8 = AllR()
p9 = AllR()
p10 = AllR()
p11 = AllR()
p12 = TitForTat()
p13 = TitForTat()
p14 = TitForTat()
p15 = TitForTat()

player_list = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15]

generation = 0
while (generation < 10):
    league = list(combinations(player_list, 2))
    generation += 1

    for team in league:
        game_cnt = 0
        referee = Referee()
        while (game_cnt < 10):
            game_cnt += 1
            player1 = team[0]
            player2 = team[1]

            # get choice
            data = referee.getData()
            c1 = player1.choice(1,data)
            c2 = player2.choice(2,data)

            # update log
            referee.p1_choice_log.append(c1)
            referee.p2_choice_log.append(c2)

            # distribute points
            if (c1 == 1 and c2 == 1):
                referee.p1_point += 3
                referee.p2_point += 3
            elif (c1 == 1 and c2 == 0):
                referee.p1_point += 5
                referee.p2_point += -1
            elif (c1 == 0 and c2 == 1):
                referee.p1_point += -1
                referee.p2_point += 5
            elif (c1 == 0 and c2 == 0) :
                referee.p1_point += 0
                referee.p2_point += 0
            # Error Case
            else :
                player1.my_point += -9999999
                player2.my_point += -9999999

        player1.my_point += referee.p1_point
        player2.my_point += referee.p2_point

        # initialization
        referee.resetData()
    # reproduction
    reproduce_s = getBest([(name,name.my_point) for name in player_list])
    eliminated_s = getWorst([(name,name.my_point) for name in player_list])
    flag = 0

    for i in range(3):
        player_list.remove(eliminated_s[i][0])
        player_list.append(reproduce_s[i][0].__class__())

    for p in player_list:
        p.my_choice_log = []
        p.my_point = 0
