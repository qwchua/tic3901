from gitpraise.parser import parseGitLogToNumOfCommits
import subprocess


def test_parseGitLogToNumOfCommits():
    gitlogcommand = "git log index.html"
    unparsedlog = subprocess.run(
        gitlogcommand, shell=True, cwd="test_repos/2048", capture_output=True, text=True
    )
    unparsedlog = unparsedlog.stdout
    total = parseGitLogToNumOfCommits(unparsedlog)
    assert total == 284
