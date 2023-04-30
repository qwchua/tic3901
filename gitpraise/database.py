#database.py

import subprocess
import re
from datetime import datetime
from gitpraise.graph import Graph
from gitpraise.levenstein import levenshteinDistanceDP

class Database():

    def __init__(self):
        self.filename = None
        self.since = None
        self.commitsMetadata = None
        self.commitGraph = None
        self.commitDiffs = None
        self.ref = None
        self.detectRenames = True

        #self.cwd = "repos-for-testing/testing_scoreboard_analytics"
        #self.cwd = "repos-for-testing/2048"
    
    def getCommitsMetaData(self):
        return self.commitsMetadata
    
    def getCommitGraph(self):
        return self.commitGraph
    
    def getCommitDiffs(self):
        return self.commitDiffs

class GitDatabase(Database):
    def __init__(self):
        super().__init__()

    def getCommitsMetaData(self):

        if self.commitsMetadata == None:
            if self.detectRenames == True:

                gitlogcommand = 'git log --name-status --follow --pretty=format:"%H" --  ' + self.filename

                unparsedlog = subprocess.run(
                    gitlogcommand,
                    shell=True,
                    capture_output=True,
                    text=True,
                    )
                
                unparsedlog = unparsedlog.stdout
                historyqueue = self.__parseGitLogToFileHistoryQueue(unparsedlog)

                allCommits = {}

                for fileRename in historyqueue:
                    currCommits = self.__getCommits(fileRename["oldFileName"],allCommits)

                    #Merge into allCommits
                    allCommits.update(currCommits)
                    
                    if "newFileName" in fileRename:
                        allCommits[fileRename["hash"]]["filename"] = fileRename["newFileName"]

                    #NEW TO HANDLE C100 in git log
                    if "change" in fileRename:
                        allCommits[fileRename["hash"]]["parenthashes"].append(fileRename["oldhash"])

                self.commitsMetadata = allCommits

            if self.detectRenames == False:
                currCommits = self.__getCommits(self.filename)
                self.commitsMetadata = currCommits

        return self.commitsMetadata
                
    def __parseGitLogToFileHistoryQueue(self, log):
        queue = []
        lines = log.split("\n")

        i = 0
        prevFilename = ""
        while i < len(lines):
            if i == 0:
                l = lines[i]
                commithash = l
                i+=1

                l = lines[i]
                if l.startswith("R"):
                    collection = lines[i].split()
                    oldfilename = collection[1]
                    newfilename = collection[2]
                    queue.append({"hash":commithash, "oldFileName":newfilename})
                    queue.append({"hash":commithash, "oldFileName":oldfilename, "newFileName": newfilename})
                
                #NEW TO HANDLE C100 
                elif l.startswith("C"):
                    collection = lines[i].split()
                    oldfilename = collection[1]
                    newfilename = collection[2]
                    queue.append({"hash":commithash, "oldFileName":newfilename})
                    i+=2
                    l = lines[i]
                    queue.append({"hash":commithash, "oldFileName":oldfilename, "newFileName": newfilename, "change": True, "oldhash":l})
                    i-=1

                else:
                    collection = lines[i].split()
                    oldfilename = collection[1]

                    filename = lines[i]

                    queue.append({"hash":commithash, "oldFileName":oldfilename})
                             
            if len(lines[i]) > 1:
                l = lines[i]
                commithash = l
                i+=1
                if lines[i].startswith("R"):
                    collection = lines[i].split()
                    oldfilename = collection[1]
                    newfilename = collection[2]

                    filename = lines[i]
                    if filename != prevFilename:
                        queue.append({"hash":commithash, "oldFileName":oldfilename, "newFileName": newfilename})
                elif l.startswith("C"):
                    collection = lines[i].split()
                    oldfilename = collection[1]
                    newfilename = collection[2]
                    i+=2
                    l = lines[i]
                    queue.append({"hash":commithash, "oldFileName":oldfilename, "newFileName": newfilename, "change": True, "oldhash":l})
                    i-=2
            i+=1

        return queue
    
    def __getCommits(self, filename, allCommits={}):
        commits = {}

        gitlogcommand = "git log --all --format=%H,%P,%an,%ci --simplify-merges -- " + filename

        unparsedlog = subprocess.run(
            gitlogcommand,
            # shell=True,
            stdout=subprocess.PIPE,
            # capture_output=True,
        )
        unparsedlog = unparsedlog.stdout.decode(encoding='UTF-8',errors='backslashreplace')

        lines = unparsedlog.split("\n")
        for l in lines:
            if len(l) > 0: 
                collection = l.split(",")
                commithash = collection[0]
                parenthashes = collection[1]
                author = collection[2]
                date = datetime.strptime(collection[-1], '%Y-%m-%d %H:%M:%S %z')

                if len(parenthashes) > 0:
                    parenthashes = parenthashes.split()
                else:
                    parenthashes = []

                if commithash in allCommits:
                    #check if commit exists in allCommits, need to append to parenthashes instead of creating new key
                    first_list = allCommits[commithash]["parenthashes"]
                    second_list = parenthashes

                    in_first = set(first_list)
                    in_second = set(second_list)

                    in_second_but_not_in_first = in_second - in_first

                    allCommits[commithash]["parenthashes"] = first_list + list(in_second_but_not_in_first)
                
                else:
                    commits[commithash] = {"author": author, "parenthashes": parenthashes, "date": date, "filename": filename}

        return commits

    def getNumOfLinesFromCommit(self, commitHash, filename):
            gitcommand = "git show " + commitHash + ":" + filename
            unparsedlog = subprocess.run(
                        gitcommand,
                        # shell=True,
                        stdout=subprocess.PIPE,
                        # capture_output=True,
                    )
            unparsedlog = unparsedlog.stdout.decode(encoding='UTF-8',errors='backslashreplace')
            #unparsedlog = unparsedlog.stdout.decode

            #print(unparsedlog)
            collection = unparsedlog.split("\n")

            return len(collection)

    def getCommitGraph(self):

        if self.commitGraph == None:

            commits = self.getCommitsMetaData()

            graph = Graph()

            for hash, hashObj in commits.items():
                for parent in hashObj["parenthashes"]:
                    graph.add_edge(parent,hash)

            self.commitGraph = graph
        
        return self.commitGraph

    def getCommitsDiffs(self):

        if self.commitDiffs == None:
            
            diffs = {}

            g = self.commitGraph
            adjList = g.m_adj_list
            
            for fromHash, toHashs in adjList.items():
                for toHash in toHashs:
                    oldFilename = self.commitsMetadata[fromHash]["filename"]
                    newFilename = self.commitsMetadata[toHash]["filename"]
    
                    gitdiffcommand = f"git diff --unified=0 --minimal {fromHash} {toHash} -- {oldFilename} {newFilename}"

                    unparsedlog = subprocess.run(
                        gitdiffcommand,
                        # shell=True,
                        stdout=subprocess.PIPE,
                        # capture_output=True,
                    )
                    unparsedlog = unparsedlog.stdout.decode(encoding='UTF-8',errors='backslashreplace')
                    #unparsedlog = unparsedlog.stdout.decode

                    if len(unparsedlog) != 0:
                        diff = self.__parseGitDiff(unparsedlog)
                        diffs[(fromHash,toHash)] = diff

                    else:
                        diffs[(fromHash,toHash)] = {}

            self.commitDiffs = diffs

        return self.commitDiffs
            
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

        currHunkIdx = -1

        startingLineIndex = 0

        if lines[1].startswith("similarity"):
            startingLineIndex = 7
        elif lines[1].startswith("new file mode") or lines[1].startswith("deleted file mode"):
            startingLineIndex = 5

        elif lines[1].startswith("old mode") and lines[2].startswith("new mode"):
            startingLineIndex = 6
        else:
            startingLineIndex = 4

        for line in lines[startingLineIndex:]:
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
                    #l = l.lstrip()
                    oldqueue.append(l)
                
                if(l.startswith("+")):
                    l = l[1:]
                    #remove trailing space before line
                    #l = l.lstrip()
                    newqueue.append(l)
            
            while len(oldqueue) > 0:
                oldLineContent = oldqueue.pop(0)

                #line edited
                if len(newqueue) > 0:
                    newLineContent = newqueue.pop(0)

                    if len(oldLineContent) > 100 or len(newLineContent) > 100:
                        ld = 50000

                    else:
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
    
    def getCommitContent(self, commitHash, filename):
        output = []

        gitlogcommand = f"git show {commitHash}:{filename}"

        unparsedlog = subprocess.run(
                        gitlogcommand,
                        # shell=True,
                        stdout=subprocess.PIPE,
                        encoding= "utf-8",
                        # capture_output=True,
                        text=True,
                    )
        unparsedlog = unparsedlog.stdout
        lines = unparsedlog.split("\n")
        for l in lines:
            output.append(l)
            
        return output
    
    #not using
    def getHashFromRef(self):
        command = 'git show-ref'

        unparsedlog = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            )

        #SAMPLE OUTPUT
        #347246901eccabe503985a64f16813ca859af25a refs/heads/4.x
        #82f8176b0634c5d744d1a45246244291d895b2d1 refs/remotes/origin/2.4

        unparsedlog = unparsedlog.stdout
        lines = unparsedlog.split("\n")

        for line in lines:
            if len(line) > 0:
                line = line.split()
                hash = line[0]

                refname = ""

                if line[1].startswith("ref/heads/"):
                    refname = line[1][10:]
                
                elif line[1].startswith("refs/remotes/origin/"):
                    refname = line[1][20:]

                elif line[1].startswith("refs/tags/"):
                    refname = line[1][10:]

                if refname == self.ref:
                    return hash
                
    #This is to get the latest commmit hash that modified the file in ref branch
    def getDestinationHash(self):
        command = f'git log --pretty=format:"%H" -1 {self.ref} {self.filename}'

        try:
            unparsedlog = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                )

            unparsedlog = unparsedlog.stdout

            assert len(unparsedlog) > 0

            return unparsedlog
        except:
            raise Exception("Destination Hash not found!")

            

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

    def setDetectRenames(self, flag):
        self.database.detectRenames = flag

    def setRef(self,ref):
        self.database.ref = ref

    def build(self):
        return self.database

    