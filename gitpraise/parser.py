def parseGitLogToNumOfCommits(log):
    # split output by \n and return an array.
    print(log)
    collection = log.split("\n")
    return len(collection)
