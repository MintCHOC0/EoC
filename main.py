from GameTools import PrisonerDilemma
from Players import AllC, AllB, AllR, TitForTat
from AnalysisTools import showPlayerGraph
print("Tool Import Complete\n")

# init enviornment
p1 = AllR()
p2 = AllR()
p3 = AllR()
p4 = AllR()
p5 = AllB()
p6 = AllB()
p7 = AllB()
p8 = AllC()
p9 = AllC()
p10 = AllC()
p11 = AllC()
p12 = TitForTat()
p13 = TitForTat()
p14 = TitForTat()
p15 = TitForTat()

list_player = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15]

# variables
meta_game_var = (10, 100, 3) # gener / match / repro_cnt
t_mat = (5, -1, 3, 0) # win-lose point matrix
msg_condition = {
    'showChoices' : False,
    'showPoints' : True,
    'showCounter' : True, # Shows the number of player classes that survived each generation.
    'saveData': True  # save player class and count in each generation.
    }

# make game Object
game = PrisonerDilemma(
    players = list_player,
    config_game = meta_game_var,
    tuple_match = t_mat
    )

for i in range(10):
    game.updateGeneration(msg_condition)
    print("=======================================")

print(game.df_gener)

# write and show
file_path = "./ignore/gamedata.csv"
game.df_gener.to_csv(file_path)
showPlayerGraph(file_path)