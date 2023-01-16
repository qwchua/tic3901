def parseGitLogToNumOfCommits(log):
    # split output by \n and return an array.
    collection = log.split("\n")
    return len(collection)
