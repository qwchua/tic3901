# from gitpraise.database import *

# # def test_1():
# #     databaseBuilder = DatabaseBuilder()
# #     databaseBuilder.setRepoType("git")
# #     databaseBuilder.setFileName("index.html")
# #     databaseBuilder.addCommitsMetaData(numOfLines=True)
# #     databaseBuilder.addCommitGraph()
# #     #databaseBuilder.addCommitsDiffs()
# #     #databaseBuilder.setSince("19/1/2020")
# #     db = databaseBuilder.build()
# #     db.commitGraph.print_adj_list()

# #     assert db.filename == "index.html"

# # def test_2():
# #     databaseBuilder = DatabaseBuilder()
# #     databaseBuilder.setRepoType("git")
# #     databaseBuilder.setFileName("index.html")
# #     databaseBuilder.addCommitsMetaData(numOfLines=True)
# #     databaseBuilder.addCommitGraph()
# #     databaseBuilder.addCommitsDiffs()
# #     db = databaseBuilder.build()

# #     assert db.filename == "index.html"

# # def test_3():
# #     databaseBuilder = DatabaseBuilder()
# #     databaseBuilder.setRepoType("git")
# #     databaseBuilder.setFileName("index.html")
# #     databaseBuilder.addCommitsMetaData(numOfLines=True)
# #     databaseBuilder.addCommitGraph()
# #     #databaseBuilder.addCommitsDiffs()
# #     db = databaseBuilder.build()

# #     db.commitGraph.print_parent_list()

# #     # diffs = db.getCommitDiffs()

# #     # for x, y in diffs.items():
# #     #     print(x)
# #     #     for d in y:
# #     #         for i in d.listOfLineChanges:
# #     #             print(i)

# #     assert db.filename == "index.html"

# # def test_4():
# #     databaseBuilder = DatabaseBuilder()
# #     databaseBuilder.setRepoType("git")
# #     databaseBuilder.setFileName("rename.txt")
# #     #databaseBuilder.addCommitsDiffs()
# #     db = databaseBuilder.build()

# #     db.cwd = "repos-for-testing/testing_scoreboard_analytics"

# #     print(db.getCommitsMetaData())

# #     db.commitGraph.print_parent_list()

# #     assert db.filename == "index.html"

# # def test_4():
# #     databaseBuilder = DatabaseBuilder()
# #     databaseBuilder.setRepoType("git")
# #     databaseBuilder.setFileName("rename.txt")
# #     databaseBuilder.setDetectRenames()
# #     db = databaseBuilder.build()

# #     db.cwd = "repos-for-testing/testing_scoreboard_analytics"

# #     g = db.getCommitGraph()
# #     g.print_adj_list()

# #     #print(db.getCommitGraph())

# #     #db.commitGraph.print_parent_list()

# #     assert db.filename == "rename.txt"

# def test_4():
#     gitlogcommand = "git log --all --format=%H,%P,%an,%ci --simplify-merges -- " + "flask/app.py"
#     gitlogcommand2 = r"git log --all --format=%H,%P,%an,%ci --simplify-merges -- flask/app.py"

#     gitlogcommand3 = 'git log --all --format=%H,%P,%an,%ci --simplify-merges -- flask.py'

#     print(gitlogcommand)

#     unparsedlog = subprocess.run(
#             gitlogcommand2,
#             shell=True,
#             cwd= "repos-for-testing/flask",
#             capture_output=True,
#             text=True,
#             check=True
#             )

#     unparsedlog = unparsedlog.stdout
#     print(len(unparsedlog))

#     #assert db.filename == "rename.txt"