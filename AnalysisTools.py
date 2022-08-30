import pandas as pd
from collections import Counter

def getPopulation(group):
    lt = list(Counter([p.code for p in group]).items())
    return lt
