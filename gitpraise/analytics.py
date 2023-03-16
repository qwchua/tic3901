class Analytics:

    def __init__(self,database):
        self.database = database

    def getFinalContributions(self,significantchangepercentage):
        cmd = self.database.getCommitsMetaData()
        cg = self.database.getCommitGraph()
        cd = self.database.getCommitsDiffs()
        




    