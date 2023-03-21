from gitpraise.database import *
from gitpraise.analyzer import *
from gitpraise.datavisualization import *
from gitpraise.scanner import *
import os

def test_integration_all_except_cli():
    os.chdir('repos-for-testing/2048')

    #from CLI retrieve this
    repotype = "git"
    path = "index.html"
    since = None
    outputformat = "pdf"
    significantchangepercentage = 0
    ref = "master"

    scanner = Scanner(repotype)
    filesToProcess = scanner.findFiles(path)
    results = []

    for file in filesToProcess:
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