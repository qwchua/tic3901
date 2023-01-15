def parseGitLogToNumOfCommits(log):
    collection = log.split("\n")
    return len(collection)
