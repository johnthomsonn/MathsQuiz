import random, Methods

class Question:

    def __init__(self,maxNumber=20):
        self.type = self.determineType()
        if self.type == "/":
            self.createDivisionQuiestion()
        elif self.type == "*":
            self.left = random.randint(1,10)
            self.right = random.randint(1,10)
        else:
            self.left = random.randint(1,maxNumber)
            self.right = random.randint(0, self.left)
        self.correct = None
        self.userAnswer = None    


    def getAnswer(self):
        if self.type == "+":
            return self.left + self.right
        elif self.type == "-":
            return self.left - self.right
        elif self.type == "*":
            return self.left * self.right
        elif self.type == "/":
            return self.left / self.right

    def __str__(self):
        return str(self.left) + self.type + str(self.right) + " = "

    def answerQuestion(self, userInput):
        self.userAnswer = userInput
        self.correct = userInput == self.getAnswer()
        return self.correct

    def getResult(self):
        return str(self.left) + self.type + str(self.right) + " = " + str(self.userAnswer) + " is " + str(self.correct)

    def determineType(self):
        return Methods.getTypes()[random.randint(0,3)]
    
    def createDivisionQuiestion(self):
        self.right = random.randint(1,10)
        tmp = random.randint(1,10)
        self.left = self.right * tmp
        

    
            
