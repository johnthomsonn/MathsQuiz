from Question import Question
import sys, time, datetime
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

totalCorrect = 0

#Loop through all questions. getting an integer answer from the user
for i in range(len(allQuestions)):    
    badInput = True
    while badInput:
        try:
            userInput = int(input(allQuestions[i].__str__() + " "))
            badInput = False
        except:
            continue
    if allQuestions[i].answerQuestion(userInput):
        totalCorrect += 1

#End the timer
endTime = time.time()

print("You have answered all your questions, here are your resuls, press enter to proceed to next")

#Show each question and the user's answer along with a true or false.
#User presses enter to proceed to the next question
for i in range(len(allQuestions)):
    input(allQuestions[i].getResult())


#Determine time taken and output how many correct answers there were
timeTaken = endTime - startTime
message = "You got " + str(totalCorrect) + "/" + str(totalQuestions) + " correct in " + str(int(timeTaken)) + " seconds"
print(message)

#Write result to file
file = open("Results.txt", "a")
dateTime = str(datetime.datetime.now())[slice(19)]
file.write(dateTime + " " + message + "\n")
file.close()