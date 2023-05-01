from gitpraise.levenstein import *

def test_1():
    actual = levenshteinDistanceDP("apple", "applepie")
    expected = 3.0
    assert actual == expected

def test_2():
    actual = levenshteinDistanceDP('    <p class="game-intro">Join the numbers and get to the <strong>2048 tile!</strong></p>', "")
    expected = 89.0
    assert actual == expected

def test_3():
    actual = levenshteinDistanceDP("",'    <p class="game-intro">Join the numbers and get to the <strong>2048 tile!</strong></p>')
    expected = 89.0
    assert actual == expected

def test_4():
    actual = levenshteinDistanceDP("","")
    expected = 0.0
    assert actual == expected

def test_5():
    actual = levenshteinDistanceDP("orange","orange")
    expected = 0.0
    assert actual == expected

def test_6():
    actual = levenshteinDistanceDP("yellow","hello")
    expected = 2.0
    assert actual == expected

def test_7():
    actual = levenshteinDistanceDP("number","strong")
    expected = 6.0
    assert actual == expected

    
def test_8():
    actual = levenshteinDistanceDP("The quick brown fox jumps over the lazy dog.", "I  have always been fascinated by the mysteries of the universe.")
    expected = 47.0
    assert actual == expected