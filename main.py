play = "yes"
import random

QUESTION_FORMAT = "{}\nA.{} B.{} C.{} D.{}"
GOOD_COMMENTS = ["Way to go!", "Keep it up!", "Fantastic!"]
BAD_COMMENTS = ["Keep Trying", "Maybe next time", "Don't give up"]
QUESTIONS = ["What is the best estimate for how many fish are in the whole ocean?",
             "What is the name of the largest fish in the ocean?",
             "What is the average lifespan of a shark?"]
OPTIONS = [["4,200,000,000,000", "2,560,000,000", "3,500,000,000,000", "9,150,000,500,000"],
           ["The whale shark", "The basking shark", "Tiger shark", "Great white shark",]
           ["10-20 years", "20-30 years", "30-40 years", "40-30 years"]]
SHORT_OPTIONS = ["a", "b", "c", "d"]
ANSWERS = [3,1,2]
# ask the user their name 
name = input("What is your name?")

# greet the user 
print("Welcome to this quiz,", name)
print("This quiz is about fish.")

# Check number of question attempts
while True:
    try:   
        tries = input("How mant attempts do you want for each question? 1-4")
        tries = int(tries) 
        break
    except:
        print("That's not a number")

# Start the quiz
while play == "yes":
    score = 0
    # loop through each questions/answers
    for i in range(len(QUESTIONS)):
        question_attempts = tries
        while question_attempts > 0:
            # ask the user a question
            answer = input(QUESTION_FORMAT.format(QUESTIONS[i], OPTIONS[i][0],
                                                OPTIONS[i][1], OPTIONS[i][2], OPTIONS[i][3])).lower()
    
            # check the users answer
            if answer == OPTIONS[i][ANSWERS[i]] or answer == SHORT_OPTIONS[ANSWERS[i]]:
                print("Correct!")
                score += 5
                print(random.choice(GOOD_COMMENTS))
                break
            elif answer == "":
                print("Not sure?")
            elif answer in SHORT_OPTIONS or answer in OPTIONS[i]:
                print("Wrong!")
                print(random.choice(BAD_COMMENTS))
            else:
                print("That wasn't an option")


            question_attempts -= 1
        print("The answer is 3,500,000,000,000")

        

    # end the quiz and thank them for playing
    print("That is the end of the quiz {}. Thank you for playing! Your final score was {}".format(name, score))

    # replay
    play = input("Do you want to play again?").lower()

print("Goodbye")