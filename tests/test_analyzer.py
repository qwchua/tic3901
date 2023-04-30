from gitpraise.database import *
from gitpraise.analyzer import *
import os

def test_adding_lines():
    os.chdir('repos-for-testing/testing_scoreboard_analytics')

    databaseBuilder = DatabaseBuilder()
    databaseBuilder.setRepoType("git")
    databaseBuilder.setFileName("addlines.txt")
    databaseBuilder.setDetectRenames(False)

    db = databaseBuilder.build()

    significantchangepercentage = 0.5
    analyzer = Analyzer(db)

    result = analyzer.findLineOwnersHashes(significantchangepercentage,"3f4f3cbe9868bd9d02354aecd9a066476d071efa")

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
    db = databaseBuilder.build()
    databaseBuilder.setDetectRenames(False)

    significantchangepercentage = 0.5
    analyzer = Analyzer(db)

    result = analyzer.findLineOwnersHashes(significantchangepercentage,"94ed2fd828975c89a78215f2e74110b42e0fbf62")

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
    databaseBuilder.setDetectRenames(False)
    db = databaseBuilder.build()
    db.cwd = "repos-for-testing/testing_scoreboard_analytics"

    significantchangepercentage = 30
    analyzer = Analyzer(db)

    result = analyzer.findLineOwnersHashes(significantchangepercentage,"25412d23b8efddc9d8230b5190fddaa7e9f1dc24")

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
    "cdaaf54c61a3d3fafebf2a159e817f8a27fd1a08",
    ]
    assert result == expected

def test_adding_lines_then_edit_lines():
    databaseBuilder = DatabaseBuilder()
    databaseBuilder.setRepoType("git")
    databaseBuilder.setFileName("addThenEditLines.txt")
    db = databaseBuilder.build()
    db.cwd = "repos-for-testing/testing_scoreboard_analytics"

    significantchangepercentage = 30
    analyzer = Analyzer(db)

    result = analyzer.findLineOwnersHashes(significantchangepercentage,"2f972d5e16e9297e41f41bd73f06ce8e88727fbe")
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
    db = databaseBuilder.build()
    db.cwd = "repos-for-testing/testing_scoreboard_analytics"

    significantchangepercentage = 30
    analyzer = Analyzer(db)

    result = analyzer.findLineOwnersHashes(significantchangepercentage,"46428b56ec4b830b9248010d6b103402f1b3c630")
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
    db = databaseBuilder.build()
    db.cwd = "repos-for-testing/testing_scoreboard_analytics"

    significantchangepercentage = 30
    analyzer = Analyzer(db)

    result = analyzer.findLineOwnersHashes(significantchangepercentage,"afb7340cc3d9c1dae4d15e315872c822188d497c")
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
    db = databaseBuilder.build()
    db.cwd = "repos-for-testing/testing_scoreboard_analytics"

    significantchangepercentage = 30
    analyzer = Analyzer(db)

    result = analyzer.findLineOwnersHashes(significantchangepercentage,"bc5797413e88bdfd09331aeca83e206f4e0e3f46")
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
    db = databaseBuilder.build()
    db.cwd = "repos-for-testing/testing_scoreboard_analytics"

    significantchangepercentage = 30
    analyzer = Analyzer(db)

    result = analyzer.findLineOwnersHashes(significantchangepercentage,"64bf2744b748c151985aad11d5b37105c4340c27")
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
    db = databaseBuilder.build()
    db.cwd = "repos-for-testing/testing_scoreboard_analytics"

    significantchangepercentage = 30
    analyzer = Analyzer(db)

    result = analyzer.findLineOwnersHashes(significantchangepercentage,"039d698982ac01c7c5970b169a0665e6364c7828")

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

def test_2048_indexhtml():
    os.chdir('../2048')

    databaseBuilder = DatabaseBuilder()
    databaseBuilder.setRepoType("git")
    databaseBuilder.setFileName("index.html")
    db = databaseBuilder.build()

    db.cwd = "repos-for-testing/2048"

    significantchangepercentage = 0
    analyzer = Analyzer(db)

    result = analyzer.findLineOwnersHashes(significantchangepercentage,"fc1ef4fe5a5fcccea7590f3e4c187c75980b353f")

    diffs = db.getCommitDiffs()

    # for x, y in diffs.items():
    #     print(x)
    #     for d in y:
    #         for i in d.listOfLineChanges:
    #             print(i)

    expected = [
    "3403e78c4b621e9a37ff6b5f008603a49dc32cf4",
    "3403e78c4b621e9a37ff6b5f008603a49dc32cf4",
    "3403e78c4b621e9a37ff6b5f008603a49dc32cf4",
    "3403e78c4b621e9a37ff6b5f008603a49dc32cf4",
    "3403e78c4b621e9a37ff6b5f008603a49dc32cf4",
    "3403e78c4b621e9a37ff6b5f008603a49dc32cf4",
    "a26e1c6bbdaea2062cfb8740aef178abe1f610f4",
    "5fb74faf5d221475ef008329f7e9a22fcaf46fcb",
    "4010bbb46caf30143c0484b7ca1ec5877e0aabf2",
    "1264d9b3f02ea27dbddbf6f71fc4f3a8c6ebf355",
    "1264d9b3f02ea27dbddbf6f71fc4f3a8c6ebf355",
    "f071712a721d15c3631d9f72938c80f0a7fc40b4",
    "1264d9b3f02ea27dbddbf6f71fc4f3a8c6ebf355",
    "b3c822c7d5e1b153e7cfa925ab35b1491aa74559",
    "b3c822c7d5e1b153e7cfa925ab35b1491aa74559",
    "b3c822c7d5e1b153e7cfa925ab35b1491aa74559",
    "7f1a82e41e38a7b369ca1f3556012fdb4066ab88",
    "3403e78c4b621e9a37ff6b5f008603a49dc32cf4",
    "3403e78c4b621e9a37ff6b5f008603a49dc32cf4",
    "3403e78c4b621e9a37ff6b5f008603a49dc32cf4",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "664546ef9a44a3cf99a7fd4ae491a98695d16693",
    "664546ef9a44a3cf99a7fd4ae491a98695d16693",
    "664546ef9a44a3cf99a7fd4ae491a98695d16693",
    "664546ef9a44a3cf99a7fd4ae491a98695d16693",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "560859fcd9af9b4280e32d48806d91057702e0b0",
    "560859fcd9af9b4280e32d48806d91057702e0b0",
    "4fa41a045be4e3654eca43cc9a6852a5fd56d3d3",
    "560859fcd9af9b4280e32d48806d91057702e0b0",
    "560859fcd9af9b4280e32d48806d91057702e0b0",
    "560859fcd9af9b4280e32d48806d91057702e0b0",
    "3403e78c4b621e9a37ff6b5f008603a49dc32cf4",
    "02b66ccb9b22580165492e99dd7053d23bd799c5",
    "02b66ccb9b22580165492e99dd7053d23bd799c5",
    "46813070acb9695a3eb4e1021597134662183b62",
    "db0dc7eae1af7a4bccd186c5933ae019635b3bc1",
    "46813070acb9695a3eb4e1021597134662183b62",
    "46813070acb9695a3eb4e1021597134662183b62",
    "02b66ccb9b22580165492e99dd7053d23bd799c5",
    "02b66ccb9b22580165492e99dd7053d23bd799c5",
    "3403e78c4b621e9a37ff6b5f008603a49dc32cf4",
    "3403e78c4b621e9a37ff6b5f008603a49dc32cf4",
    "3403e78c4b621e9a37ff6b5f008603a49dc32cf4",
    "3403e78c4b621e9a37ff6b5f008603a49dc32cf4",
    "3403e78c4b621e9a37ff6b5f008603a49dc32cf4",
    "3403e78c4b621e9a37ff6b5f008603a49dc32cf4",
    "3403e78c4b621e9a37ff6b5f008603a49dc32cf4",
    "3403e78c4b621e9a37ff6b5f008603a49dc32cf4",
    "3403e78c4b621e9a37ff6b5f008603a49dc32cf4",
    "3403e78c4b621e9a37ff6b5f008603a49dc32cf4",
    "3403e78c4b621e9a37ff6b5f008603a49dc32cf4",
    "3403e78c4b621e9a37ff6b5f008603a49dc32cf4",
    "3403e78c4b621e9a37ff6b5f008603a49dc32cf4",
    "3403e78c4b621e9a37ff6b5f008603a49dc32cf4",
    "3403e78c4b621e9a37ff6b5f008603a49dc32cf4",
    "3403e78c4b621e9a37ff6b5f008603a49dc32cf4",
    "3403e78c4b621e9a37ff6b5f008603a49dc32cf4",
    "3403e78c4b621e9a37ff6b5f008603a49dc32cf4",
    "3403e78c4b621e9a37ff6b5f008603a49dc32cf4",
    "3403e78c4b621e9a37ff6b5f008603a49dc32cf4",
    "3403e78c4b621e9a37ff6b5f008603a49dc32cf4",
    "3403e78c4b621e9a37ff6b5f008603a49dc32cf4",
    "3403e78c4b621e9a37ff6b5f008603a49dc32cf4",
    "3403e78c4b621e9a37ff6b5f008603a49dc32cf4",
    "3403e78c4b621e9a37ff6b5f008603a49dc32cf4",
    "3403e78c4b621e9a37ff6b5f008603a49dc32cf4",
    "b0bf6c5e20d72d2679d4c46adc5c193c7ed41752",
    "b0bf6c5e20d72d2679d4c46adc5c193c7ed41752",
    "b7476f1f62f9e7c5ff6d32c14617cfa5ecab51af",
    "b0bf6c5e20d72d2679d4c46adc5c193c7ed41752",
    "3403e78c4b621e9a37ff6b5f008603a49dc32cf4",
    "fd2927c37c699e4fa8965d0cb77168f3868d5793",
    "fd2927c37c699e4fa8965d0cb77168f3868d5793",
    "fd2927c37c699e4fa8965d0cb77168f3868d5793",
    "fd2927c37c699e4fa8965d0cb77168f3868d5793",
    "fd2927c37c699e4fa8965d0cb77168f3868d5793",
    "fd2927c37c699e4fa8965d0cb77168f3868d5793",
    "d7ef12e41c44dab6a3966d28fd6050f44fcec65c",
    "425076c759f131c98cb1bbd78b14ee5368a50d77",
    "425076c759f131c98cb1bbd78b14ee5368a50d77",
    "425076c759f131c98cb1bbd78b14ee5368a50d77",
    "bc2a710ea9c2348394550a919670b751e55c6080",
    "fd2927c37c699e4fa8965d0cb77168f3868d5793",
    "3403e78c4b621e9a37ff6b5f008603a49dc32cf4",
    "d2315af2ec3332d319c8ba7839707d5d7ad1691b",
    "cf01ca7e8bf670822c55b0a4b04cd5c2b0271b3e",
    "cf01ca7e8bf670822c55b0a4b04cd5c2b0271b3e",
    "d2315af2ec3332d319c8ba7839707d5d7ad1691b",
    "53b0bd2e17d2f23bea498d90de1900877e321bfd",
    "53b0bd2e17d2f23bea498d90de1900877e321bfd",
    "53b0bd2e17d2f23bea498d90de1900877e321bfd",
    "53b0bd2e17d2f23bea498d90de1900877e321bfd",
    "08c50df9386e4003a76a5fb03a3941516531403f",
    "53b0bd2e17d2f23bea498d90de1900877e321bfd",
    "53b0bd2e17d2f23bea498d90de1900877e321bfd",
    "3403e78c4b621e9a37ff6b5f008603a49dc32cf4",
    "3403e78c4b621e9a37ff6b5f008603a49dc32cf4",
    "3403e78c4b621e9a37ff6b5f008603a49dc32cf4",
]
    
    assert result == expected

def test_2048_js_game_manager_no_rename():
    databaseBuilder = DatabaseBuilder()
    databaseBuilder.setRepoType("git")
    databaseBuilder.setFileName("js/game_manager.js")
    db = databaseBuilder.build()

    db.cwd = "repos-for-testing/2048"

    significantchangepercentage = 0
    analyzer = Analyzer(db)

    result = analyzer.findLineOwnersHashes(significantchangepercentage,"3b86903e65383e30ffc836b733dcaf094c33ff10")

    # for x, y in diffs.items():
    #     print(x)
    #     for d in y:
    #         for i in d.listOfLineChanges:
    #             print(i)

    expected = [
    "02a24c0610c56da8a3e7e0ed3790f252a760e9c9",
    "8ad8318c7ce84298b17dcf0aa15f357926cb2ffa",
    "8ad8318c7ce84298b17dcf0aa15f357926cb2ffa",
    "02a24c0610c56da8a3e7e0ed3790f252a760e9c9",
    "8ad8318c7ce84298b17dcf0aa15f357926cb2ffa",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "8ad8318c7ce84298b17dcf0aa15f357926cb2ffa",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "02b66ccb9b22580165492e99dd7053d23bd799c5",
    "9626e2b060485b69d944a70ad670e251ba014aa4",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "02b66ccb9b22580165492e99dd7053d23bd799c5",
    "02b66ccb9b22580165492e99dd7053d23bd799c5",
    "02a24c0610c56da8a3e7e0ed3790f252a760e9c9",
    "cf01ca7e8bf670822c55b0a4b04cd5c2b0271b3e",
    "02b66ccb9b22580165492e99dd7053d23bd799c5",
    "02b66ccb9b22580165492e99dd7053d23bd799c5",
    "02b66ccb9b22580165492e99dd7053d23bd799c5",
    "2f912471322c62cdc3b4628010330e42541ab11f",
    "9626e2b060485b69d944a70ad670e251ba014aa4",
    "9626e2b060485b69d944a70ad670e251ba014aa4",
    "cf01ca7e8bf670822c55b0a4b04cd5c2b0271b3e",
    "9626e2b060485b69d944a70ad670e251ba014aa4",
    "9626e2b060485b69d944a70ad670e251ba014aa4",
    "6cb3d71a40f1f030efe67263a43673882ba60523",
    "5392893cd6f6f2e2fe461481729d18b870c311e3",
    "3b86903e65383e30ffc836b733dcaf094c33ff10",
    "cfbf74905fa44e72a39d50701f96b614660ba445",
    "9626e2b060485b69d944a70ad670e251ba014aa4",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "02b66ccb9b22580165492e99dd7053d23bd799c5",
    "6cb3d71a40f1f030efe67263a43673882ba60523",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "02a24c0610c56da8a3e7e0ed3790f252a760e9c9",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "02a24c0610c56da8a3e7e0ed3790f252a760e9c9",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "02a24c0610c56da8a3e7e0ed3790f252a760e9c9",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "dca5207fa4f48dfae9f0ac15a845f1d32311355f",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "dca5207fa4f48dfae9f0ac15a845f1d32311355f",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "dca5207fa4f48dfae9f0ac15a845f1d32311355f",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "dca5207fa4f48dfae9f0ac15a845f1d32311355f",
    "02a24c0610c56da8a3e7e0ed3790f252a760e9c9",
    "02a24c0610c56da8a3e7e0ed3790f252a760e9c9",
    "664546ef9a44a3cf99a7fd4ae491a98695d16693",
    "664546ef9a44a3cf99a7fd4ae491a98695d16693",
    "af683a7856485d8be156c3e070fdb7c9baff0145",
    "af683a7856485d8be156c3e070fdb7c9baff0145",
    "af683a7856485d8be156c3e070fdb7c9baff0145",
    "af683a7856485d8be156c3e070fdb7c9baff0145",
    "af683a7856485d8be156c3e070fdb7c9baff0145",
    "af683a7856485d8be156c3e070fdb7c9baff0145",
    "02a24c0610c56da8a3e7e0ed3790f252a760e9c9",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "5392893cd6f6f2e2fe461481729d18b870c311e3",
    "5392893cd6f6f2e2fe461481729d18b870c311e3",
    "5392893cd6f6f2e2fe461481729d18b870c311e3",
    "02a24c0610c56da8a3e7e0ed3790f252a760e9c9",
    "5392893cd6f6f2e2fe461481729d18b870c311e3",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "664546ef9a44a3cf99a7fd4ae491a98695d16693",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "6cb3d71a40f1f030efe67263a43673882ba60523",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "02a24c0610c56da8a3e7e0ed3790f252a760e9c9",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "6cb3d71a40f1f030efe67263a43673882ba60523",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "5392893cd6f6f2e2fe461481729d18b870c311e3",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "4b3055fcd0b88b52769574e3183434fa43922b8e",
    "e65111f13ba8ebc6d72094c5497ec81b95084ff0",
    "e65111f13ba8ebc6d72094c5497ec81b95084ff0",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "4b3055fcd0b88b52769574e3183434fa43922b8e",
    "4b3055fcd0b88b52769574e3183434fa43922b8e",
    "4b3055fcd0b88b52769574e3183434fa43922b8e",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "6cb3d71a40f1f030efe67263a43673882ba60523",
    "6cb3d71a40f1f030efe67263a43673882ba60523",
    "6cb3d71a40f1f030efe67263a43673882ba60523",
    "6cb3d71a40f1f030efe67263a43673882ba60523",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "4b3055fcd0b88b52769574e3183434fa43922b8e",
    "4b3055fcd0b88b52769574e3183434fa43922b8e",
    "4b3055fcd0b88b52769574e3183434fa43922b8e",
    "4b3055fcd0b88b52769574e3183434fa43922b8e",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
]
    
    assert result == expected

def test_2048_js_game_manager_rename():
    databaseBuilder = DatabaseBuilder()
    databaseBuilder.setRepoType("git")
    databaseBuilder.setFileName("js/game_manager.js")
    databaseBuilder.setDetectRenames(True)
    db = databaseBuilder.build()

    db.cwd = "repos-for-testing/2048"

    significantchangepercentage = 0
    analyzer = Analyzer(db)

    result = analyzer.findLineOwnersHashes(significantchangepercentage,"3b86903e65383e30ffc836b733dcaf094c33ff10")

    # for x, y in diffs.items():
    #     print(x)
    #     for d in y:
    #         for i in d.listOfLineChanges:
    #             print(i)

    expected = [
    "02a24c0610c56da8a3e7e0ed3790f252a760e9c9",
    "8ad8318c7ce84298b17dcf0aa15f357926cb2ffa",
    "8ad8318c7ce84298b17dcf0aa15f357926cb2ffa",
    "02a24c0610c56da8a3e7e0ed3790f252a760e9c9",
    "8ad8318c7ce84298b17dcf0aa15f357926cb2ffa",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "8ad8318c7ce84298b17dcf0aa15f357926cb2ffa",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "02b66ccb9b22580165492e99dd7053d23bd799c5",
    "9626e2b060485b69d944a70ad670e251ba014aa4",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "02b66ccb9b22580165492e99dd7053d23bd799c5",
    "02b66ccb9b22580165492e99dd7053d23bd799c5",
    "02a24c0610c56da8a3e7e0ed3790f252a760e9c9",
    "cf01ca7e8bf670822c55b0a4b04cd5c2b0271b3e",
    "02b66ccb9b22580165492e99dd7053d23bd799c5",
    "02b66ccb9b22580165492e99dd7053d23bd799c5",
    "02b66ccb9b22580165492e99dd7053d23bd799c5",
    "2f912471322c62cdc3b4628010330e42541ab11f",
    "9626e2b060485b69d944a70ad670e251ba014aa4",
    "9626e2b060485b69d944a70ad670e251ba014aa4",
    "cf01ca7e8bf670822c55b0a4b04cd5c2b0271b3e",
    "9626e2b060485b69d944a70ad670e251ba014aa4",
    "9626e2b060485b69d944a70ad670e251ba014aa4",
    "6cb3d71a40f1f030efe67263a43673882ba60523",
    "5392893cd6f6f2e2fe461481729d18b870c311e3",
    "3b86903e65383e30ffc836b733dcaf094c33ff10",
    "cfbf74905fa44e72a39d50701f96b614660ba445",
    "9626e2b060485b69d944a70ad670e251ba014aa4",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "02b66ccb9b22580165492e99dd7053d23bd799c5",
    "6cb3d71a40f1f030efe67263a43673882ba60523",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "02a24c0610c56da8a3e7e0ed3790f252a760e9c9",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "02a24c0610c56da8a3e7e0ed3790f252a760e9c9",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "02a24c0610c56da8a3e7e0ed3790f252a760e9c9",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "dca5207fa4f48dfae9f0ac15a845f1d32311355f",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "dca5207fa4f48dfae9f0ac15a845f1d32311355f",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "dca5207fa4f48dfae9f0ac15a845f1d32311355f",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "dca5207fa4f48dfae9f0ac15a845f1d32311355f",
    "02a24c0610c56da8a3e7e0ed3790f252a760e9c9",
    "02a24c0610c56da8a3e7e0ed3790f252a760e9c9",
    "664546ef9a44a3cf99a7fd4ae491a98695d16693",
    "664546ef9a44a3cf99a7fd4ae491a98695d16693",
    "af683a7856485d8be156c3e070fdb7c9baff0145",
    "af683a7856485d8be156c3e070fdb7c9baff0145",
    "af683a7856485d8be156c3e070fdb7c9baff0145",
    "af683a7856485d8be156c3e070fdb7c9baff0145",
    "af683a7856485d8be156c3e070fdb7c9baff0145",
    "af683a7856485d8be156c3e070fdb7c9baff0145",
    "02a24c0610c56da8a3e7e0ed3790f252a760e9c9",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "5392893cd6f6f2e2fe461481729d18b870c311e3",
    "5392893cd6f6f2e2fe461481729d18b870c311e3",
    "5392893cd6f6f2e2fe461481729d18b870c311e3",
    "02a24c0610c56da8a3e7e0ed3790f252a760e9c9",
    "5392893cd6f6f2e2fe461481729d18b870c311e3",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "664546ef9a44a3cf99a7fd4ae491a98695d16693",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "6cb3d71a40f1f030efe67263a43673882ba60523",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "02a24c0610c56da8a3e7e0ed3790f252a760e9c9",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "6cb3d71a40f1f030efe67263a43673882ba60523",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "5392893cd6f6f2e2fe461481729d18b870c311e3",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "4b3055fcd0b88b52769574e3183434fa43922b8e",
    "e65111f13ba8ebc6d72094c5497ec81b95084ff0",
    "e65111f13ba8ebc6d72094c5497ec81b95084ff0",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "4b3055fcd0b88b52769574e3183434fa43922b8e",
    "4b3055fcd0b88b52769574e3183434fa43922b8e",
    "4b3055fcd0b88b52769574e3183434fa43922b8e",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "6cb3d71a40f1f030efe67263a43673882ba60523",
    "6cb3d71a40f1f030efe67263a43673882ba60523",
    "6cb3d71a40f1f030efe67263a43673882ba60523",
    "6cb3d71a40f1f030efe67263a43673882ba60523",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "4b3055fcd0b88b52769574e3183434fa43922b8e",
    "4b3055fcd0b88b52769574e3183434fa43922b8e",
    "4b3055fcd0b88b52769574e3183434fa43922b8e",
    "4b3055fcd0b88b52769574e3183434fa43922b8e",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
]
    
    assert result == expected

def test_2048_main_css_rename():
    databaseBuilder = DatabaseBuilder()
    databaseBuilder.setRepoType("git")
    databaseBuilder.setFileName("style/main.css")
    databaseBuilder.setDetectRenames(True)
    db = databaseBuilder.build()

    db.cwd = "repos-for-testing/2048"

    significantchangepercentage = 0
    analyzer = Analyzer(db)

    result = analyzer.findLineOwnersHashes(significantchangepercentage,"837ca51b6f254c416cb74b6a1baa1bb7cc7e6fd1")

    expected = [
    "02a24c0610c56da8a3e7e0ed3790f252a760e9c9",
    "8ad8318c7ce84298b17dcf0aa15f357926cb2ffa",
    "8ad8318c7ce84298b17dcf0aa15f357926cb2ffa",
    "02a24c0610c56da8a3e7e0ed3790f252a760e9c9",
    "8ad8318c7ce84298b17dcf0aa15f357926cb2ffa",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "8ad8318c7ce84298b17dcf0aa15f357926cb2ffa",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "02b66ccb9b22580165492e99dd7053d23bd799c5",
    "9626e2b060485b69d944a70ad670e251ba014aa4",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "02b66ccb9b22580165492e99dd7053d23bd799c5",
    "02b66ccb9b22580165492e99dd7053d23bd799c5",
    "02a24c0610c56da8a3e7e0ed3790f252a760e9c9",
    "cf01ca7e8bf670822c55b0a4b04cd5c2b0271b3e",
    "02b66ccb9b22580165492e99dd7053d23bd799c5",
    "02b66ccb9b22580165492e99dd7053d23bd799c5",
    "02b66ccb9b22580165492e99dd7053d23bd799c5",
    "2f912471322c62cdc3b4628010330e42541ab11f",
    "9626e2b060485b69d944a70ad670e251ba014aa4",
    "9626e2b060485b69d944a70ad670e251ba014aa4",
    "cf01ca7e8bf670822c55b0a4b04cd5c2b0271b3e",
    "9626e2b060485b69d944a70ad670e251ba014aa4",
    "9626e2b060485b69d944a70ad670e251ba014aa4",
    "6cb3d71a40f1f030efe67263a43673882ba60523",
    "5392893cd6f6f2e2fe461481729d18b870c311e3",
    "3b86903e65383e30ffc836b733dcaf094c33ff10",
    "cfbf74905fa44e72a39d50701f96b614660ba445",
    "9626e2b060485b69d944a70ad670e251ba014aa4",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "02b66ccb9b22580165492e99dd7053d23bd799c5",
    "6cb3d71a40f1f030efe67263a43673882ba60523",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "02a24c0610c56da8a3e7e0ed3790f252a760e9c9",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "02a24c0610c56da8a3e7e0ed3790f252a760e9c9",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "02a24c0610c56da8a3e7e0ed3790f252a760e9c9",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "dca5207fa4f48dfae9f0ac15a845f1d32311355f",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "dca5207fa4f48dfae9f0ac15a845f1d32311355f",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "dca5207fa4f48dfae9f0ac15a845f1d32311355f",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "dca5207fa4f48dfae9f0ac15a845f1d32311355f",
    "02a24c0610c56da8a3e7e0ed3790f252a760e9c9",
    "02a24c0610c56da8a3e7e0ed3790f252a760e9c9",
    "664546ef9a44a3cf99a7fd4ae491a98695d16693",
    "664546ef9a44a3cf99a7fd4ae491a98695d16693",
    "af683a7856485d8be156c3e070fdb7c9baff0145",
    "af683a7856485d8be156c3e070fdb7c9baff0145",
    "af683a7856485d8be156c3e070fdb7c9baff0145",
    "af683a7856485d8be156c3e070fdb7c9baff0145",
    "af683a7856485d8be156c3e070fdb7c9baff0145",
    "af683a7856485d8be156c3e070fdb7c9baff0145",
    "02a24c0610c56da8a3e7e0ed3790f252a760e9c9",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "5392893cd6f6f2e2fe461481729d18b870c311e3",
    "5392893cd6f6f2e2fe461481729d18b870c311e3",
    "5392893cd6f6f2e2fe461481729d18b870c311e3",
    "02a24c0610c56da8a3e7e0ed3790f252a760e9c9",
    "5392893cd6f6f2e2fe461481729d18b870c311e3",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "664546ef9a44a3cf99a7fd4ae491a98695d16693",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "6cb3d71a40f1f030efe67263a43673882ba60523",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "02a24c0610c56da8a3e7e0ed3790f252a760e9c9",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "6cb3d71a40f1f030efe67263a43673882ba60523",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "5392893cd6f6f2e2fe461481729d18b870c311e3",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "4b3055fcd0b88b52769574e3183434fa43922b8e",
    "e65111f13ba8ebc6d72094c5497ec81b95084ff0",
    "e65111f13ba8ebc6d72094c5497ec81b95084ff0",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "4b3055fcd0b88b52769574e3183434fa43922b8e",
    "4b3055fcd0b88b52769574e3183434fa43922b8e",
    "4b3055fcd0b88b52769574e3183434fa43922b8e",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "6cb3d71a40f1f030efe67263a43673882ba60523",
    "6cb3d71a40f1f030efe67263a43673882ba60523",
    "6cb3d71a40f1f030efe67263a43673882ba60523",
    "6cb3d71a40f1f030efe67263a43673882ba60523",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "4b3055fcd0b88b52769574e3183434fa43922b8e",
    "4b3055fcd0b88b52769574e3183434fa43922b8e",
    "4b3055fcd0b88b52769574e3183434fa43922b8e",
    "4b3055fcd0b88b52769574e3183434fa43922b8e",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
]
    
    #assert result == expected

def test_2048_index_html_rename_total_lines_ownership():
    databaseBuilder = DatabaseBuilder()
    databaseBuilder.setRepoType("git")
    databaseBuilder.setFileName("index.html")
    databaseBuilder.setRef("master")
    databaseBuilder.setDetectRenames(True)
    db = databaseBuilder.build()

    db.cwd = "repos-for-testing/2048"

    significantchangepercentage = 0
    analyzer = Analyzer(db)

    result = analyzer.getLinesContributions(significantchangepercentage)

    # for x, y in diffs.items():
    #     print(x)
    #     for d in y:
    #         for i in d.listOfLineChanges:
    #             print(i)

    expected = []

def test_flask():
    os.chdir('../flask')
    databaseBuilder = DatabaseBuilder()
    databaseBuilder.setRepoType("git")
    databaseBuilder.setFileName("src/flask/helpers.py")
    databaseBuilder.setDetectRenames(True)
    db = databaseBuilder.build()

    db.cwd = "repos-for-testing/flask"

    significantchangepercentage = 0
    analyzer = Analyzer(db)

    result = analyzer.findLineOwnersHashes(significantchangepercentage,"4256fc63044fa0d9c2135443461689b1adaf386d")

    expected = [
    "02a24c0610c56da8a3e7e0ed3790f252a760e9c9",
    "8ad8318c7ce84298b17dcf0aa15f357926cb2ffa",
    "8ad8318c7ce84298b17dcf0aa15f357926cb2ffa",
    "02a24c0610c56da8a3e7e0ed3790f252a760e9c9",
    "8ad8318c7ce84298b17dcf0aa15f357926cb2ffa",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "8ad8318c7ce84298b17dcf0aa15f357926cb2ffa",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "02b66ccb9b22580165492e99dd7053d23bd799c5",
    "9626e2b060485b69d944a70ad670e251ba014aa4",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "02b66ccb9b22580165492e99dd7053d23bd799c5",
    "02b66ccb9b22580165492e99dd7053d23bd799c5",
    "02a24c0610c56da8a3e7e0ed3790f252a760e9c9",
    "cf01ca7e8bf670822c55b0a4b04cd5c2b0271b3e",
    "02b66ccb9b22580165492e99dd7053d23bd799c5",
    "02b66ccb9b22580165492e99dd7053d23bd799c5",
    "02b66ccb9b22580165492e99dd7053d23bd799c5",
    "2f912471322c62cdc3b4628010330e42541ab11f",
    "9626e2b060485b69d944a70ad670e251ba014aa4",
    "9626e2b060485b69d944a70ad670e251ba014aa4",
    "cf01ca7e8bf670822c55b0a4b04cd5c2b0271b3e",
    "9626e2b060485b69d944a70ad670e251ba014aa4",
    "9626e2b060485b69d944a70ad670e251ba014aa4",
    "6cb3d71a40f1f030efe67263a43673882ba60523",
    "5392893cd6f6f2e2fe461481729d18b870c311e3",
    "3b86903e65383e30ffc836b733dcaf094c33ff10",
    "cfbf74905fa44e72a39d50701f96b614660ba445",
    "9626e2b060485b69d944a70ad670e251ba014aa4",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "02b66ccb9b22580165492e99dd7053d23bd799c5",
    "6cb3d71a40f1f030efe67263a43673882ba60523",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "02a24c0610c56da8a3e7e0ed3790f252a760e9c9",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "02a24c0610c56da8a3e7e0ed3790f252a760e9c9",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "02a24c0610c56da8a3e7e0ed3790f252a760e9c9",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "dca5207fa4f48dfae9f0ac15a845f1d32311355f",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "dca5207fa4f48dfae9f0ac15a845f1d32311355f",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "dca5207fa4f48dfae9f0ac15a845f1d32311355f",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "dca5207fa4f48dfae9f0ac15a845f1d32311355f",
    "02a24c0610c56da8a3e7e0ed3790f252a760e9c9",
    "02a24c0610c56da8a3e7e0ed3790f252a760e9c9",
    "664546ef9a44a3cf99a7fd4ae491a98695d16693",
    "664546ef9a44a3cf99a7fd4ae491a98695d16693",
    "af683a7856485d8be156c3e070fdb7c9baff0145",
    "af683a7856485d8be156c3e070fdb7c9baff0145",
    "af683a7856485d8be156c3e070fdb7c9baff0145",
    "af683a7856485d8be156c3e070fdb7c9baff0145",
    "af683a7856485d8be156c3e070fdb7c9baff0145",
    "af683a7856485d8be156c3e070fdb7c9baff0145",
    "02a24c0610c56da8a3e7e0ed3790f252a760e9c9",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "5392893cd6f6f2e2fe461481729d18b870c311e3",
    "5392893cd6f6f2e2fe461481729d18b870c311e3",
    "5392893cd6f6f2e2fe461481729d18b870c311e3",
    "02a24c0610c56da8a3e7e0ed3790f252a760e9c9",
    "5392893cd6f6f2e2fe461481729d18b870c311e3",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "664546ef9a44a3cf99a7fd4ae491a98695d16693",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "6cb3d71a40f1f030efe67263a43673882ba60523",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "c48b92689dd232656b669e13c982e1d74bf753bf",
    "02a24c0610c56da8a3e7e0ed3790f252a760e9c9",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "6cb3d71a40f1f030efe67263a43673882ba60523",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "5392893cd6f6f2e2fe461481729d18b870c311e3",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "4b3055fcd0b88b52769574e3183434fa43922b8e",
    "e65111f13ba8ebc6d72094c5497ec81b95084ff0",
    "e65111f13ba8ebc6d72094c5497ec81b95084ff0",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "4b3055fcd0b88b52769574e3183434fa43922b8e",
    "4b3055fcd0b88b52769574e3183434fa43922b8e",
    "4b3055fcd0b88b52769574e3183434fa43922b8e",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "6cb3d71a40f1f030efe67263a43673882ba60523",
    "6cb3d71a40f1f030efe67263a43673882ba60523",
    "6cb3d71a40f1f030efe67263a43673882ba60523",
    "6cb3d71a40f1f030efe67263a43673882ba60523",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "53e08722e0f926c902a879c467765fbb197c07eb",
    "b20e26e3bd5940355846a1308120e2d3adc40acd",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "f18f7cee2268de6189f3129b7e68faa9df43862c",
    "4b3055fcd0b88b52769574e3183434fa43922b8e",
    "4b3055fcd0b88b52769574e3183434fa43922b8e",
    "4b3055fcd0b88b52769574e3183434fa43922b8e",
    "4b3055fcd0b88b52769574e3183434fa43922b8e",
    "cf31e146aad692a8fed02a3aa3c80af183502de8",
]
    
    #assert result == expected
