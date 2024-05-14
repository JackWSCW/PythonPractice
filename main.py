play = "yes"

QUESTION_FORMAT = "{}\nA.{} B.{} C.{} D.{}"
while play == "yes":
    print("Hello")
    score = 0
    # ask the user their name 
    name = input("What is your name?")
    # greet the user and ask their name
    print("Welcome to this quiz,", name)
    print("This quiz is about fish.")
    tries = input("How mant attempts do you want at each question? 1-4")
    tries = int(tries) 
    try:
        number = int(number)
    except:
        print("Oh no, that didn't work!")
    # ask the user a question
    question ="What is the best estimate for how many fish are in the whole ocean?"
    a = "4,200,000,000,000"
    b = "2,560,000,000"
    c = "3,500,000,000,000"
    d = "9,150,000,500,000"
    answer = input(QUESTION_FORMAT.format(question, a, b, c, d)).lower()
    if answer == c or answer == "c".lower():
        print("Correct!")
        score += 5
    elif answer == "":
        print("Not Sure?")
    elif answer != a and answer != "a" and answer != b and answer != "b" and answer != d and answer != "d":
        print("That wasn't an option")
    else:
        print("You are wrong")
    # check the users answer and give them feedback
    print("The answer is 3,500,000,000,000!")
    # ask the user a question
    question = "What is the worlds largest fish?"
    a = "The Whale Shark"
    b = "The Blue Whale"
    c = "The Basking Shark"
    d = "Megalodon"     
    answer = input(QUESTION_FORMAT.format(question, a, b, c, d)).lower()        
    if answer == a or answer == "a".lower():
        print("Correct!")
        score += 5
    elif answer == "":
        print("Not Sure?")
    elif answer != a and answer != "a" and answer != b and answer != "b" and answer != d and answer != "d":
        print("That wasn't an option")
    else:
        print("You are wrong")
    # check the users answer and give them feedback
    print("The answer is the Whale Shark!")
    play = input("Do you want to play again?").lower()
# end the quiz and thank them for playing
print("That is the end of the quiz {}. Thank you for playing! Your final score was {}".format(name, score))