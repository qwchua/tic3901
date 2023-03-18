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

def test_adding_lines():
    databaseBuilder = DatabaseBuilder()
    databaseBuilder.setRepoType("git")
    databaseBuilder.setFileName("addlines.txt")
    databaseBuilder.addCommitsMetaData(numOfLines=True)
    databaseBuilder.addCommitGraph()
    databaseBuilder.addCommitsDiffs()
    db = databaseBuilder.build()

    significantchangepercentage = 0.5
    analytics = Analytics(db)

    result = analytics.findLineOwnersHashes(significantchangepercentage,"3f4f3cbe9868bd9d02354aecd9a066476d071efa")

    expected = [
    "6e9beadfb14307fef8f60c37270fd1720752fb69",
    "6e9beadfb14307fef8f60c37270fd1720752fb69",
    "6e9beadfb14307fef8f60c37270fd1720752fb69",
    "6e9beadfb14307fef8f60c37270fd1720752fb69",
    "6e9beadfb14307fef8f60c37270fd1720752fb69",
    "6e9beadfb14307fef8f60c37270fd1720752fb69",
    "6e9beadfb14307fef8f60c37270fd1720752fb69",
    "6e9beadfb14307fef8f60c37270fd1720752fb69",
    "6e9beadfb14307fef8f60c37270fd1720752fb69",
    "6e9beadfb14307fef8f60c37270fd1720752fb69",
    "6e9beadfb14307fef8f60c37270fd1720752fb69",
    "3f4f3cbe9868bd9d02354aecd9a066476d071efa",
    "3f4f3cbe9868bd9d02354aecd9a066476d071efa",
    "3f4f3cbe9868bd9d02354aecd9a066476d071efa",
    "6e9beadfb14307fef8f60c37270fd1720752fb69",
    "6e9beadfb14307fef8f60c37270fd1720752fb69",
    "6e9beadfb14307fef8f60c37270fd1720752fb69",
    "6e9beadfb14307fef8f60c37270fd1720752fb69",
    "6e9beadfb14307fef8f60c37270fd1720752fb69",
    "6e9beadfb14307fef8f60c37270fd1720752fb69",
    "6e9beadfb14307fef8f60c37270fd1720752fb69",
    "6e9beadfb14307fef8f60c37270fd1720752fb69",
    "6e9beadfb14307fef8f60c37270fd1720752fb69",
    "6e9beadfb14307fef8f60c37270fd1720752fb69",
    "6e9beadfb14307fef8f60c37270fd1720752fb69",
    "6e9beadfb14307fef8f60c37270fd1720752fb69",
    "6e9beadfb14307fef8f60c37270fd1720752fb69",
]


    assert result == expected

def test_deleting_lines():
    databaseBuilder = DatabaseBuilder()
    databaseBuilder.setRepoType("git")
    databaseBuilder.setFileName("deletelines.txt")
    databaseBuilder.addCommitsMetaData(numOfLines=True)
    databaseBuilder.addCommitGraph()
    databaseBuilder.addCommitsDiffs()
    db = databaseBuilder.build()

    significantchangepercentage = 0.5
    analytics = Analytics(db)

    result = analytics.findLineOwnersHashes(significantchangepercentage,"94ed2fd828975c89a78215f2e74110b42e0fbf62")

    expected = [
    "df15f3587a965a58fb1f1a92d45eb10d4a46e3ca",
    "df15f3587a965a58fb1f1a92d45eb10d4a46e3ca",
    "df15f3587a965a58fb1f1a92d45eb10d4a46e3ca",
    "df15f3587a965a58fb1f1a92d45eb10d4a46e3ca",
    "df15f3587a965a58fb1f1a92d45eb10d4a46e3ca",
    "df15f3587a965a58fb1f1a92d45eb10d4a46e3ca",
    "2292ccfec14eacdbea2719cd47f118eb5de9796a",
    "2292ccfec14eacdbea2719cd47f118eb5de9796a",
    "df15f3587a965a58fb1f1a92d45eb10d4a46e3ca",
    "df15f3587a965a58fb1f1a92d45eb10d4a46e3ca",
    "df15f3587a965a58fb1f1a92d45eb10d4a46e3ca",
    "df15f3587a965a58fb1f1a92d45eb10d4a46e3ca",
    "df15f3587a965a58fb1f1a92d45eb10d4a46e3ca",
    "df15f3587a965a58fb1f1a92d45eb10d4a46e3ca",
    "df15f3587a965a58fb1f1a92d45eb10d4a46e3ca",
    "df15f3587a965a58fb1f1a92d45eb10d4a46e3ca",
    "df15f3587a965a58fb1f1a92d45eb10d4a46e3ca",
    "df15f3587a965a58fb1f1a92d45eb10d4a46e3ca",
    "df15f3587a965a58fb1f1a92d45eb10d4a46e3ca",
    "df15f3587a965a58fb1f1a92d45eb10d4a46e3ca",
    "df15f3587a965a58fb1f1a92d45eb10d4a46e3ca",
    "df15f3587a965a58fb1f1a92d45eb10d4a46e3ca",
    "df15f3587a965a58fb1f1a92d45eb10d4a46e3ca",
    "df15f3587a965a58fb1f1a92d45eb10d4a46e3ca",
    "df15f3587a965a58fb1f1a92d45eb10d4a46e3ca",
    "df15f3587a965a58fb1f1a92d45eb10d4a46e3ca",
]


    assert result == expected

def test_editing_lines():
    databaseBuilder = DatabaseBuilder()
    databaseBuilder.setRepoType("git")
    databaseBuilder.setFileName("editlines.txt")
    databaseBuilder.addCommitsMetaData(numOfLines=True)
    databaseBuilder.addCommitGraph()
    databaseBuilder.addCommitsDiffs()
    db = databaseBuilder.build()

    significantchangepercentage = 30
    analytics = Analytics(db)

    result = analytics.findLineOwnersHashes(significantchangepercentage,"25412d23b8efddc9d8230b5190fddaa7e9f1dc24")

    diffs = db.getCommitDiffs()

    # for x, y in diffs.items():
    #     print(x)
    #     for d in y:
    #         for i in d.listOfLineChanges:
    #             print(i)

    expected = [
    "cdaaf54c61a3d3fafebf2a159e817f8a27fd1a08",
    "cdaaf54c61a3d3fafebf2a159e817f8a27fd1a08",
    "cdaaf54c61a3d3fafebf2a159e817f8a27fd1a08",
    "cdaaf54c61a3d3fafebf2a159e817f8a27fd1a08",
    "cdaaf54c61a3d3fafebf2a159e817f8a27fd1a08",
    "cdaaf54c61a3d3fafebf2a159e817f8a27fd1a08",
    "cdaaf54c61a3d3fafebf2a159e817f8a27fd1a08",
    "cdaaf54c61a3d3fafebf2a159e817f8a27fd1a08",
    "cdaaf54c61a3d3fafebf2a159e817f8a27fd1a08",
    "cdaaf54c61a3d3fafebf2a159e817f8a27fd1a08",
    "25412d23b8efddc9d8230b5190fddaa7e9f1dc24",
    "cdaaf54c61a3d3fafebf2a159e817f8a27fd1a08",
    "25412d23b8efddc9d8230b5190fddaa7e9f1dc24",
    "cdaaf54c61a3d3fafebf2a159e817f8a27fd1a08",
    "cdaaf54c61a3d3fafebf2a159e817f8a27fd1a08",
    "cdaaf54c61a3d3fafebf2a159e817f8a27fd1a08",
    "cdaaf54c61a3d3fafebf2a159e817f8a27fd1a08",
    "cdaaf54c61a3d3fafebf2a159e817f8a27fd1a08",
    "cdaaf54c61a3d3fafebf2a159e817f8a27fd1a08",
    "cdaaf54c61a3d3fafebf2a159e817f8a27fd1a08",
    "cdaaf54c61a3d3fafebf2a159e817f8a27fd1a08",
    "cdaaf54c61a3d3fafebf2a159e817f8a27fd1a08",
    "cdaaf54c61a3d3fafebf2a159e817f8a27fd1a08",
    "cdaaf54c61a3d3fafebf2a159e817f8a27fd1a08",
]
    
    assert result == expected

def test_adding_lines_then_edit_lines():
    databaseBuilder = DatabaseBuilder()
    databaseBuilder.setRepoType("git")
    databaseBuilder.setFileName("addThenEditLines.txt")
    databaseBuilder.addCommitsMetaData(numOfLines=True)
    databaseBuilder.addCommitGraph()
    databaseBuilder.addCommitsDiffs()
    db = databaseBuilder.build()

    significantchangepercentage = 30
    analytics = Analytics(db)

    result = analytics.findLineOwnersHashes(significantchangepercentage,"2f972d5e16e9297e41f41bd73f06ce8e88727fbe")
    #print(result)

    diffs = db.getCommitDiffs()

    # for x, y in diffs.items():
    #     print(x)
    #     for d in y:
    #         for i in d.listOfLineChanges:
    #             print(i)

    expected = [
    "00df1638d6b1598c65dcf87617b03e6c6897f60e",
    "00df1638d6b1598c65dcf87617b03e6c6897f60e",
    "00df1638d6b1598c65dcf87617b03e6c6897f60e",
    "00df1638d6b1598c65dcf87617b03e6c6897f60e",
    "00df1638d6b1598c65dcf87617b03e6c6897f60e",
    "00df1638d6b1598c65dcf87617b03e6c6897f60e",
    "2f972d5e16e9297e41f41bd73f06ce8e88727fbe",
    "2f972d5e16e9297e41f41bd73f06ce8e88727fbe",
    "00df1638d6b1598c65dcf87617b03e6c6897f60e",
    "00df1638d6b1598c65dcf87617b03e6c6897f60e",
    "00df1638d6b1598c65dcf87617b03e6c6897f60e",
    "00df1638d6b1598c65dcf87617b03e6c6897f60e",
    "00df1638d6b1598c65dcf87617b03e6c6897f60e",
    "00df1638d6b1598c65dcf87617b03e6c6897f60e",
    "00df1638d6b1598c65dcf87617b03e6c6897f60e",
    "00df1638d6b1598c65dcf87617b03e6c6897f60e",
    "00df1638d6b1598c65dcf87617b03e6c6897f60e",
    "00df1638d6b1598c65dcf87617b03e6c6897f60e",
    "00df1638d6b1598c65dcf87617b03e6c6897f60e",
    "00df1638d6b1598c65dcf87617b03e6c6897f60e",
    "00df1638d6b1598c65dcf87617b03e6c6897f60e",
    "2f972d5e16e9297e41f41bd73f06ce8e88727fbe",
    "00df1638d6b1598c65dcf87617b03e6c6897f60e",
    "00df1638d6b1598c65dcf87617b03e6c6897f60e",
    "00df1638d6b1598c65dcf87617b03e6c6897f60e",
    "00df1638d6b1598c65dcf87617b03e6c6897f60e",
    ]
    
    assert result == expected

def test_deleting_lines_then_edit_lines():
    databaseBuilder = DatabaseBuilder()
    databaseBuilder.setRepoType("git")
    databaseBuilder.setFileName("deleteThenEditLines.txt")
    databaseBuilder.addCommitsMetaData(numOfLines=True)
    databaseBuilder.addCommitGraph()
    databaseBuilder.addCommitsDiffs()
    db = databaseBuilder.build()

    significantchangepercentage = 30
    analytics = Analytics(db)

    result = analytics.findLineOwnersHashes(significantchangepercentage,"46428b56ec4b830b9248010d6b103402f1b3c630")
    #print(result)

    diffs = db.getCommitDiffs()

    # for x, y in diffs.items():
    #     print(x)
    #     for d in y:
    #         for i in d.listOfLineChanges:
    #             print(i)

    expected = [
    "8979a0bd66d39ea7d48729330278566a0d31decf",
    "8979a0bd66d39ea7d48729330278566a0d31decf",
    "8979a0bd66d39ea7d48729330278566a0d31decf",
    "8979a0bd66d39ea7d48729330278566a0d31decf",
    "8979a0bd66d39ea7d48729330278566a0d31decf",
    "8979a0bd66d39ea7d48729330278566a0d31decf",
    "8979a0bd66d39ea7d48729330278566a0d31decf",
    "8979a0bd66d39ea7d48729330278566a0d31decf",
    "8979a0bd66d39ea7d48729330278566a0d31decf",
    "8979a0bd66d39ea7d48729330278566a0d31decf",
    "8979a0bd66d39ea7d48729330278566a0d31decf",
    "8979a0bd66d39ea7d48729330278566a0d31decf",
    "8979a0bd66d39ea7d48729330278566a0d31decf",
    "8979a0bd66d39ea7d48729330278566a0d31decf",
    "8979a0bd66d39ea7d48729330278566a0d31decf",
    "8979a0bd66d39ea7d48729330278566a0d31decf",
    "46428b56ec4b830b9248010d6b103402f1b3c630",
    "8979a0bd66d39ea7d48729330278566a0d31decf",
    "8979a0bd66d39ea7d48729330278566a0d31decf",
    "8979a0bd66d39ea7d48729330278566a0d31decf",
    "8979a0bd66d39ea7d48729330278566a0d31decf",
    ]
    
    assert result == expected

def test_adding_lines_then_adding_lines():
    databaseBuilder = DatabaseBuilder()
    databaseBuilder.setRepoType("git")
    databaseBuilder.setFileName("addThenAddLines.txt")
    databaseBuilder.addCommitsMetaData(numOfLines=True)
    databaseBuilder.addCommitGraph()
    databaseBuilder.addCommitsDiffs()
    db = databaseBuilder.build()

    significantchangepercentage = 30
    analytics = Analytics(db)

    result = analytics.findLineOwnersHashes(significantchangepercentage,"afb7340cc3d9c1dae4d15e315872c822188d497c")
    #print(result)

    diffs = db.getCommitDiffs()

    # for x, y in diffs.items():
    #     print(x)
    #     for d in y:
    #         for i in d.listOfLineChanges:
    #             print(i)

    expected = [
    "fa6f29996943d70a042e61fca77f46f709fd5f13",
    "fa6f29996943d70a042e61fca77f46f709fd5f13",
    "fa6f29996943d70a042e61fca77f46f709fd5f13",
    "fa6f29996943d70a042e61fca77f46f709fd5f13",
    "fa6f29996943d70a042e61fca77f46f709fd5f13",
    "fa6f29996943d70a042e61fca77f46f709fd5f13",
    "afb7340cc3d9c1dae4d15e315872c822188d497c",
    "afb7340cc3d9c1dae4d15e315872c822188d497c",
    "fa6f29996943d70a042e61fca77f46f709fd5f13",
    "fa6f29996943d70a042e61fca77f46f709fd5f13",
    "fa6f29996943d70a042e61fca77f46f709fd5f13",
    "fa6f29996943d70a042e61fca77f46f709fd5f13",
    "fa6f29996943d70a042e61fca77f46f709fd5f13",
    "fa6f29996943d70a042e61fca77f46f709fd5f13",
    "fa6f29996943d70a042e61fca77f46f709fd5f13",
    "fa6f29996943d70a042e61fca77f46f709fd5f13",
    "fa6f29996943d70a042e61fca77f46f709fd5f13",
    "fa6f29996943d70a042e61fca77f46f709fd5f13",
    "fa6f29996943d70a042e61fca77f46f709fd5f13",
    "fa6f29996943d70a042e61fca77f46f709fd5f13",
    "fa6f29996943d70a042e61fca77f46f709fd5f13",
    "fa6f29996943d70a042e61fca77f46f709fd5f13",
    "fa6f29996943d70a042e61fca77f46f709fd5f13",
    "afb7340cc3d9c1dae4d15e315872c822188d497c",
    "afb7340cc3d9c1dae4d15e315872c822188d497c",
    "fa6f29996943d70a042e61fca77f46f709fd5f13",
    "fa6f29996943d70a042e61fca77f46f709fd5f13",
    "fa6f29996943d70a042e61fca77f46f709fd5f13",
    ]
    
    assert result == expected

def test_delete_lines_then_delete_lines():
    databaseBuilder = DatabaseBuilder()
    databaseBuilder.setRepoType("git")
    databaseBuilder.setFileName("deleteThenDeleteLines.txt")
    databaseBuilder.addCommitsMetaData(numOfLines=True)
    databaseBuilder.addCommitGraph()
    databaseBuilder.addCommitsDiffs()
    db = databaseBuilder.build()

    significantchangepercentage = 30
    analytics = Analytics(db)

    result = analytics.findLineOwnersHashes(significantchangepercentage,"bc5797413e88bdfd09331aeca83e206f4e0e3f46")
    #print(result)

    diffs = db.getCommitDiffs()

    # for x, y in diffs.items():
    #     print(x)
    #     for d in y:
    #         for i in d.listOfLineChanges:
    #             print(i)

    expected = [
    "c76752166228ac1e7a2329c65ad28b78ca977a70",
    "c76752166228ac1e7a2329c65ad28b78ca977a70",
    "c76752166228ac1e7a2329c65ad28b78ca977a70",
    "c76752166228ac1e7a2329c65ad28b78ca977a70",
    "6baf0ce6004fe98acf34fd6dbf62c3d2e0de2aeb",
    "6baf0ce6004fe98acf34fd6dbf62c3d2e0de2aeb",
    "6baf0ce6004fe98acf34fd6dbf62c3d2e0de2aeb",
    "9474974e564af0310acf5121e9b7de22fafffe13",
    "9474974e564af0310acf5121e9b7de22fafffe13",
    "e66093e953714c28e0db0f4c6aa6ea7ce3bd1034",
    "e66093e953714c28e0db0f4c6aa6ea7ce3bd1034",
    "e66093e953714c28e0db0f4c6aa6ea7ce3bd1034",
    "e66093e953714c28e0db0f4c6aa6ea7ce3bd1034",
    "7fa7f7c5139bf683edc2b6d2901b390fd6c8936b",
    "7fa7f7c5139bf683edc2b6d2901b390fd6c8936b",
    "7fa7f7c5139bf683edc2b6d2901b390fd6c8936b",
    "7fa7f7c5139bf683edc2b6d2901b390fd6c8936b",
    "bc5797413e88bdfd09331aeca83e206f4e0e3f46",
    "7fa7f7c5139bf683edc2b6d2901b390fd6c8936b",
    "7fa7f7c5139bf683edc2b6d2901b390fd6c8936b",
    ]
   
    assert result == expected

def test_add_lines_then_delete_lines():
    databaseBuilder = DatabaseBuilder()
    databaseBuilder.setRepoType("git")
    databaseBuilder.setFileName("addThenDeleteLines.txt")
    databaseBuilder.addCommitsMetaData(numOfLines=True)
    databaseBuilder.addCommitGraph()
    databaseBuilder.addCommitsDiffs()
    db = databaseBuilder.build()

    significantchangepercentage = 30
    analytics = Analytics(db)

    result = analytics.findLineOwnersHashes(significantchangepercentage,"64bf2744b748c151985aad11d5b37105c4340c27")
    #print(result)

    diffs = db.getCommitDiffs()

    # for x, y in diffs.items():
    #     print(x)
    #     for d in y:
    #         for i in d.listOfLineChanges:
    #             print(i)

    expected = [
    "05a8d7acf560fe2f972246e2df79430aa6848fbd",
    "05a8d7acf560fe2f972246e2df79430aa6848fbd",
    "05a8d7acf560fe2f972246e2df79430aa6848fbd",
    "05a8d7acf560fe2f972246e2df79430aa6848fbd",
    "b6d21a352328bd5171f86a8f1211011f6f39372d",
    "b6d21a352328bd5171f86a8f1211011f6f39372d",
    "b6d21a352328bd5171f86a8f1211011f6f39372d",
    "b6d21a352328bd5171f86a8f1211011f6f39372d",
    "e9a300f093aff9e01daf474a76fca15819530f88",
    "64bf2744b748c151985aad11d5b37105c4340c27",
    "64bf2744b748c151985aad11d5b37105c4340c27",
    "64bf2744b748c151985aad11d5b37105c4340c27",
    "64bf2744b748c151985aad11d5b37105c4340c27",
    "e9a300f093aff9e01daf474a76fca15819530f88",
    "e9a300f093aff9e01daf474a76fca15819530f88",
    "e9a300f093aff9e01daf474a76fca15819530f88",
    "55c95b9ca585a988ffc6a4e4e56f9f5eba760187",
    "55c95b9ca585a988ffc6a4e4e56f9f5eba760187",
    "55c95b9ca585a988ffc6a4e4e56f9f5eba760187",
    "1c7534401f26265f68f62b20ca4f27d5be0254c7",
    "1c7534401f26265f68f62b20ca4f27d5be0254c7",
    "1c7534401f26265f68f62b20ca4f27d5be0254c7",
    "31951af22ae3db3257d93dab0c2b32d6b2f5edf6",
    "31951af22ae3db3257d93dab0c2b32d6b2f5edf6",
    "31951af22ae3db3257d93dab0c2b32d6b2f5edf6",
    "31951af22ae3db3257d93dab0c2b32d6b2f5edf6",
    ]   
    
    assert result == expected

def test_delete_lines_then_add_lines():
    databaseBuilder = DatabaseBuilder()
    databaseBuilder.setRepoType("git")
    databaseBuilder.setFileName("deleteThenAddLines.txt")
    databaseBuilder.addCommitsMetaData(numOfLines=True)
    databaseBuilder.addCommitGraph()
    databaseBuilder.addCommitsDiffs()
    db = databaseBuilder.build()

    significantchangepercentage = 30
    analytics = Analytics(db)

    result = analytics.findLineOwnersHashes(significantchangepercentage,"039d698982ac01c7c5970b169a0665e6364c7828")

    diffs = db.getCommitDiffs()

    # for x, y in diffs.items():
    #     print(x)
    #     for d in y:
    #         for i in d.listOfLineChanges:
    #             print(i)

    expected = [
    "91759820b5fbb4bbd17a1f46887ccd848dba8192",
    "91759820b5fbb4bbd17a1f46887ccd848dba8192",
    "91759820b5fbb4bbd17a1f46887ccd848dba8192",
    "91759820b5fbb4bbd17a1f46887ccd848dba8192",
    "b8e52d2945427bd7dfa28a0fd1464edc4fbc881b",
    "b8e52d2945427bd7dfa28a0fd1464edc4fbc881b",
    "b8e52d2945427bd7dfa28a0fd1464edc4fbc881b",
    "b8e52d2945427bd7dfa28a0fd1464edc4fbc881b",
    "dbaa24724c32be69ed71fd2e3c399a4bd70569a0",
    "dbaa24724c32be69ed71fd2e3c399a4bd70569a0",
    "dbaa24724c32be69ed71fd2e3c399a4bd70569a0",
    "dbaa24724c32be69ed71fd2e3c399a4bd70569a0",
    "502521076ce1b42468d4a9890b5cdc03a0af0a7a",
    "502521076ce1b42468d4a9890b5cdc03a0af0a7a",
    "502521076ce1b42468d4a9890b5cdc03a0af0a7a",
    "570989077ad57de086bf28e1874ae123cc5c2cea",
    "570989077ad57de086bf28e1874ae123cc5c2cea",
    "570989077ad57de086bf28e1874ae123cc5c2cea",
    "fd6747b67f3f42a9ed64587b349761e4055ba6c9",
    "fd6747b67f3f42a9ed64587b349761e4055ba6c9",
    "fd6747b67f3f42a9ed64587b349761e4055ba6c9",
    "039d698982ac01c7c5970b169a0665e6364c7828",
    "039d698982ac01c7c5970b169a0665e6364c7828",
    "039d698982ac01c7c5970b169a0665e6364c7828",
    "039d698982ac01c7c5970b169a0665e6364c7828",
    "039d698982ac01c7c5970b169a0665e6364c7828",
    "fd6747b67f3f42a9ed64587b349761e4055ba6c9",
    ]
    
    assert result == expected

def test_bigone():
    databaseBuilder = DatabaseBuilder()
    databaseBuilder.setRepoType("git")
    databaseBuilder.setFileName("js/game_manager.js")
    databaseBuilder.addCommitsMetaData(numOfLines=True)
    databaseBuilder.addCommitGraph()
    databaseBuilder.addCommitsDiffs()
    db = databaseBuilder.build()

    significantchangepercentage = 0.1
    analytics = Analytics(db)

    #result = analytics.findLineOwnersHashes(significantchangepercentage,"fc1ef4fe5a5fcccea7590f3e4c187c75980b353f")
    result = analytics.findLineOwnersHashes(significantchangepercentage,"3b86903e65383e30ffc836b733dcaf094c33ff10")

    diffs = db.getCommitDiffs()

    # for x, y in diffs.items():
    #     print(x)
    #     for d in y:
    #         for i in d.listOfLineChanges:
    #             print(i)

    expected = [
    "91759820b5fbb4bbd17a1f46887ccd848dba8192",
    "91759820b5fbb4bbd17a1f46887ccd848dba8192",
    "91759820b5fbb4bbd17a1f46887ccd848dba8192",
    "91759820b5fbb4bbd17a1f46887ccd848dba8192",
    "b8e52d2945427bd7dfa28a0fd1464edc4fbc881b",
    "b8e52d2945427bd7dfa28a0fd1464edc4fbc881b",
    "b8e52d2945427bd7dfa28a0fd1464edc4fbc881b",
    "b8e52d2945427bd7dfa28a0fd1464edc4fbc881b",
    "dbaa24724c32be69ed71fd2e3c399a4bd70569a0",
    "dbaa24724c32be69ed71fd2e3c399a4bd70569a0",
    "dbaa24724c32be69ed71fd2e3c399a4bd70569a0",
    "dbaa24724c32be69ed71fd2e3c399a4bd70569a0",
    "502521076ce1b42468d4a9890b5cdc03a0af0a7a",
    "502521076ce1b42468d4a9890b5cdc03a0af0a7a",
    "502521076ce1b42468d4a9890b5cdc03a0af0a7a",
    "570989077ad57de086bf28e1874ae123cc5c2cea",
    "570989077ad57de086bf28e1874ae123cc5c2cea",
    "570989077ad57de086bf28e1874ae123cc5c2cea",
    "fd6747b67f3f42a9ed64587b349761e4055ba6c9",
    "fd6747b67f3f42a9ed64587b349761e4055ba6c9",
    "fd6747b67f3f42a9ed64587b349761e4055ba6c9",
    "039d698982ac01c7c5970b169a0665e6364c7828",
    "039d698982ac01c7c5970b169a0665e6364c7828",
    "039d698982ac01c7c5970b169a0665e6364c7828",
    "039d698982ac01c7c5970b169a0665e6364c7828",
    "039d698982ac01c7c5970b169a0665e6364c7828",
    "fd6747b67f3f42a9ed64587b349761e4055ba6c9",
    ]
    
    #assert result == expected