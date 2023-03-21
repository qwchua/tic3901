import pandas as pd

class Analyzer:

    def __init__(self,database):
        self.database = database

    def getLinesContributions(self,significantchangepercentage):
        destinationHash = self.database.getHashFromRef()
        
        hashes = self.findLineOwnersHashes(significantchangepercentage,destinationHash)

        commits = self.database.getCommitsMetaData()

        lines = []

        lineContent = self.database.getCommitContent(destinationHash,self.database.filename)

        i = 1
        for hash in hashes:
            line = {}
            line["linenum"] = i
            line["commithash"] = hash
            line["author"] = commits[hash]["author"]
            line["date"] = commits[hash]["date"]
            line["content"] = lineContent[i-1]
            lines.append(line)
            i+=1

        df = pd.DataFrame.from_dict(lines)

        results = {
            "type": "linecontributions",
            "filename": commits[destinationHash]["filename"],
            "data": df
        }

        return results

    def findLineOwnersHashes(self,SCthresholdpercent,destinationHash):

        #helper function
        def __applyChanges(commitHash):
                numOfParents = len(commitgraph.m_parents[currentCommitHash])
                
                if numOfParents == 1:
                    parentHash = commitgraph.m_parents[currentCommitHash][0]

                    #copy over parents's line ownership
                    currLineOwners = scoreboard[parentHash].copy()

                    hunks = diffs[(parentHash,currentCommitHash)]

                    linesOffSet = 0
                    
                    for hunk in hunks:

                        deletedLinesStack = []

                        for change in hunk.listOfLineChanges:
                            if change.type == "edited":
                                lineNum = change.lineNum
                                changepercent = change.significantChangePercent

                                if changepercent > SCthresholdpercent :
                                    currLineOwners[lineNum-1] = currentCommitHash

                            if change.type  == "added":
                                lineNum = change.lineNum
                                currLineOwners.insert(lineNum-1,commitHash)
                                continue

                            if change.type  == "deleted":
                                lineNum = change.lineNum
                                deletedLinesStack.append(lineNum+linesOffSet)
                                continue

                        while deletedLinesStack:
                            lineToDelete = deletedLinesStack.pop()
                            currLineOwners.pop(lineToDelete-1)

                        linesOffSet = linesOffSet + (hunk.linesAdded - hunk.linesDeleted)
                
                    return currLineOwners
                
                #This means this is a merge commit
                if numOfParents > 1:

                    parentHashes = commitgraph.m_parents[currentCommitHash]

                    parentOwners = []

                    finalOwner = []

                    for parent in parentHashes:
                        #copy over parents's line ownership
                        currLineOwners = scoreboard[parent].copy()

                        hunks = diffs[(parent,currentCommitHash)]

                        linesOffSet = 0

                        for hunk in hunks:

                            deletedLinesStack = []

                            for change in hunk.listOfLineChanges:
                                if change.type == "edited":
                                    lineNum = change.lineNum
                                    changepercent = change.significantChangePercent

                                    if changepercent > SCthresholdpercent :
                                        currLineOwners[lineNum-1] = None

                                if change.type  == "added":
                                    lineNum = change.lineNum
                                    currLineOwners.insert(lineNum-1,None)
                                    continue

                                if change.type  == "deleted":
                                    lineNum = change.lineNum
                                    deletedLinesStack.append(lineNum+linesOffSet)
                                    continue

                            while deletedLinesStack:
                                lineToDelete = deletedLinesStack.pop()
                                currLineOwners.pop(lineToDelete-1)

                            linesOffSet = linesOffSet + (hunk.linesAdded - hunk.linesDeleted)

                        parentOwners.append(currLineOwners)

                    transpose = [[parentOwners[j][i] for j in range(len(parentOwners))] for i in range(len(parentOwners[0]))]

                    for column in transpose:
                        mySet = set(column)

                        if len(mySet) == 1:
                            for val in mySet:
                                if val == None:
                                    finalOwner.append(currentCommitHash)
                                else:
                                    finalOwner.append(val)

                        else:
                            earliest = None
                            for val in mySet:
                                if earliest == None:
                                    earliest = val
                                elif val == None:
                                    continue
                                else:
                                    if val < earliest:
                                        earliest = val

                            finalOwner.append(earliest)

                    return finalOwner



        commitsMetaData = self.database.getCommitsMetaData()
        commitgraph = self.database.getCommitGraph()
        diffs = self.database.getCommitsDiffs()

        topsort = commitgraph.topologicalSort()

        scoreboard = {}
        
        for currentCommitHash in topsort:
            numOfParents = len(commitgraph.m_parents[currentCommitHash])
            
            #This means it is the initial commit or it is an orphan commit
            if numOfParents == 0:
                numOfLines = self.database.getNumOfLinesFromCommit(currentCommitHash,commitsMetaData[currentCommitHash]["filename"])
                
                result = []

                for _ in range(numOfLines):
                    result.append(currentCommitHash)

                scoreboard[currentCommitHash] = result
                continue

            if numOfParents > 0:
                sb = __applyChanges(currentCommitHash)
                scoreboard[currentCommitHash] = sb
    
            if currentCommitHash == destinationHash:
                return scoreboard[currentCommitHash]
        
        return scoreboard[topsort[-1]]

            


        




    