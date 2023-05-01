from gitpraise.levenstein import *

def test_1():
    actual = levenshteinDistanceDP("apple", "applepie")
    expected = 3.0
    assert actual == expected

def test_2():
    actual = levenshteinDistanceDP('    <p class="game-intro">Join the numbers and get to the <strong>2048 tile!</strong></p>', "")
    expected = 89.0
    assert actual == expected