from gitpraise.database import *
from gitpraise.analyzer import *
from gitpraise.datavisualization import *
from gitpraise.scanner import *
from tqdm import tqdm
import os
import cProfile
import pstats
import concurrent.futures


# multithreaded experimental
def processFile(file,repotype,since,ref,detectRename,significantchangepercentage):
        try:
                print(f"Doing: {file}")
                databaseBuilder = DatabaseBuilder()
                databaseBuilder.setRepoType(repotype)
                databaseBuilder.setFileName(file)
                databaseBuilder.setSince(since)
                databaseBuilder.setRef(ref)
                databaseBuilder.setDetectRenames(detectRename)

                db = databaseBuilder.build()

                analyzer = Analyzer(db)
                result = analyzer.getLinesContributions(significantchangepercentage)
                return result

        except MergeError as me: print(me,file)

# multithreaded experimental
def test_integration_all_except_cli_multithreaded():
    with cProfile.Profile() as profile:
          
        os.chdir('repos-for-testing/flask')

        #from CLI retrieve this
        repotype = "git"
        path = "ALL"
        since = None
        outputformat = "txt"
        significantchangepercentage = 0
        detectRename = True
        ref = "main"

        scanner = Scanner(repotype)
        filesToProcess = scanner.findFiles(path)

        results=[]
        
        with concurrent.futures.ProcessPoolExecutor() as executor:
                outputs = [executor.submit(processFile,file,repotype,since,ref,detectRename,significantchangepercentage) for file in filesToProcess]

                for f in concurrent.futures.as_completed(outputs):
                        results.append(f.result())

        dv = DataVisualization()
        dv.process(results, outputformat)

    results = pstats.Stats(profile)
    results.sort_stats(pstats.SortKey.TIME)
    results.print_stats(15)
    

# def test_integration_all_except_cli_singlethreaded():
#     os.chdir('repos-for-testing/nanoGPT')

#     #from CLI retrieve this
#     repotype = "git"
#     path = "ALL"
#     since = None
#     outputformat = "csv"
#     significantchangepercentage = 0
#     detectRename = True
#     ref = "master"

#     scanner = Scanner(repotype)
#     filesToProcess = scanner.findFiles(path)
    
#     results = []
#     failed = []

#     for file in tqdm(filesToProcess):
#         try:
#             databaseBuilder = DatabaseBuilder()
#             databaseBuilder.setRepoType(repotype)
#             databaseBuilder.setFileName(file)
#             databaseBuilder.setSince(since)
#             databaseBuilder.setRef(ref)
#             databaseBuilder.setDetectRenames(True)

#             db = databaseBuilder.build()

#             analyzer = Analyzer(db)
#             result = analyzer.getLinesContributions(significantchangepercentage)
#             results.append(result)

#         except MergeError as me: print(me,file)

#         except:
#             failed.append(file)

#     for f in failed:
#         print("FAILED")
#         print(f)


#     dv = DataVisualization()
#     dv.process(results, outputformat)


# def test_integration_all_except_cli_single_file():
#     os.chdir('repos-for-testing/flask')

#     #from CLI retrieve this
#     repotype = "git"
#     path = "ALL"
#     since = None
#     outputformat = "csv"
#     significantchangepercentage = 0
#     detectRename = True
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
#         databaseBuilder.setDetectRenames(True)

#         db = databaseBuilder.build()

#         analyzer = Analyzer(db)
#         result = analyzer.getLinesContributions(significantchangepercentage)
#         results.append(result)


#     dv = DataVisualization()
#     dv.process(results, outputformat)