from gitpraise.parser import parseGitLogToNumOfCommits
import subprocess


def test_parseGitLogToNumOfCommits():
    gitlogcommand = "git log index.html"
    unparsedlog = subprocess.run(
        gitlogcommand,
        shell=True,
        cwd="repos-for-testing/2048",
        capture_output=True,
        text=True,
    )
    unparsedlog = unparsedlog.stdout
    total = parseGitLogToNumOfCommits(unparsedlog)
    assert total == 284


def test_parseGitLogToNumOfCommits():
    gitlogcommand = "git log tox.ini"
    unparsedlog = subprocess.run(
        gitlogcommand,
        shell=True,
        cwd="repos-for-testing/flask",
        capture_output=True,
        text=True,
    )
    unparsedlog = unparsedlog.stdout
    total = parseGitLogToNumOfCommits(unparsedlog)
    assert total == 595
