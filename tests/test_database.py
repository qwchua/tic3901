from gitpraise.database import *
import os
import pytest 
from datetime import datetime, timezone, timedelta

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
 
@pytest.fixture 
def create_database(): 
    database = GitDatabase()
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
    test_dir = os.path.dirname(os.path.abspath(__file__)) 
    repo_dir = os.path.normpath(os.path.join(test_dir, '..', 'repos-for-testing', 'testing_scoreboard_analytics')) 
    os.chdir(repo_dir)

    database = create_database
    actual = database._GitDatabase__getCommits("deleteThenDeleteLines.txt")

    expected =  {'bc5797413e88bdfd09331aeca83e206f4e0e3f46': {'author': 'qwchua', 'parenthashes': ['7fa7f7c5139bf683edc2b6d2901b390fd6c8936b'], 'date': datetime(2023, 3, 18, 14, 35, 43, tzinfo=timezone(timedelta(seconds=28800))), 'filename': 'deleteThenDeleteLines.txt'}, '7fa7f7c5139bf683edc2b6d2901b390fd6c8936b': {'author': 'qwchua', 'parenthashes': ['e66093e953714c28e0db0f4c6aa6ea7ce3bd1034'], 'date': datetime(2023, 3, 18, 14, 32, 56, tzinfo=timezone(timedelta(seconds=28800))), 'filename': 'deleteThenDeleteLines.txt'}, 'e66093e953714c28e0db0f4c6aa6ea7ce3bd1034': {'author': 'qwchua', 'parenthashes': ['9474974e564af0310acf5121e9b7de22fafffe13'], 'date': datetime(2023, 3, 18, 14, 32, 38, tzinfo=timezone(timedelta(seconds=28800))), 'filename': 'deleteThenDeleteLines.txt'}, '9474974e564af0310acf5121e9b7de22fafffe13': {'author': 'qwchua', 'parenthashes': ['6baf0ce6004fe98acf34fd6dbf62c3d2e0de2aeb'], 'date': datetime(2023, 3, 18, 14, 32, 26, tzinfo=timezone(timedelta(seconds=28800))), 'filename': 'deleteThenDeleteLines.txt'}, '6baf0ce6004fe98acf34fd6dbf62c3d2e0de2aeb': {'author': 'qwchua', 'parenthashes': ['c76752166228ac1e7a2329c65ad28b78ca977a70'], 'date': datetime(2023, 3, 18, 14, 32, 14, tzinfo=timezone(timedelta(seconds=28800))), 'filename': 'deleteThenDeleteLines.txt'}, 'c76752166228ac1e7a2329c65ad28b78ca977a70': {'author': 'qwchua', 'parenthashes': ['560eee34b25db34d126b9671cb62ced5f5c0dfbf'], 'date': datetime(2023, 3, 18, 14, 31, 56, tzinfo=timezone(timedelta(seconds=28800))), 'filename': 'deleteThenDeleteLines.txt'}, '560eee34b25db34d126b9671cb62ced5f5c0dfbf': {'author': 'qwchua', 'parenthashes': ['f06aa203421618ca84c2d2478320ac606cc314a5'], 'date': datetime(2023, 3, 18, 14, 31, 35, tzinfo=timezone(timedelta(seconds=28800))), 'filename': 'deleteThenDeleteLines.txt'}, 'f06aa203421618ca84c2d2478320ac606cc314a5': {'author': 'qwchua', 'parenthashes': ['ec70983334f2b847d330e182c4e47e3109ec7aa7'], 'date': datetime(2023, 3, 18, 14, 28, 8, tzinfo=timezone(timedelta(seconds=28800))), 'filename': 'deleteThenDeleteLines.txt'}, 'ec70983334f2b847d330e182c4e47e3109ec7aa7': {'author': 'qwchua', 'parenthashes': [], 'date': datetime(2023, 3, 18, 14, 27, 26, tzinfo=timezone(timedelta(seconds=28800))), 'filename': 'deleteThenDeleteLines.txt'}}
    assert actual == expected

