from gitpraise.database import *
from gitpraise.analyzer import *
from gitpraise.datavisualization import *
from gitpraise.scanner import *
from tqdm import tqdm
import os

def test_integration_all_except_cli():
    os.chdir('repos-for-testing/2048')

    #from CLI retrieve this
    repotype = "git"
    path = "ALL"
    since = None
    outputformat = "txt"
    significantchangepercentage = 0
    ref = "master"

    scanner = Scanner(repotype)
    filesToProcess = scanner.findFiles(path)
    
    results = []
    failed = []

    # for file in tqdm(filesToProcess):
        # databaseBuilder = DatabaseBuilder()
        # databaseBuilder.setRepoType(repotype)
        # databaseBuilder.setFileName(file)
        # databaseBuilder.setSince(since)
        # databaseBuilder.setRef(ref)

        # db = databaseBuilder.build()

        # analyzer = Analyzer(db)
        # result = analyzer.getLinesContributions(significantchangepercentage)
        # results.append(result)


    for file in tqdm(filesToProcess):
        try:
            databaseBuilder = DatabaseBuilder()
            databaseBuilder.setRepoType(repotype)
            databaseBuilder.setFileName(file)
            databaseBuilder.setSince(since)
            databaseBuilder.setRef(ref)

            db = databaseBuilder.build()

            analyzer = Analyzer(db)
            result = analyzer.getLinesContributions(significantchangepercentage)
            results.append(result)

        except:
            failed.append(file)

    for f in failed:
        print("FAILED")
        print(f)


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