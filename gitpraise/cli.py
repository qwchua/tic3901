import click
from gitpraise.database import *
from gitpraise.analyzer import *
from gitpraise.datavisualization import *
from gitpraise.scanner import *
from tqdm import tqdm

@click.command()
@click.option("-r", "--repotype", type=str, default="git", help="The type of repository to analyse")
@click.option("-p", "--path", type=str, default="ALL", help="The file / directory to analyse, or ALL for all files tracked by git")
@click.option("-s", "--since", type=str, default=None)
@click.option("-o", "--outputformat", type=str, default="txt")
@click.option("-c", "--sigchange", type=float, default=50)
@click.option("-r", "--ref", type=str, default="txt", required=True,prompt="Enter a branch name or tag to start looking from")
@click.option("-d", "--detectrename", type=bool, default=True)
# sample usage in CLI "gitpraise -f index.html"
def run_command(repotype,path,since,outputformat,sigchange,ref,detectrename):
    scanner = Scanner(repotype)
    filesToProcess = scanner.findFiles(path)
    results = []

    for file in tqdm(filesToProcess):
        databaseBuilder = DatabaseBuilder()
        databaseBuilder.setRepoType(repotype)
        databaseBuilder.setFileName(file)
        databaseBuilder.setSince(since)
        databaseBuilder.setRef(ref)
        databaseBuilder.setDetectRenames(detectrename)

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