from gitpraise.database import *
from gitpraise.analytics import *

# def test_1():
#     databaseBuilder = DatabaseBuilder()
#     databaseBuilder.setRepoType("git")
#     databaseBuilder.setFileName("index.html")
#     databaseBuilder.addCommitsMetaData(numOfLines=True)
#     databaseBuilder.addCommitGraph()
#     #databaseBuilder.addCommitsDiffs()
#     #databaseBuilder.setSince("19/1/2020")
#     db = databaseBuilder.build()
#     db.commitGraph.print_adj_list()

#     assert db.filename == "index.html"

def test_2():
    databaseBuilder = DatabaseBuilder()
    databaseBuilder.setRepoType("git")
    databaseBuilder.setFileName("index.html")
    databaseBuilder.addCommitsMetaData(numOfLines=True)
    databaseBuilder.addCommitGraph()
    databaseBuilder.addCommitsDiffs()
    db = databaseBuilder.build()

    significantchangepercentage = 0.5
    analytics = Analytics(db)
    result = analytics.getFinalContributions(significantchangepercentage)

    assert db.filename == "index.html"