import subprocess
import re
from datetime import datetime
from gitpraise.graph import Graph
from gitpraise.levenstein import levenshteinDistanceDP

class Database:

    def __init__(self):
        self.filename = None
        self.since = None
        self.commitsMetadata = None
        self.commitGraph = None
        self.commitDiffs = None
        #self.cwd = "repos-for-testing/testing_scoreboard_analytics"
        self.cwd = "repos-for-testing/2048"

    def addCommitsMetaData(self):
        pass
    def addCommitGraph(self):
        pass
    def addCommitsDiffs(self):
        pass
    
    def getCommitsMetaData(self):
        return self.commitsMetadata
    
    def getCommitGraph(self):
        return self.commitGraph
    
    def getCommitDiffs(self):
        return self.commitDiffs

class GitDatabase(Database):
    def __init__(self):
        super().__init__()

    def addCommitsMetaData(self,numOfLines=False):
        gitlogcommand = "git log --all --format=%H,%an,%ci --simplify-merges " + self.filename

        unparsedlog = subprocess.run(
            gitlogcommand,
            shell=True,
            cwd= self.cwd,
            capture_output=True,
            text=True,
            )
        unparsedlog = unparsedlog.stdout
        commits = self.__parseGitLog(unparsedlog)

        if numOfLines == True:
            for commit in commits:
                numOfLines = self.__getNumOfLines(commit)
                commits[commit]["numOfLines"] = numOfLines 
        self.commitsMetadata = commits
                

    def __parseGitLog(self, log):
        commits = {}
        lines = log.split("\n")
        for l in lines:
            if len(l) > 0: 
                collection = l.split(",")
                commithash = collection[0]
                author = collection[1]
                date = datetime.strptime(collection[2], '%Y-%m-%d %H:%M:%S %z')
                commits[commithash] = {"author": author, "date": date}
        return commits
    
    def __getNumOfLines(self, commitHash):
            gitcommand = "git diff --numstat " + commitHash + " 4b825dc642cb6eb9a060e54bf8d69288fbee4904 " + self.filename
            unparsedlog = subprocess.run(
                    gitcommand,
                    shell=True,
                    cwd=self.cwd,
                    capture_output=True,
                    text=True,
                )
            unparsedlog = unparsedlog.stdout
            collection = unparsedlog.split()
            return int(collection[1])

    
    def addCommitGraph(self):
        gitlogcommand = "git log --all --format=%H,%P,%an --simplify-merges " + self.filename

        unparsedlog = subprocess.run(
            gitlogcommand,
            shell=True,
            cwd=self.cwd,
            capture_output=True,
            text=True,
        )
        unparsedlog = unparsedlog.stdout
        edges = self.__parseGitLogWithParents(unparsedlog)
        graph = Graph()

        for e in edges:
            newcommit = e["hash"]
            oldcommits = e["parents"]
            for oldcommit in oldcommits:
                graph.add_edge(oldcommit,newcommit)

        self.commitGraph = graph

    
    def __parseGitLogWithParents(self, log):
        edges = []
        lines = log.split("\n")
        for l in lines:
            if len(l) > 0: 
                collection = l.split(",")
                commithash = collection[0]
                parenthashes = collection[1]
                if len(parenthashes) > 0:
                    parenthashes = parenthashes.split()
                else:
                    parenthashes = []
                
                edges.append({"hash": commithash, "parents": parenthashes})
        return edges

    def addCommitsDiffs(self):
        diffs = {}

        g = self.commitGraph
        adjList = g.m_adj_list
        
        for fromHash, toHashs in adjList.items():
            for toHash in toHashs:
                gitdiffcommand = f"git diff --unified=0 --minimal {fromHash} {toHash} {self.filename}"
                unparsedlog = subprocess.run(
                    gitdiffcommand,
                    shell=True,
                    cwd=self.cwd,
                    capture_output=True,
                    text=True,
                )
                unparsedlog = unparsedlog.stdout

                diff = self.__parseGitDiff(unparsedlog)
                diffs[(fromHash,toHash)] = diff

        self.commitDiffs = diffs


    # def __parseGitDiff(self, log):
    #     class Hunk:
    #         def __init__(self,oldStart,newStart,lines=None):
    #             self.oldStart = oldStart
    #             self.newStart = newStart
    #             if lines is None:
    #                 lines = []
    #             self.lines = lines
            
    #         def addLine(self,line):
    #             self.lines.append(line)

    #         def getLines(self):
    #             return self.lines

    #     lines = log.split("\n")

    #     hunks = []
    #     oldSeen = {}
    #     newSeen = {}

    #     currHunkIdx = -1
    #     oldPtr = 0
    #     newPtr = 0

    #     for line in lines[4:]:
    #         if(line.startswith("@@")):
    #             oldStart = re.findall(r'[-]\d+', line)
    #             oldStart = oldStart[0][1:]
    #             oldStart = int(oldStart)

    #             newStart = re.findall(r'[+]\d+', line)
    #             newStart = newStart[0][1:]
    #             newStart = int(newStart)

    #             oldPtr = oldStart
    #             newPtr = newStart
                
    #             h = Hunk(oldStart,newStart,None)
    #             hunks.append(h)
    #             currHunkIdx += 1

    #         if line.startswith("-"):
    #             hunks[currHunkIdx].addLine(line)

    #             #remove + or - before the line
    #             line = line[1:]

    #             #remove trailing space before line
    #             line = line.lstrip()
                
    #             # add into oldSeen if line is not empty
    #             if len(line) > 0:
    #                 oldSeen[line] = oldPtr

    #             oldPtr += 1


    #         if line.startswith("+"):
    #             hunks[currHunkIdx].addLine(line)

    #             #remove + or - before the line
    #             line = line[1:]

    #             #remove trailing space before line
    #             line = line.lstrip()

    #             # add into newSeen if line is not empty
    #             if len(line) > 0:
    #                 newSeen[line] = newPtr

    #             newPtr += 1

    #         if len(line) == 0:
    #             continue

    #     # for x, y in oldSeen.items():
    #     #     print(x, y)

    #     changes = []

    #     class Change:
    #         def __init__(self,oldLineNum,newLineNum,significantChangePercentage):
    #             self.oldLineNum = oldLineNum
    #             self.newLineNum = newLineNum
    #             self.significantChangePercentage = significantChangePercentage

    #         def __eq__(self, other):
    #             return (self.oldLineNum == other.oldLineNum and self.newLineNum == other.newLineNum and self.significantChangePercentage == other.significantChangePercentage)

    #     for hunk in hunks:

    #         oldqueue = []
    #         newqueue = []

    #         oldLineNum = hunk.oldStart
    #         newLineNum = hunk.newStart

    #         for l in hunk.getLines():
    #             if(l.startswith("-")):
    #                 l = l[1:]
    #                 #remove trailing space before line
    #                 l = l.lstrip()
    #                 oldqueue.append(l)
                
    #             if(l.startswith("+")):
    #                 l = l[1:]
    #                 #remove trailing space before line
    #                 l = l.lstrip()
    #                 newqueue.append(l)
            
    #         while len(oldqueue) > 0:
    #             oldLineContent = oldqueue.pop(0)

    #             #line moved
    #             if oldLineContent in newSeen:
    #                 newLineNum = newSeen[oldLineContent]

    #                 change = Change(oldLineNum,newLineNum,0)

    #                 if change not in changes:
    #                     changes.append(change)

    #                 oldLineNum += 1
    #                 continue

    #             #line deleted
    #             if len(newqueue) == 0:
    #                 changes.append(Change(oldLineNum,None,0))
    #                 oldLineNum += 1
    #                 continue

    #             #line changed
    #             while len(newqueue) > 0:
    #                 newLineContent = newqueue.pop(0)

    #                 if newLineContent in oldSeen:
    #                     oldLineNum = oldSeen[newLineContent]
    #                     changes.append(Change(oldLineNum,newLineNum,0))
    #                     newLineNum += 1
    #                     continue
                    
    #                 else:
    #                     ld = levenshteinDistanceDP(oldLineContent,newLineContent)

    #                     oldContentLength = len(oldLineContent)
    #                     #significant change percentage
    #                     if oldContentLength == 0:
    #                         oldContentLength = 1

    #                     sfcp = ld / oldContentLength

    #                     changes.append(Change(oldLineNum,newLineNum,sfcp))

    #                     oldLineNum += 1
    #                     newLineNum += 1
    #                     break

    #         while len(newqueue) > 0:
    #             newLineContent = newqueue.pop(0)

    #             #line moved
    #             if newLineContent in oldSeen:
    #                     oldLineNum = oldSeen[newLineContent]

    #                     change = Change(oldLineNum,newLineNum,0)

    #                     if change not in changes:
    #                         changes.append(change)

    #                     newLineNum += 1

    #             #line added
    #             else:
    #                 changes.append(Change(None,newLineNum,0))
    #                 oldLineNum += 1
    #                 newLineNum += 1
            
    #     for c in changes:
    #         #print (c.oldLineNum, c.newLineNum, c.significantChangePercentage)
    #         print (f'oldline: {c.oldLineNum}, newline: {c.newLineNum}, change%: {c.significantChangePercentage}')
            
    def __parseGitDiff(self, log):
        class Chunk:
            def __init__(self,oldStart,newStart,lines=None):
                self.oldStart = oldStart
                self.newStart = newStart
                if lines is None:
                    lines = []
                self.lines = lines
                self.linesAdded = 0
                self.linesDeleted = 0
            
            def addLine(self,line):
                self.lines.append(line)

            def getLines(self):
                return self.lines

        lines = log.split("\n")

        chunks = []

        deletedLines = {}

        currHunkIdx = -1

        for line in lines[4:]:
            if(line.startswith("@@")):
                oldStart = re.findall(r'[-]\d+', line)
                oldStart = oldStart[0][1:]
                oldStart = int(oldStart)

                newStart = re.findall(r'[+]\d+', line)
                newStart = newStart[0][1:]
                newStart = int(newStart)
                
                c = Chunk(oldStart,newStart,None)

                chunks.append(c)
                currHunkIdx += 1

            if line.startswith("-"):
                chunks[currHunkIdx].addLine(line)

                #remove + or - before the line
                line = line[1:]

                #remove trailing space before line
                line = line.lstrip()
                
                # add into oldSeen if line is not empty
                # if len(line) > 0:
                #     #deletedLines.add(line)
                #     deletedLines[line] =
                
                chunks[currHunkIdx].linesDeleted += 1
                
            if line.startswith("+"):
                chunks[currHunkIdx].addLine(line)

                chunks[currHunkIdx].linesAdded += 1

            if len(line) == 0:
                continue

        class LineChange:
            def __init__(self,lineNum):
                self.lineNum = lineNum
            def __str__(self): 
                return f"type: {self.lineNum} {self.type}"

        class Added_LineChange(LineChange):
            type = "added"

            def __init__(self,lineNum):
                super().__init__(lineNum)

        class Deleted_LineChange(LineChange):
            type = "deleted"

            def __init__(self,lineNum):
                super().__init__(lineNum)
        
        # class Moved_LineChange(LineChange):
        #     type = "moved"

        #     def __init__(self,lineNum,movedFromLine):
        #         super().__init__(lineNum)
        #         self.significantChangePercent = movedFromLine

        class Edited_LineChange(LineChange):
            type = "edited"

            def __init__(self,lineNum,significantChangePercent):
                super().__init__(lineNum)
                self.significantChangePercent = significantChangePercent
            def __str__(self): 
                return f"type: {self.lineNum} {self.type} change: {self.significantChangePercent}%"

        class Hunk:
            def __init__(self,linesAdded,linesDeleted,listOfLineChanges=None):
                #lines added - lines removed = numOfLinesDifference
                self.linesAdded = linesAdded
                self.linesDeleted = linesDeleted
                if listOfLineChanges is None:
                    listOfLineChanges = []
                self.listOfLineChanges = listOfLineChanges
            def addLineChange(self,line):
                self.listOfLineChanges.append(line)


        hunks = []
        for chunk in chunks:

            oldqueue = []
            newqueue = []

            oldLineNum = chunk.oldStart
            newLineNum = chunk.newStart

            hunk = Hunk(chunk.linesAdded,chunk.linesDeleted)

            for l in chunk.getLines():
                if(l.startswith("-")):
                    l = l[1:]
                    #remove trailing space before line
                    l = l.lstrip()
                    oldqueue.append(l)
                
                if(l.startswith("+")):
                    l = l[1:]
                    #remove trailing space before line
                    l = l.lstrip()
                    newqueue.append(l)
            
            while len(oldqueue) > 0:
                oldLineContent = oldqueue.pop(0)

                #line edited
                if len(newqueue) > 0:
                    newLineContent = newqueue.pop(0)

                    ld = levenshteinDistanceDP(oldLineContent,newLineContent)

                    oldContentLength = len(oldLineContent)

                    if oldContentLength == 0:
                        oldContentLength = 1

                    #significant change percentage
                    sfcp = ld / oldContentLength * 100.0

                    editedLine = Edited_LineChange(newLineNum,sfcp)

                    hunk.addLineChange(editedLine)

                    oldLineNum += 1
                    newLineNum += 1
                    continue

                #line deleted
                # if len(oldqueue) > 0:
                deletedLine = Deleted_LineChange(oldLineNum)
                oldLineNum += 1
                hunk.addLineChange(deletedLine)

            while len(newqueue) > 0:
                newLineContent = newqueue.pop(0)

                addedLine = Added_LineChange(newLineNum)
                hunk.addLineChange(addedLine)

                # #line moved
                # if newLineContent in deletedLines:
                #     movedLine = Moved_LineChange(newLineNum)
                #     hunk.addLineChange(movedLine)

                newLineNum += 1

            hunks.append(hunk)
            
        return hunks
            

    


                    



                






            



        

class DatabaseBuilder:
    def __init__(self, database = Database()):
        if database is None:
            self.database = database

    def setRepoType(self,repotype):
        if repotype == "git":
            self.database= GitDatabase()

    def setFileName(self,filename):
        self.database.filename = filename

    def setSince(self,since):
        self.database.since = since

    def addCommitsMetaData(self,numOfLines=False):
        self.database.addCommitsMetaData(numOfLines)

    def addCommitGraph(self):
        self.database.addCommitGraph()

    def addCommitsDiffs(self):
        self.database.addCommitsDiffs()

    def build(self):
        return self.database

    