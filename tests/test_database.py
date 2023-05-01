from gitpraise.database import *
import os

# Test database init and getter methods
def test_database_getters():
    database = Database()
    assert database.filename == None
    assert database.since == None
    assert database.commitsMetadata == None
    assert database.commitGraph == None
    assert database.commitDiffs == None
    assert database.ref == None
    assert database.detectRenames == True
    assert database.getCommitsMetaData() == None
    assert database.getCommitGraph() == None
    assert database.getCommitDiffs() == None
    
# Test database builder setRepoType method
def test_DatabaseBuilder_setRepoType():
    databaseBuilder = DatabaseBuilder()
    databaseBuilder.setRepoType("git")
    assert isinstance(databaseBuilder.database, GitDatabase)

# Test database builder setFileName method   
def test_DatabaseBuilder_setFileName():
    databaseBuilder = DatabaseBuilder()
    databaseBuilder.setFileName("file.txt")
    assert databaseBuilder.database.filename == "file.txt"

# Test database builder setDetectRenames method  
def test_DatabaseBuilder_setDetectRenames():
    databaseBuilder = DatabaseBuilder()
    databaseBuilder.setDetectRenames(False)
    assert databaseBuilder.database.detectRenames == False
# Test database builder setRef method
def test_DatabaseBuilder_setRef():
    databaseBuilder = DatabaseBuilder()
    databaseBuilder.setRef("master")
    assert databaseBuilder.database.ref == "master"

# Test database builder build method
def test_DatabaseBuilder_build():
    databaseBuilder = DatabaseBuilder()
    assert isinstance(databaseBuilder.build(), Database)

# Test GitDatabase getNumOfLinesFromCommit method
def test_getNumOfLinesFromCommit():
    # Create a GitDatabase object and set the repository path
    gitDatabase = GitDatabase()

    # Get a commit hash and filename to test with
    commitHash = "33b39a597a3742c0b87effb1055124d2f3be4701"
    os.chdir('repos-for-testing/cli_test_repo')
    filename = " fileoutput.txt"

    # Call the getNumOfLinesFromCommit method
    num_lines = gitDatabase.getNumOfLinesFromCommit(commitHash, filename)

    # Assert that the method returns an integer value equal to 4 for the given file and commit
    assert isinstance(num_lines, int)
    assert num_lines == 4

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

# def test_3():
#     databaseBuilder = DatabaseBuilder()
#     databaseBuilder.setRepoType("git")
#     databaseBuilder.setFileName("index.html")
#     databaseBuilder.addCommitsMetaData(numOfLines=True)
#     databaseBuilder.addCommitGraph()
#     #databaseBuilder.addCommitsDiffs()
#     db = databaseBuilder.build()

#     db.commitGraph.print_parent_list()

#     # diffs = db.getCommitDiffs()

#     # for x, y in diffs.items():
#     #     print(x)
#     #     for d in y:
#     #         for i in d.listOfLineChanges:
#     #             print(i)

#     assert db.filename == "index.html"

# def test_4():
#     databaseBuilder = DatabaseBuilder()
#     databaseBuilder.setRepoType("git")
#     databaseBuilder.setFileName("rename.txt")
#     #databaseBuilder.addCommitsDiffs()
#     db = databaseBuilder.build()

#     db.cwd = "repos-for-testing/testing_scoreboard_analytics"

#     print(db.getCommitsMetaData())

#     db.commitGraph.print_parent_list()

#     assert db.filename == "index.html"

# def test_4():
#     databaseBuilder = DatabaseBuilder()
#     databaseBuilder.setRepoType("git")
#     databaseBuilder.setFileName("rename.txt")
#     databaseBuilder.setDetectRenames()
#     db = databaseBuilder.build()

#     db.cwd = "repos-for-testing/testing_scoreboard_analytics"

#     g = db.getCommitGraph()
#     g.print_adj_list()

#     #print(db.getCommitGraph())

#     #db.commitGraph.print_parent_list()

#     assert db.filename == "rename.txt"

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

#     assert db.filename == "rename.txt"