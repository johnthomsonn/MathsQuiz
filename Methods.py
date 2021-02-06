import sys

def getTotalQuestions():    
    try:
        questions = int(sys.argv[1])
    except:
        questions = 10
    return questions

def getTypes():
    return ["+", "-"]