# from gitpraise.database import *
# from gitpraise.analyzer import *
# from gitpraise.datavisualization import *

# def test_1():
#     databaseBuilder = DatabaseBuilder()
#     databaseBuilder.setRepoType("git")
#     databaseBuilder.setFileName("js/game_manager.js")
#     databaseBuilder.setDetectRenames()
#     db = databaseBuilder.build()

#     db.cwd = "repos-for-testing/2048"

#     significantchangepercentage = 0
#     analytics = Analyzer(db)

#     results = []

#     result = analytics.getLinesContributions(significantchangepercentage,"3b86903e65383e30ffc836b733dcaf094c33ff10")

#     results.append(result)

#     outputformat = "pdf"

#     dv = DataVisualization()
#     dv.process(results, outputformat)