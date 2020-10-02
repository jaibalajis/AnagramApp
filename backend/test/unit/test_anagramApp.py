from app import isAnagramCheck
import app
import pytest

#Unit test cases

def test_preprocess_inputs_tc1():
    #GIVEN 2 STRINGS 
    #WHEN preprocessInputs FUNCTION IS CALLED
    #THEN CHECK IF THE 2 STRINGS ARE CONVERTED INTO LOWERCASE AND TRAILING WHITE SPACES ARE REMOVED
    result1, result2 = app.preprocessInputs('HEARt','EArth  ')
    assert result1 =='heart'
    assert result2 =='earth'


def test_preprocess_inputs_tc2():
    #GIVEN 2 STRINGS 
    #WHEN preprocessInputs FUNCTION IS CALLED
    #THEN CHECK IF THE 2 STRINGS ARE CONVERTED INTO LOWERCASE AND TRAILING WHITE SPACES ARE REMOVED
    result1, result2 = app.preprocessInputs(' THE classroom   ',' earth  ')
    assert result1 =='the classroom'
    assert result2 =='earth'    

def test_check_anagram_tc1():
    #GIVEN 2 STRINGS OF EQUAL LENGTH
    #WHEN isAnagramCheck FUNCTION IS CALLED
    #THEN CHECK IF THE 2 STRINGS ARE ANAGRAM
    result = isAnagramCheck('wolf','flow')
    assert result == True

def test_check_anagram_tc2():
    #GIVEN 2 STRINGS OF EQUAL LENGTH
    #WHEN isAnagramCheck FUNCTION IS CALLED
    #THEN CHECK IF THE 2 STRINGS ARE ANAGRAM
    result = isAnagramCheck('wolf','flew')
    assert result == False

def test_check_anagram_tc3():
    #GIVEN 2 STRINGS OF UNEQUAL LENGTH
    #WHEN isAnagramCheck FUNCTION IS CALLED
    #THEN CHECK IF THE 2 STRINGS ARE ANAGRAM
    result = isAnagramCheck('wolf','owl')
    assert result == False

def test_check_anagram_tc4():
    #GIVEN 2 STRINGS OF EQUAL LENGTH - WITH ALPHANUMERIC CHARACTER
    #WHEN isAnagramCheck FUNCTION IS CALLED
    #THEN CHECK IF THE 2 STRINGS ARE ANAGRAM
    result = isAnagramCheck('wolf','owl7')
    assert result == False    

def test_check_anagram_tc5():
    #GIVEN 2 STRINGS OF EQUAL LENGTH - WITH A SPACE INBETWEEN
    #WHEN isAnagramCheck FUNCTION IS CALLED
    #THEN CHECK IF THE 2 STRINGS ARE ANAGRAM
    result = isAnagramCheck('wo lf','flo w')
    assert result == True        

def test_check_anagram_tc6():
    #GIVEN 2 EQUAL/SAME STRINGS
    #WHEN isAnagramCheck FUNCTION IS CALLED
    #THEN CHECK IF THE 2 STRINGS ARE ANAGRAM
    result = isAnagramCheck('wolf','wolf')
    assert result == True    

def test_check_anagram_tc7():
    #GIVEN 1 STRING in LOwERCASE AND 1 IN UPPERCASE
    #WHEN isAnagramCheck FUNCTION IS CALLED
    #THEN CHECK IF THE 2 STRINGS ARE ANAGRAM
    result = isAnagramCheck('wolf','FLOW')
    assert result == False      

def test_build_all_anagrams_dict_tc1():
    #GIVEN 2 DICT - SAME STRINGS
    #WHEN buildAllAnagramsDict FUNCTION IS CALLED
    #THEN CHECK IF THE 2 DICTS ARE EQUAL AND THEIR VALUES ARE ADDED TOGTHER
    popularAnagramDict = app.buildAllAnagramsDict('heart','earth')
    app.popularAnagramDict = popularAnagramDict
    resultDict = app.buildAllAnagramsDict('heart', 'earth')
    assert resultDict[('heart','earth')]==2


def test_build_all_anagrams_dict_tc2():
    #GIVEN 2 DICT - CASE SENSITIVE STRINGS
    #WHEN buildAllAnagramsDict FUNCTION IS CALLED
    #THEN CHECK IF THE 2 DICTS ARE EQUAL AND THEIR VALUES ARE ADDED TOGTHER
    popularAnagramDict = app.buildAllAnagramsDict('heart','earth')
    app.popularAnagramDict = popularAnagramDict
    resultDict = app.buildAllAnagramsDict('Heart', 'eaRth')
    assert resultDict[('heart','earth')]==3

def test_build_all_anagrams_dict_tc3():
    #GIVEN 2 DICT - STRINGS INCLUDE SPACE
    #WHEN buildAllAnagramsDict FUNCTION IS CALLED
    #THEN CHECK IF THE 2 DICTS ARE EQUAL AND THEIR VALUES ARE ADDED TOGTHER
    popularAnagramDict = app.buildAllAnagramsDict('heart','earth')
    app.popularAnagramDict = popularAnagramDict
    resultDict = app.buildAllAnagramsDict('Hea rt', 'eaRth')
    assert resultDict[('heart','earth')]==4


def test_build_popular_anagram_list_tc1():
    #GIVEN 2 DICT - STRINGS INCLUDE SPACE
    #WHEN buildAllAnagramsDict FUNCTION IS CALLED
    #THEN CHECK IF THE 2 DICTS ARE EQUAL AND THEIR VALUES ARE ADDED TOGTHER
    app.popularAnagramDict = {('part','trap'):1,('earth','heart'):3,('money','king'):3}
    popularAnagramsList = app.buildPopularAnagramsList()
    assert len(popularAnagramsList)==3
    assert popularAnagramsList[0]['word1']=='earth'
    assert popularAnagramsList[0]['word2']=='heart'
    assert popularAnagramsList[0]['count']==3
    assert popularAnagramsList[1]['word1']=='money'
    assert popularAnagramsList[1]['word2']=='king'
    assert popularAnagramsList[1]['count']==3

def test_build_popular_anagram_list_tc2():
    #GIVEN 2 DICT - STRINGS INCLUDE SPACE
    #WHEN buildAllAnagramsDict FUNCTION IS CALLED
    #THEN CHECK IF THE 2 DICTS ARE EQUAL AND THEIR VALUES ARE ADDED TOGTHER
    app.popularAnagramDict = {('part','trap'):1,('earth','heart'):3,('money','king'):2}
    popularAnagramsList = app.buildPopularAnagramsList()
    assert len(popularAnagramsList)==3
    assert popularAnagramsList[0]['word1']=='earth'
    assert popularAnagramsList[0]['word2']=='heart'
    assert popularAnagramsList[0]['count']==3
    assert popularAnagramsList[1]['word1']=='money'
    assert popularAnagramsList[1]['word2']=='king'
    assert popularAnagramsList[1]['count']==2
    assert popularAnagramsList[2]['word1']=='part'
    assert popularAnagramsList[2]['word2']=='trap'
    assert popularAnagramsList[2]['count']==1
