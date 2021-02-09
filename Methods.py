import sys



def getTypes():
    return ["+", "-", "*", "/"]

def getWhosePlaying():
    return input("Who is playing? ")

def getNumberOfQuestions():
    badInput = True
    while badInput:
        try:
            numQ = int(input("How many questions do you want? "))
            return numQ
        except KeyboardInterrupt:
            sys.exit()
        except:
            continue

def getMaxNumber():
    badInput = True
    while badInput:
        try:
            num = int(input("What is the maximum number you want for addition and subtraction? "))
            return num
        except KeyboardInterrupt:
            sys.exit()
        except:
            continue
