from minimum_edit_distance import *

def test_passes():
    assert True

def test_minimum_edit_distance():
    word1, word2 = 'play', 'stay'
    assert minimum_edit_distance(word1, word2) == 4
