import pandas as pd 

def getDataframeSize(players):
    cols,rows=players.shape
    return [cols,rows]