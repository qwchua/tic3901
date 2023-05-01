import click
from gitpraise.database import *
from gitpraise.analyzer import *
from gitpraise.datavisualization import *
from gitpraise.scanner import *
from tqdm import tqdm

@click.command()
@click.option("--repotype", type=click.Choice(['git']),default="git", help="The type of repository to analyse")
@click.option("-p", "--path", type=str, default="ALL", help="file or folder to analyse, or 'ALL' for all files tracked by git")
@click.option("-o", "--outputformat", type=click.Choice(['txt','pdf','csv']), default="txt", help="txt / pdf / csv")
@click.option("-c", "--sigchange", type=float, default=50, help="Significant change percentage")
@click.option("-r", "--ref", type=str, required=True,help="branch name or tag to start looking from", prompt="Enter a branch name or tag to start looking from")
@click.option("-d", "--detectrename", type=bool, default=True, help="Continue searching the history of a file beyond renames")

# sample usage in CLI command line "gitpraise"
# sample usage in CLI command line "gitpraise --repotype=git --path=ALL --outputformat==txt"
# sample usage in CLI command line "gitpraise --repotype=git --path=ALL --outputformat=txt --sigchange=50 --ref=master"

def run_command(repotype,path,outputformat,sigchange,ref,detectrename):
    scanner = Scanner(repotype)
    filesToProcess = scanner.findFiles(path)
    results = []

    for file in tqdm(filesToProcess):
    # for file in filesToProcess:
        databaseBuilder = DatabaseBuilder()
        databaseBuilder.setRepoType(repotype)
        databaseBuilder.setFileName(file)
        databaseBuilder.setRef(ref)
        databaseBuilder.setDetectRenames(detectrename)

        db = databaseBuilder.build()

        analyzer = Analyzer(db)
        result = analyzer.getLinesContributions(sigchange)

        results.append(result)

    dv = DataVisualization()
    dv.process(results, outputformat)
