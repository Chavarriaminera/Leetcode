import pandas as pd

def getDataframeSize(players):
    rows,cols=players.shape
    return [rows,cols]