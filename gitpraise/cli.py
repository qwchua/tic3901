import click
from gitpraise.database import *
from gitpraise.analyzer import *
from gitpraise.datavisualization import *
from gitpraise.scanner import *

@click.command()
@click.option("-f", "--filename", type=str)
@click.option("-f", "--repotype", type=str)
@click.option("-f", "--since", type=str)
@click.option("-f", "--outputformat", type=str)
@click.option("-f", "--significantchangepercentage", type=str)
# sample usage in CLI "gitpraise -f index.html"
def run_command(repotype,path,since,outputformat,significantchangepercentage,ref):
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
        result = analyzer.getLinesContributions(significantchangepercentage)

        results.append(result)

    dv = DataVisualization()
    dv.process(results, outputformat)
