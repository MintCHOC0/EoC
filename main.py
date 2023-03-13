from GameTools import PrisonerDilemma, copyPlayer
from Players import *
from AnalysisTools import showPlayerGraph
print("Tool Import Complete\n")

# init enviornment
p101 = copyPlayer(AllR, 20)
p102 = copyPlayer(AllB, 20)
p104 = copyPlayer(TitForTat, 20)
p105 = copyPlayer(FriedMan, 20)
p106 = copyPlayer(Joss, 20)
p107 = copyPlayer(XOR, 20)
p108 = copyPlayer(BetrayExp, 20)

list_player = p101 + p102 + p104 + p105 + p106 + p107 + p108

# variables
meta_game_var = (20, 100, 5) # gener / match / repro_cnt
t_mat = (5, -1, 3, 0) # win-lose point matrix
msg_condition = {
    'showChoices' : False,
    'showPoints' : True,
    'showCounter' : True, # Shows the number of player classes that survived each generation.
    'saveData': True,  # save player class and count in each generation.
    }

# make game Object

game = PrisonerDilemma(
    players = list_player,
    config_game = meta_game_var,
    tuple_match = t_mat
    )

game.returnFinalGeneration(msg_condition)

# write and show
file_path = "./ignore/gamedata.csv"
game.df_gener.to_csv(file_path)

if msg_condition.get('saveData'):
    showPlayerGraph(file_path)