import pandas as pd

class ReadStrategy:

    def __init__(self, pscore, dscore):
        self.pscore = pscore
        self.dscore = dscore

    def getStrategy(rowidx, colidx):
        df = pd.read_csv('strategy.csv')
        df.head()
        df.set_index("Pscore", inplace=True)
        return (df.loc[rowidx, str(colidx)])

    def getSoftStrategy(rowidx, colidx):
        df = pd.read_csv('softstrategy.csv')
        df.head()
        df.set_index("Pscore", inplace=True)
        return (df.loc[rowidx, str(colidx)])

    # print(getStrategy(21, 2))
    # print(getSoftStrategy(18, 3))


    # running simulation 100,000 times


