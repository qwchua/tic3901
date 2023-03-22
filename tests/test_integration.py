from gitpraise.database import *
from gitpraise.analyzer import *
from gitpraise.datavisualization import *
from gitpraise.scanner import *
from tqdm import tqdm
import os

def test_integration_all_except_cli():
    os.chdir('repos-for-testing/flask/')

    #from CLI retrieve this
    repotype = "git"
    path = "src"
    since = None
    outputformat = "pdf"
    significantchangepercentage = 0
    ref = "main"

    scanner = Scanner(repotype)
    filesToProcess = scanner.findFiles(path)
    
    results = []

    for file in tqdm(filesToProcess):
        databaseBuilder = DatabaseBuilder()
        databaseBuilder.setRepoType(repotype)
        databaseBuilder.setFileName(file)
        databaseBuilder.setSince(since)
        databaseBuilder.setRef(ref)

        db = databaseBuilder.build()

        analyzer = Analyzer(db)
        result = analyzer.getLinesContributions(significantchangepercentage)
        results.append(result)

    print(results)

    dv = DataVisualization()
    dv.process(results, outputformat)

# def test_integration_all_except_cli():
#     os.chdir('repos-for-testing/flask/tests')

#     #from CLI retrieve this
#     repotype = "git"
#     path = "flask/src"
#     since = None
#     outputformat = "pdf"
#     significantchangepercentage = 0
#     ref = "master"

#     scanner = Scanner(repotype)
#     filesToProcess = scanner.findFiles(path)
    
#     results = []

#     for file in tqdm(filesToProcess):
#         databaseBuilder = DatabaseBuilder()
#         databaseBuilder.setRepoType(repotype)
#         databaseBuilder.setFileName(file)
#         databaseBuilder.setSince(since)
#         databaseBuilder.setRef(ref)

#         db = databaseBuilder.build()

#         analyzer = Analyzer(db)
#         result = analyzer.getLinesContributions(significantchangepercentage)
#         results.append(result)

#     dv = DataVisualization()
#     dv.process(results, outputformat)