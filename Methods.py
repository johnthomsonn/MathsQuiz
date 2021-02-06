import sys

def getTotalQuestions(): 
    try:
        questions = int(sys.argv[1])
        print("You are playing " + str(questions) + " questions.")
    except ValueError:
        questions = 10
        print("Invalid input. Playing for 10 questions.")
    except:
        questions = 5
        print("You are playing 5 quesions.")
    return questions

def getTypes():
    return ["+", "-"]