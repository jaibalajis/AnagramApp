from flask import Flask, request
from flask_cors import CORS
from operator import itemgetter

app = Flask(__name__)
CORS(app)

# Should ideally be maintained in a database
popularAnagramDict ={}

@app.route('/checkAnagram', methods=['GET'])
def checkAnagram():
    """
    The check anagram route that checks for whether a given pair of words/phrases are an Anagram.

    Type
    ----
        GET request

    Returns
    -------
    response: Obj
        Returns a response object containing whether it is an anagram and the most popular anagrams requests made.
    """
    word1 = request.args.get('word1')
    word2 = request.args.get('word2')
    if word1 and word2:
        word1, word2 = preprocessInputs(word1, word2)
        isAnagram = isAnagramCheck(word1, word2)
        if isAnagram:
            print("Popular Anagrams Dict:", popularAnagramDict)
            buildAllAnagramsDict(word1, word2)
            popularAnagramsList = buildPopularAnagramsList()
            print("popularAnagramsList",popularAnagramsList)
            return {
                "isAnagram" : "true",
                "popularAnagramsList": popularAnagramsList
            }
        else:
            popularAnagramsList = buildPopularAnagramsList()
            return {
                "isAnagram" : "false",
                "popularAnagramsList": popularAnagramsList
            }
    else:
        return "Please enter a proper word"
        
def isAnagramCheck(input1, input2):
    """
    Checks for whether a given pair of words/phrases are an Anagram.

    Parameters
    ----------
    input1: str
        The first input word used for anagram check
    input2: str
        The second input word used for anagram check
    
    Returns
    -------
    result: bool
        A boolean value that says true if the given pair of words are an anagram and returns false if not.
    """
    input1 = input1.replace(" ","")
    input2 = input2.replace(" ","")
    if len(input1)!= len(input2):
        return False
    elif sorted(input1) == sorted(input2):
        return True
    else:
        return False

def buildAllAnagramsDict(input1, input2):
    """
    Builds/adds to a dictionary of all the successful Anagram check requests that comes in.

    Parameters
    ----------
    input1: str
        The 1st input word used for anagram check
    input2: str
        The second input word used for anagram check
    
    Returns
    -------
    anagramDict: dict
        A dictionary that contains the succesful anagram pairs as keys and the number of times it is requested as the value.
    """
    keypair = (input1, input2)
    keypair2 = (input2, input1)
    if len(popularAnagramDict)>0 and keypair in popularAnagramDict.keys():
        popularAnagramDict[keypair]=popularAnagramDict[keypair]+1
    else:
        popularAnagramDict[keypair] = 1
    return popularAnagramDict
    
def buildPopularAnagramsList():
    """
    Builds a final list that contains the top 10 most requested anagrams.

    Parameters
    ----------
    anagramDict: dict
        A dictionary that contains all the succesful anagram pairs as keys and the number of times it is requested as the value.
    
    Returns
    -------
    popularAnagramsList: list
        A list that contains the top 10 most requested anagram pairs with their request count.
    """
    sortedDict = dict( sorted(popularAnagramDict.items(),key=itemgetter(1), reverse=True)[:10])
    popularAnagramsList=[]
    for key,value in sortedDict.items():
        popularAnagramsList.append({
            "word1": key[0],
            "word2": key[1],
            "count": value
        })
    return popularAnagramsList

def preprocessInputs(input1, input2):
    """
    Preprocess to convert inputs to lowercase and remove excess whitespaces

    Parameters
    ----------
    input1: str
        The 1st input word used for anagram check
    input2: str
        The second input word used for anagram check
    
    Returns
    -------
    input1: str
        The processed word after converting lower case and trailing whitespaces are removed

    input2: str
        The processed word after converting lower case and trailing whitespaces are removed

    """
    input1 = input1.lower().strip()
    input2 = input2.lower().strip()
    return input1, input2

if __name__ == '__main__':
    app.run(host="0.0.0.0")