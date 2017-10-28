import random

playing = True


def switch_replacement(x):
    result_dict = {
        "rock": 0,
        "paper": 1,
        "scissors": 2,
    }
    return result_dict[x] if x in result_dict else 3


def back(x):
    return ["rock", "paper", "scissors"][x]


while playing:
    print("Prepare yourself! We are going to play three rounds of rock, paper, scissors. Can you beat me, a computer?")
    userScore = 0
    computerScore = 0

    for i in range(0, 3):
        draw = True

        while draw:
            computerChoice = random.randint(0, 3)

            userChoice = switch_replacement(input("Rock, paper or scissors").lower())   #convert to number

            print("Computer chose " + back(computerChoice))

            if userChoice == 0:                                     #chooses rock
                if computerChoice == 0:                             #rock
                    print("DRAW!")
                    draw = True

                elif computerChoice == 2:                           #rock crushes scissors
                    print("USER WINS!")
                    userScore += 1
                    draw = False

                else:                                               #paper covers rock
                    print("COMPUTER WINS!")
                    computerScore += 1
                    draw = False

            elif userChoice == 1:                                   #chooses paper
                if computerChoice == 1:                             #paper
                    print("DRAW!")
                    draw = True

                elif computerChoice == 0:                           #covers rock
                    print("USER WINS!")
                    userScore += 1
                    draw = False

                else:                                               #scissors cut paper
                    print("COMPUTER WINS!")
                    computerScore += 1
                    draw = False

            else:                                                   #scissors
                if computerChoice == 2:                             #scissors
                    print("DRAW!")
                    draw = True

                elif computerChoice == 1:                           #cuts paper
                    print("USER WINS!")
                    userScore += 1
                    draw = False

                else:                                               #rock crushes scissors
                    print("COMPUTER WINS!")
                    computerScore += 1
                    draw = False

    if userScore > computerScore:
        print("User wins by " + str(userScore - computerScore))

    else:
        print("Computer wins by " + str(computerScore - userScore))

    userReplay = input("Would you like to play again? (Y/N)")
    if userReplay == "N":
        playing = False
        break
