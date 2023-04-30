from click.testing import CliRunner
from gitpraise.cli import run_command
import os

def test_run_command():
    runner = CliRunner()
    os.chdir('repos-for-testing/cli_test_repo')
    result = runner.invoke(run_command, ["--repotype", "git", "--path", "clifile.txt", "--outputformat", "txt", "--sigchange", "50", "--ref", "master"], catch_exceptions=True)
    assert result.exit_code == 0
    expected_output = "clifile.txt\n 33b39a597  drrnsyk 2023-04-30 00:50:31+08:00 1)  Hello, world"
    
    with open('output.txt', 'r') as f:
        output = f.read().strip()
    
    assert expected_output == output
