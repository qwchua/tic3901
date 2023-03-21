from gitpraise.scanner import *

# def test_1():
#     s = Scanner("git")
#     s.cwd = "repos-for-testing/2048"
#     #print("\n")
#     s.findAllFilesTracked()

#     # assert db.filename == "index.html"

# def test_2():
#     scanner = Scanner("git")
#     print("\n")

#     results = scanner.scan("README.rst")
#     print(results)

def test_3():
    scanner = Scanner("git")
    print("\n")

    results = scanner.findHashFromRef("0.7")
    print(results)