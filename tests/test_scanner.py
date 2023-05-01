import os
import pytest
from gitpraise.scanner import Scanner
    
@pytest.fixture
def create_scanner(type = "git"):
    scanner = Scanner(type)
    return scanner

@pytest.fixture(scope='module')
def temp_directory(tmpdir_factory):
    test_dir = tmpdir_factory.mktemp("sample_dir")
    test_file1 = test_dir.join("test_file1.txt")
    test_file2 = test_dir.join("test_file2.txt")
    test_file1.write("This is test_file1.")
    test_file2.write("This is test_file2.")
    return str(test_dir)

def test_find_all_files_tracked(temp_directory, create_scanner):
    os.chdir(temp_directory)
    os.system("git init")
    os.system("git add .")
    os.system("git commit -m 'Initial commit'")

    scanner = create_scanner
    files = scanner._Scanner__findAllFilesTracked("")

    assert "test_file1.txt" in files
    assert "test_file2.txt" in files

def test_find_all_files_in_directory(temp_directory, create_scanner):
    scanner = create_scanner
    files = scanner._Scanner__findallFilesInDirectoy(temp_directory)

    print("Found files:")
    for file in files:
        print(file)

    assert os.path.join(temp_directory, "test_file1.txt") in files
    assert os.path.join(temp_directory, "test_file2.txt") in files

def test_find_files_all(temp_directory):
    os.chdir(temp_directory)
    os.system("git init")
    os.system("git add .")
    os.system("git commit -m 'Initial commit'")

    scanner = Scanner("git")
    files = scanner.findFiles("ALL")

    assert "test_file1.txt" in files
    assert "test_file2.txt" in files

def test_find_files_single(temp_directory):
    scanner = Scanner("git")
    file_path = os.path.join(temp_directory, "test_file1.txt")
    print("printing file_path from test_find_files_single "+file_path)
    files = scanner.findFiles(file_path)
    print("printing files from test_find_files_single "+files.__str__())

    assert any("test_file1.txt" in file_path for file_path in files)

def test_find_files_directory(temp_directory):
    scanner = Scanner("git")
    files = scanner.findFiles(temp_directory)
    print("printing files from test_find_files_directory"+ files.__str__())

    # assert "test_file1.txt" in files
    # assert "test_file2.txt" in files
    assert any("test_file1.txt" in file_path for file_path in files)
    assert any("test_file2.txt" in file_path for file_path in files)


def test_find_files_invalid_path(temp_directory):
    scanner = Scanner("git")
    files = scanner.findFiles("non_existent_path")

    assert len(files) == 0
