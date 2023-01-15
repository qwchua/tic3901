import click
from gitpraise.core import showNumberOfCommits


# @click.command()
# @click.option('--path', '-p', help="path or file for gitpraise to analyze", required=True)
# def run_command(path):
#     print("processing " + path + "!")


@click.command()
@click.option("-f", "--filename", type=str)
def run_command(filename):
    click.echo("Hello world")
    showNumberOfCommits(filename)
