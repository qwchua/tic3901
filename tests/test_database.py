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

import pytest 
from datetime import datetime, timezone, timedelta
from gitpraise.database import GitDatabase 
 
@pytest.fixture 
def create_database(): 
    database = GitDatabase()
    database.commitGraph = {
            '55b2a0fb703a8d19cfa92ccca62e89e54c51e8d1': {
            'author': 'John Doe',
            'parenthashes': ['92b6aa38f6a5fb5a5a6d5f27a391a02b0c0f4d4e'],
            'date': datetime(2022, 4, 1, 11, 31, 25, tzinfo=timezone(timedelta(days=-1, seconds=61200))),
            'filename': 'file6.txt'
            },
            '31bfc7c1226d8a0c5d8829aef7c04b3b3d7d8473': {
            'author': 'Jane Smith',
            'parenthashes': ['6dcf7b59c8c180d77e868f4476e5e6a5a5f5d6db'],
            'date': datetime(2022, 3, 28, 14, 42, 12, tzinfo=timezone(timedelta(days=-1, seconds=61200))),
            'filename': 'file6.txt'
            },
            '72a24b0a0e8c28fa09a6a12f16c08f19d8de26dc': {
            'author': 'Bob Johnson',
            'parenthashes': ['9f9b7c132b82671b8a0d45ddcbf18a06b3a3a8c2'],
            'date': datetime(2022, 3, 25, 9, 17, 49, tzinfo=timezone(timedelta(days=-1, seconds=61200))),
            'filename': 'file6.txt'
            }
        }
    return database 
 
def test_parse_git_log_to_file_history_queue(create_database): 
    database = create_database 
    test_output_log = '''5269327b7ea8bb69ad9c07c7e9e4a533149c81a0
R100 folder2/file5.txt folder2/file6.txt

aec80cb6de715408ea84725e57e55a0a8e60ba0a
C100 file4.txt folder2/file5.txt

dd9224200a9fa18004d04cc2ddc4defd033eac6c 
A file4.txt''' 
    actual = database._GitDatabase__parseGitLogToFileHistoryQueue(test_output_log)
    expected = [
                    {
                        'hash': '5269327b7ea8bb69ad9c07c7e9e4a533149c81a0',
                        'oldFileName': 'folder2/file6.txt'
                    },
                    {
                        'hash': '5269327b7ea8bb69ad9c07c7e9e4a533149c81a0',
                        'oldFileName': 'folder2/file5.txt',
                        'newFileName': 'folder2/file6.txt'
                    },
                    {
                        'hash': 'aec80cb6de715408ea84725e57e55a0a8e60ba0a',
                        'oldFileName': 'file4.txt',
                        'newFileName': 'folder2/file5.txt',
                        'change': True,
                        'oldhash': 'dd9224200a9fa18004d04cc2ddc4defd033eac6c '
                    },
                    {
                        'hash': 'dd9224200a9fa18004d04cc2ddc4defd033eac6c ',
                        'oldFileName': 'file4.txt'
                    }
            ]
    assert actual == expected

def test_get_commits(create_database):
    database = create_database
    fileName = 'file6.txt'
    test_output_log = '''55b2a0fb703a8d19cfa92ccca62e89e54c51e8d1,92b6aa38f6a5fb5a5a6d5f27a391a02b0c0f4d4e,John Doe,2022-04-01 11:31:25 -0700
31bfc7c1226d8a0c5d8829aef7c04b3b3d7d8473,6dcf7b59c8c180d77e868f4476e5e6a5a5f5d6db,Jane Smith,2022-03-28 14:42:12 -0700
72a24b0a0e8c28fa09a6a12f16c08f19d8de26dc,9f9b7c132b82671b8a0d45ddcbf18a06b3a3a8c2,Bob Johnson,2022-03-25 09:17:49 -0700'''
    allCommits = {}
    actual = database._GitDatabase__getCommits(fileName, test_output_log, allCommits)
    expected = {
            '55b2a0fb703a8d19cfa92ccca62e89e54c51e8d1': {
            'author': 'John Doe',
            'parenthashes': ['92b6aa38f6a5fb5a5a6d5f27a391a02b0c0f4d4e'],
            'date': datetime(2022, 4, 1, 11, 31, 25, tzinfo=timezone(timedelta(days=-1, seconds=61200))),
            'filename': 'file6.txt'
            },
            '31bfc7c1226d8a0c5d8829aef7c04b3b3d7d8473': {
            'author': 'Jane Smith',
            'parenthashes': ['6dcf7b59c8c180d77e868f4476e5e6a5a5f5d6db'],
            'date': datetime(2022, 3, 28, 14, 42, 12, tzinfo=timezone(timedelta(days=-1, seconds=61200))),
            'filename': 'file6.txt'
            },
            '72a24b0a0e8c28fa09a6a12f16c08f19d8de26dc': {
            'author': 'Bob Johnson',
            'parenthashes': ['9f9b7c132b82671b8a0d45ddcbf18a06b3a3a8c2'],
            'date': datetime(2022, 3, 25, 9, 17, 49, tzinfo=timezone(timedelta(days=-1, seconds=61200))),
            'filename': 'file6.txt'
            }
        }
    
    assert actual == expected

# def test_parse_git_diff(create_database):
#     database = create_database
#     actual = database.getCommitsDiffs()
#     assert 1 == 2 

