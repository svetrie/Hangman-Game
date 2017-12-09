from random import *

def play_game():
    print("Hi there! Would you like to play a game of hangman?")
    input("(Hit ENTER to continue or CTRL-C to quit)")
    print("Great! What list of words would you like to play from?")
    print("Options are animals, sports, and brands")

    choice  = "invalid"
    word = ""
    while(choice == "invalid"):

        choice = input("Please enter your choice: ")
        if (choice == "animals"):
            word = pickWord("animals.txt")
        elif (choice == "sports"):
            word = pickWord("sports.txt")
        elif (choice == "brands"):
            word = pickWord("brands.txt")
        else:
            print("Sorry, that wasn't a valid option")
            choice = "invalid"

    #print(word)

    sub = "-" * len(word)

    print("Here's your mystery word: ", sub)
    print("You have 10 tries to guess the word. Good luck!")

    hangman(word, sub)

    print("Would you like to play again?")
    play_again = input("Please enter yes or no: ")
    if (play_again == "yes"):
        play_game()
    else:
        print("Ok, thank you for playing!")


def pickWord(file_name):
    txt = open(file_name)
    word_list = []

    words = txt.read()
    word_list = words.split('\n')

    #for word in word_list:
    #    print (word)

    txt.close()

    num = randint(0, len(word_list) - 1)
    game_word = word_list[num]
    return game_word


def hangman(word, sub):

    tries = 10
    incorrect_guesses = []
    word_chrs = list(word)
    sub_chrs = list(sub)

    while(tries > 0):

        choice = input("Would you like to guess a letter(l) or the word(w)? ")
        if (choice == "word" or choice == "w"):
            guess = input("Enter your guess: ")
            if (guess == word):
                print("Congrats, that was it! You've won!")
                break;
            else:
                print("Sorry that was incorrect")
                tries -= 1

        elif (choice == "letter" or choice == "l"):
                guess = input("Enter your guess: ")
                correct = False
                for i in range(0, len(word_chrs)):
                    if(guess == word_chrs[i]):
                        correct = True
                        sub_chrs[i] = guess
                        sub = "".join(sub_chrs)
                if(sub == word):
                    print("Congrats, you've completed the word! You've won!")
                    break;
                elif (correct == True):
                    print("Nice guess!", guess, " is in the word")
                    print(sub)
                else:
                    print("Sorry, ", guess, " is not in the word")
                    tries -= 1
                    incorrect_guesses.append(guess)
                    print("Here are your incorrect guesses: ", ",".join(incorrect_guesses))

        else:
            print("Sorry, that is not a valid option")
            print("Please try again")

    if (tries == 0):
        print("Sorry you're out of tries. Game over")
        print("The word was ", word)


play_game()
