from app import isAnagramCheck
import app
import pytest

#Unit test cases

def test_check_anagram_correct():
    result = isAnagramCheck('wolf','flow')
    assert result == True

def test_check_anagram_false():
    result = isAnagramCheck('wolf','flew')
    assert result == False

def test_build_popular_anagram_list():
    app.popularAnagramDict = {('part','trap'):1,('earth','heart'):3}
    popularAnagramsList = app.buildPopularAnagramsList()
    assert len(popularAnagramsList)==2
    assert popularAnagramsList[0]['word1']=='earth'
    assert popularAnagramsList[0]['word2']=='heart'
    assert popularAnagramsList[0]['count']==3

def test_build_all_anagrams_dict():
    popularAnagramDict = app.buildAllAnagramsDict('heart','earth')
    app.popularAnagramDict = popularAnagramDict
    resultDict = app.buildAllAnagramsDict('heart', 'earth')
    assert resultDict[('heart','earth')]==2


def test_preprocess_inputs():
    result1, result2 = app.preprocessInputs('HEARt','EArth  ')
    assert result1 =='heart'
    assert result2 =='earth'