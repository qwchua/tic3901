#analyzer.py

import pandas as pd
from gitpraise.exception import *

class Analyzer:

    def __init__(self,database):
        self.database = database

    def getLinesContributions(self,significantchangepercentage):
        destinationHash = self.database.getDestinationHash()
        
        hashes = self.findLineOwnersHashes(significantchangepercentage,destinationHash)

        commits = self.database.getCommitsMetaData()

        lines = []

        lineContent = self.database.getCommitContent(destinationHash,self.database.filename)

        #abit hacky,delete last blank line in file, similar to git blame, they dont blame the last blank line
        if len(lineContent[-1]) == 0:
            lineContent.pop()
            
        # i = 1
        # for hash in hashes:
        #     line = {}
        #     line["linenum"] = i
        #     line["commithash"] = hash
        #     line["author"] = commits[hash]["author"]
        #     line["date"] = commits[hash]["date"]
        #     line["content"] = lineContent[i-1]
        #     lines.append(line)
        #     i+=1

        i = 1
        for l in lineContent:
            hash = hashes[i-1]
            line = {}
            line["linenum"] = i
            line["commithash"] = hash
            line["author"] = commits[hash]["author"]
            line["date"] = commits[hash]["date"]
            line["content"] = l
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

                    # for hunk in hunks:
                    #     print(hunk.linesAdded)
                    #     print(hunk.linesDeleted)
                    #     for l in hunk.listOfLineChanges:
                    #         print(l)

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

                    #dirty hack
                    numOfLinesOfCurrentHash = self.database.getNumOfLinesFromCommit(currentCommitHash,commitsMetaData[currentCommitHash]["filename"])

                    for parent in parentHashes:
                        #copy over parents's line ownership
                        currLineOwners = scoreboard[parent].copy()

                        hunks = diffs[(parent,currentCommitHash)]

                        # if commitHash== "fd36a13cc46032cb412a01ad275cc897e9f58ed2" and parent=="30d1351590ab6af58263116924e80bfacde575f6":
                        #     for hunk in hunks:
                        #         print(hunk.linesAdded)
                        #         print(hunk.linesDeleted)
                        #         for l in hunk.listOfLineChanges:
                        #             print(l)

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

                        # if(len(currLineOwners) != numOfLinesOfCurrentHash):
                        #     raise MergeError(f"Something went wrong when merging: {parent} to {currentCommitHash}")

                        
                        #DIRTYHACK when 1 branch change file, 1 branch continue to edit, finally merge,
                        # example: in flask, git diff --unified=0 --minimal 871e6d6a9d1c453716f68e4e88268961d067b26d 2a2134974cc8d39f64c89b40dd5999e0c3ec01ae -- flask/__init__.py src/flask/__init__.py
                        # example: in flask hash: 216151c8a3c02e805fe5d1824708253f7e01e77f parents: 5e1ced3c055f7eb567bf7266c98de3d44ceea1b4 0e1e9a04aaf29ab78f721cfc79ac2a691f6e3929 src/flask/json/__init__.py
                        # if(len(currLineOwners) == numOfLinesOfCurrentHash):
                        parentOwners.append(currLineOwners)


                    it = iter(parentOwners)
                    the_len = len(next(it))
                    if not all(len(l) == the_len for l in it):
                        raise MergeError(f"Something went wrong when merging at {currentCommitHash}")

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

        #only 1 node
        if len(commitsMetaData) == 1:
            numOfLines = self.database.getNumOfLinesFromCommit(destinationHash,commitsMetaData[destinationHash]["filename"])
                
            result = []

            for _ in range(numOfLines):
                result.append(destinationHash)
            return result

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