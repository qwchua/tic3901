import asyncio
import time
from asyncio.subprocess import Process
from asyncio import Semaphore
import os

class Database():
        self.ref = None
        self.detectRenames = True

        #self.cwd = "repos-for-testing/2048"
    def getCommitsMetaData(self):
        if self.commitsMetadata == None:
            if self.detectRenames == True:
                gitlogcommand = 'git log --name-status --follow --pretty=format:"%H" --  ' + self.filename
                unparsedlog = subprocess.run(
                    gitlogcommand,
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
            # shell=True,
            stdout=subprocess.PIPE,
            # capture_output=True,
        unparsedlog = unparsedlog.stdout.decode(encoding='UTF-8',errors='backslashreplace')
        lines = unparsedlog.split("\n")
                author = collection[2]
                date = datetime.strptime(collection[-1], '%Y-%m-%d %H:%M:%S %z')

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
    
    async def getDiff(self,sem: Semaphore, fromHash: str, toHash: str, oldFilename: str, newFilename: str) -> bytes:
        program = [
            "git",
            "diff",
            "--unified=0",
            "--minimal",
            fromHash,
            toHash,
            "--",
            oldFilename,
            newFilename
        ]
        async with sem:
            process: Process = await asyncio.create_subprocess_exec(
                *program, stdout=asyncio.subprocess.PIPE, stdin=asyncio.subprocess.PIPE
            )
            stdout, stderr = await process.communicate()
            data = stdout.decode(encoding='UTF-8',errors='backslashreplace')
            return (fromHash, toHash, data)
    async def getCommitsDiffs(self):
        if self.commitDiffs == None:
            tasks = []
            diffs = {}
            g = self.commitGraph
            adjList = g.m_adj_list
            semaphore = Semaphore(os.cpu_count())
            
            for fromHash, toHashs in adjList.items():
                for toHash in toHashs:
                    oldFilename = self.commitsMetadata[fromHash]["filename"]
                    newFilename = self.commitsMetadata[toHash]["filename"]
                    tasks.append(asyncio.create_task(self.getDiff(semaphore, fromHash, toHash, oldFilename, newFilename)))
            unparsedResults = await asyncio.gather(*tasks)
            for result in unparsedResults:
                fromHash = result[0]
                toHash = result[1]
                unparsedData = result[2]
                if len(unparsedData) != 0:
                    diff = self.__parseGitDiff(unparsedData)
                    diffs[(fromHash,toHash)] = diff
                else:
                    diffs[(fromHash,toHash)] = {}
            self.commitDiffs = diffs
        return self.commitDiffs
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
                    if len(oldLineContent) > 100 or len(newLineContent) > 100:
                        ld = 50000

                    else:
                        ld = levenshteinDistanceDP(oldLineContent,newLineContent)
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
            
    def setDetectRenames(self, flag):
        self.database.detectRenames = flag
    def setRef(self,ref):
        self.database.ref = ref