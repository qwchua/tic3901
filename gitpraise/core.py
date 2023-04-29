import subprocess
from gitpraise.parser import parseGitLogToNumOfCommits


def showNumberOfCommits(filename):
    gitlogcommand = "git log --all --format=%H,%P,%an,%ci --simplify-merges " + filename
    unparsedlog = subprocess.run(
        gitlogcommand,
        shell=True,
        cwd="repos-for-testing/2048",
        capture_output=True,
        text=True,
    )
    unparsedlog = unparsedlog.stdout
    total = parseGitLogToNumOfCommits(unparsedlog)
    print("File was found in : {} commits".format(total))


# def getScoreboard(filename):
#     gitlogcommand = 'git log'.format(
#         filename)
#     unparsedlog = subprocess.run(
#         gitlogcommand, shell=True, cwd="test_repos/2048", capture_output=True, text=True)
#     unparsedlog = unparsedlog.stdout
#     collection = unparsedlog.split('\n')
#     commitgraph = []
#     print("File was found in : {} commits".format(len(collection)))
