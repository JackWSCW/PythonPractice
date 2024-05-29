guesses = []
BEST_SELLING_CAR_BRANDS_ANSWERS = ["toyota", "volkswagen", "honda", "hyundai", "ford", "nissan", "chevrolet", "kia", "build Your Dream", "mercedes"]

# ------ FUNCTIONS --------

# welcome user and introduces the quiz
def intro():
    # Ask the user their name
    name = input("What's your name?")

    # Greet the user and introduce the quiz
    print("Welcome to this quiz,", name)
    print("This quiz is about the top 10 best selling car brands in the world.")

# Asks the user for lives and confirms is valid
def getLives():
    while True:
        lives = input("How many chances do you want?")
        try:
            # Checking if valid answer
            lives = int(lives)
            if lives >= 0:
                return lives
            else:
                print("Please choose a positive number")
        except:
            print("That wasn't a number")

# checks if answer already exists in list. Used for checking both correct answers, and previous guesses. 
def inList(answer, list):
    if answer in list:
        return True
    else:
        return False
    
# ------- MAIN CODE -------

intro()
lives = getLives()
score = 0

# Begin quiz
while lives > 0:
    answer = input("Name one of the best selling car brands in the world:\n").lower()

    # Checks if correct or wrong
    if inList(answer, BEST_SELLING_CAR_BRANDS_ANSWERS):
        # Checks if already guessed or not
        if inList(answer, guesses):
            print("You've guessed that already")
        else:
            print("Correct")
            score += 5
            guesses.append(answer)
            print("You have guessed {}. Your score is {}. You have {} chances remaining".format(len(guesses), score))
    else:
        print("Wrong")
        lives -= 1
        print("You have guessed {}. Your score is {}. You have {} chances remaining".format(len(guesses), score))

# End game
print ("Game Over. Your final score was {}".format(score))