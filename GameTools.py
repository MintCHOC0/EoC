from itertools import combinations
from collections import Counter
from random import sample
from AnalysisTools import showAllChoices, showAllPoints, showNowPlayers
import copy
import pandas as pd

def copyPlayer(class_player, count):
    list_copycats = []
    for i in range(count):
        list_copycats.append(copy.deepcopy(class_player()))
    return list_copycats

class PrisonerDilemma:
    def __init__(self, players, config_game, tuple_match):
        self.players = players
        self.gener_cnt, self.match_cnt, self.repro_cnt = config_game
        self.list_league = list(combinations(self.players, 2))
        self.win_point, self.lose_point, self.tie_win_point, self.tie_lose_point = tuple_match
        
        # make default df
        self.init_name = dict(Counter([player.__class__.__name__ for player in self.players[:]]))
        print(self.init_name)
        self.dict_name = dict(Counter([player.__class__.__name__ for player in self.players]))
        self.df_gener = pd.DataFrame(columns=self.dict_name.keys())
        self.df_gener.loc[0] = self.dict_name.values()


    def returnFinalGeneration(self, showConditions):
        for cnt in range(self.gener_cnt):
            self.updateGeneration(showConditions, cnt)
    
    def updateGeneration(self, showConditions, cnt):
        # match per team
        self.list_league = list(combinations(self.players, 2))
        for team in self.list_league:
            for i in range(self.match_cnt):
                self.match(team)
            if (showConditions.get('showChoices')): showAllChoices(team[0], team[1])
            team[0].list_choice = []
            team[1].list_choice = []
        
        if (showConditions.get('showPoints')): showAllPoints(self.players)

        # check winner and loser
        self.players.sort(key = lambda x:x.point, reverse=True)
        list_loser_idx = self.getLoserIdx()
        list_winner_idx = self.getWinnerIdx()

        # reproduce winner and eliminate loser
        self.updatePlayers(list_loser_idx, list_winner_idx)
        
        if (showConditions.get('showCounter')): showNowPlayers(self.players, cnt + 1)
        if (showConditions.get('saveData')): self.appendDataFrame()

        # reset points
        for i in range(len(self.players)):
            self.players[i].point = 0

    def match(self, team):
        tuple_match = self.getChoice(team)
        tuple_point = self.getPoint(tuple_match)
        self.updatePoint(team, tuple_point)
        self.updateLog(team, tuple_match)

    def getChoice(self, team): return (team[0].chooseChoice(team[1]), team[1].chooseChoice(team[0]))
    
    def getPoint(self, tuple_match):
        if tuple_match == (1, 1): return (self.tie_win_point, self.tie_win_point)
        elif tuple_match == (1, 0): return (self.win_point, self.lose_point)
        elif tuple_match == (0, 1): return (self.lose_point, self.win_point)
        elif tuple_match == (0, 0): return (self.tie_lose_point, self.tie_lose_point)
        else: return (99999999, 99999999) #Check Error
    
    def updatePoint(self, team, tuple_point):
        team[0].point += tuple_point[0]
        team[1].point += tuple_point[1]

    def updateLog(self, team, tuple_match):
        team[0].list_choice.append(tuple_match[0])
        team[1].list_choice.append(tuple_match[1])
    
    def updatePlayers(self, list_loser_idx, list_winner_idx):
        for i in range(self.repro_cnt):
            self.players[list_loser_idx[i]] = self.players[list_winner_idx[i]].__class__()
    
    def getWinnerIdx(self):
        list_winner_idx = [] # winner
        temp = [] # tiebreaker
        cut_off = self.players[self.repro_cnt - 1].point
        
        for i in range(self.repro_cnt - 1): # pick clear winner
            if (self.players[i].point > cut_off): list_winner_idx.append(i)
            else: temp.append(i)
        
        for i in range(self.repro_cnt - 1, len(self.players)): # pick tiebreaker
            if (self.players[i].point < cut_off): break
            else: temp.append(i)
        
        list_winner_idx += sample(temp, self.repro_cnt - len(list_winner_idx)) # append random tiebreaker
        return list_winner_idx
    
    def getLoserIdx(self):
        list_loser_idx = []
        temp = []
        cut_off = self.players[-self.repro_cnt].point

        for i in range(1, self.repro_cnt):
            if (self.players[-i].point < cut_off): list_loser_idx.append(-i)
            else: temp.append(-i)
        
        for i in range(self.repro_cnt, len(self.players)):
            if (self.players[-i].point > cut_off): break
            else: temp.append(-i)
        
        list_loser_idx += sample(temp, self.repro_cnt - len(list_loser_idx))
        return list_loser_idx
    
    def appendDataFrame(self):
        self.dict_name = dict(Counter([player.__class__.__name__ for player in self.players]))
        self.df_gener.loc[len(self.df_gener)] = [0 for i in range(len(self.init_name))]
        for player, count in self.dict_name.items():
            self.df_gener.loc[len(self.df_gener) - 1, player] = count