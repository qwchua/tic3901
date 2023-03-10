import click
from gitpraise.core import showNumberOfCommits


# @click.command()
# @click.option('--path', '-p', help="path or file for gitpraise to analyze", required=True)
# def run_command(path):
#     print("processing " + path + "!")


@click.command()
@click.option("-f", "--filename", type=str)
# sample usage in CLI "gitpraise -f index.html"
def run_command(filename):
    click.echo("Hello world")
    showNumberOfCommits(filename)




@click.command()
@click.option("-f", "--filename", type=str)
@click.option("-f", "--repotype", type=str)
@click.option("-f", "--since", type=str)
@click.option("-f", "--outputformat", type=str)
@click.option("-f", "--significantchangepercentage", type=str)
# sample usage in CLI "gitpraise -f index.html"
def run_command(repotype,filename,since,outputformat,significantchangepercentage):
    databaseBuilder = DatabaseBuilder()
    databaseBuilder.setRepoType(repotype)
    databaseBuilder.setFileName(filename)
    databaseBuilder.setSince(since)
    db = databaseBuilder.create()

    analytics = Analytics()
    result = analytics.getFinalContributions(db,significantchangepercentage)

    dv = DataVisualization()
    dv.showContributions(result, outputformat)

class Database:
    x = 5

class DatabaseBuilder:
    x = 5

class Analytics:
    x = 5

class DataVisualization:
    x = 5


# databaseBuilder.addCommitsMetaData()
# databaseBuilder.addCommitGraph()
# databaseBuilder.addCommitsDiffs()