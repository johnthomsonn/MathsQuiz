import random, Methods

class Question:

    def __init__(self,maxNumber=20):
        self.left = random.randint(1,maxNumber)
        self.right = random.randrange(0, self.left)
        self.correct = None
        self.userAnswer = None
        self.type = self.determineType()


    def getAnswer(self):
        if self.type == "+":
            return self.left + self.right
        elif self.type == "-":
            return self.left - self.right

    def __str__(self):
        return str(self.left) + self.type + str(self.right) + " = "

    def answerQuestion(self, userInput):
        self.userAnswer = userInput
        self.correct = userInput == self.getAnswer()

    def getResult(self):
        return str(self.left) + self.type + str(self.right) + " = " + str(self.userAnswer) + " is " + str(self.correct)

    def determineType(self):
        return Methods.getTypes()[random.randint(0,1)]
            
