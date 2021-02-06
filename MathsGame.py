from Question import Question
import sys, time
import Methods

#Creates a set amount of questions, currently only addition, then times how long it takes you
#to answer them all

#get total number of questions
totalQuestions = Methods.getTotalQuestions()
#set all questions array
allQuestions = []

#create all the questions
for i in range(totalQuestions):
    allQuestions.append(Question())

#Start the timer
startTime = time.time()

#Loop through all questions. getting an integer answer from the user
for i in range(len(allQuestions)):    
    badInput = True
    while badInput:
        try:
            userInput = int(input(allQuestions[i].__str__() + " "))
            badInput = False
        except:
            continue
    allQuestions[i].answerQuestion(userInput)

#End the timer
endTime = time.time()

print("You have answered all your questions, here are your resuls, press enter to proceed to next")

#Show each question and the user's answer along with a true or false.
#User presses enter to proceed to the next question
for i in range(len(allQuestions)):
    input(allQuestions[i].getResult())

#Determine how many correct answers there were
totalCorrect = 0
for i in range(len(allQuestions)):
    if allQuestions[i].correct:
        totalCorrect += 1

#Determine time taken and output how many correct answers there were
timeTaken = endTime - startTime
print("You got " + str(totalCorrect) + "/" + str(totalQuestions) + " correct in " + str(int(timeTaken)) + " seconds")