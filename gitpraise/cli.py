import click
from gitpraise.database import *
from gitpraise.analyzer import *
from gitpraise.datavisualization import *
from gitpraise.scanner import *

@click.command()
@click.option("-r", "--repotype", type=str, default="git")
@click.option("-f", "--filename", type=str, default="ALL")
@click.option("-s", "--since", type=str)
@click.option("-o", "--outputformat", type=str, default="txt")
@click.option("-c", "--sigchange", type=str, default=50)
@click.option("-r", "--ref", type=str, default="txt")
# sample usage in CLI "gitpraise -f index.html"
def run_command(repotype,path,since,outputformat,sigchange,ref):
    scanner = Scanner(repotype)
    filesToProcess = scanner.findFiles(path)
    results = []

    for file in filesToProcess:
        print("Doing: ", file)
        databaseBuilder = DatabaseBuilder()
        databaseBuilder.setRepoType(repotype)
        databaseBuilder.setFileName(file)
        databaseBuilder.setSince(since)
        databaseBuilder.setRef(ref)

        db = databaseBuilder.build()

        analyzer = Analyzer(db)
        result = analyzer.getLinesContributions(sigchange)

        results.append(result)

    dv = DataVisualization()
    dv.process(results, outputformat)


def validate_rolls(ctx, param, value):
    try:
        rolls, dice = map(int, value.split('d', 2))
        return (dice, rolls)
    except ValueError:
        raise click.BadParameter('rolls need to be in format NdM')