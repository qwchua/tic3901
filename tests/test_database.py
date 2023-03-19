from gitpraise.database import *

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

# def test_2():
#     databaseBuilder = DatabaseBuilder()
#     databaseBuilder.setRepoType("git")
#     databaseBuilder.setFileName("index.html")
#     databaseBuilder.addCommitsMetaData(numOfLines=True)
#     databaseBuilder.addCommitGraph()
#     databaseBuilder.addCommitsDiffs()
#     db = databaseBuilder.build()

#     assert db.filename == "index.html"

def test_3():
    databaseBuilder = DatabaseBuilder()
    databaseBuilder.setRepoType("git")
    databaseBuilder.setFileName("index.html")
    databaseBuilder.addCommitsMetaData(numOfLines=True)
    databaseBuilder.addCommitGraph()
    #databaseBuilder.addCommitsDiffs()
    db = databaseBuilder.build()

    db.commitGraph.print_parent_list()

    # diffs = db.getCommitDiffs()

    # for x, y in diffs.items():
    #     print(x)
    #     for d in y:
    #         for i in d.listOfLineChanges:
    #             print(i)

    assert db.filename == "index.html"

def test_3():
    databaseBuilder = DatabaseBuilder()
    databaseBuilder.setRepoType("git")
    databaseBuilder.setFileName("index.html")
    databaseBuilder.addCommitsMetaData(numOfLines=True)
    databaseBuilder.addCommitGraph()
    #databaseBuilder.addCommitsDiffs()
    db = databaseBuilder.build()

    db.commitGraph.print_parent_list()

    # diffs = db.getCommitDiffs()

    # for x, y in diffs.items():
    #     print(x)
    #     for d in y:
    #         for i in d.listOfLineChanges:
    #             print(i)

    assert db.filename == "index.html"