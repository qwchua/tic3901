class Analytics:

    def __init__(self,database):
        self.database = database

    def getFinalContributions(self,significantchangepercentage):
        commitsMetaData = self.database.getCommitsMetaData()
        commitgraph = self.database.getCommitGraph()
        diffs = self.database.getCommitDiffs()

        topsort = commitgraph.topologicalSort()

        scoreboard = {}
        
        for currentCommitHash in topsort:

            print(f'Doing: {currentCommitHash}')

            numOfParents = len(commitgraph.m_parents[currentCommitHash])
            
            #This means it is the initial commit or it is an orphan commit
            if numOfParents == 0:
                numOfLines = commitsMetaData[currentCommitHash]["numOfLines"]
                
                result = []

                for _ in range(numOfLines):
                    result.append(currentCommitHash)

                scoreboard[currentCommitHash] = result
                continue

            if numOfParents > 0:
                sb = __applyChanges(currentCommitHash)
                scoreboard[currentCommitHash] = sb

    
        def __applyChanges(commitHash):
            numOfParents = len(commitgraph.m_parents[currentCommitHash])
            
            if numOfParents == 1:
                parentHash = commitgraph.m_parents[currentCommitHash][0]
                parentLineOwners = scoreboard[parentHash]

                hunks = diffs[(parentHash,currentCommitHash)]
                
                for hunk in hunks:
                    pass
            
            #if commit has more than 1 parent, it is a merge commit
            if numOfParents > 1:
                pass


            print(scoreboard)
        




    