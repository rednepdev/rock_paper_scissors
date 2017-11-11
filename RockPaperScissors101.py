from random import randint
import time

playing = True

main_array = ['gun', 'dynamite', 'nuke', 'lightning', 'devil', 'dragon', 'alien', 'water', 'bowl', 'air', 'moon', 'paper', 'sponge', 'wolf',
              'cockroach', 'tree', 'man', 'woman', 'monkey', 'snake', 'axe', 'scissors', 'fire', 'sun', 'rock']


def switch_replacement(x):
    # populates dictionary from array
    result_dict = {}
    for i in range(0, len(main_array)):
        result_dict[main_array[i]] = i

    return result_dict[x] if x in result_dict else len(main_array)


def back(x):
    return main_array[x]


while playing:
    wantRules = input('Would you like the rules (Y/N)')
    if wantRules == 'Y':
        print('WARNING: Lots of text coming your way (~300 lines, so get ready to scroll!)')
        time.sleep(2)  # give them adequate warning
        rulesFile = open('rules.txt')
        rulesArray = rulesFile.readlines();
        rules = ''.join(rulesArray)
        print(rules)
    print('Prepare yourself! We are going to play three rounds of rock, paper, scissors (The 25 version). Can you beat me, a computer?')
    userScore = 0
    computerScore = 0

    for i in range(0, 3):
        draw = True

        while draw:
            computerChoice = randint(0, len(main_array))

            userChoice = switch_replacement(input('Gun, dynamite, nuke, lightning, devil, dragon, alien, water, bowl, air, moon, paper, '
                                                  'sponge, wolf, cockroach, tree, man, woman, monkey, snake, axe, scissors, fire, '
                                                  'sun or rock?').lower())  # convert to number
            if userChoice == len(main_array):
                print("Invalid Input")  #invalid input was given
                print("Computer won by default :-(")
                computerScore += 1
                break

            print('Computer chose ' + back(computerChoice))

            # The following logic works because of the order of the array: If computerChoice is more than twelve before the userChoice,
            # it beats the userChoice. This is better illustrated if you look in rules.txt.
            if computerChoice == userChoice:
                print('DRAW!')
                draw = True
            else:
                total = 0
                for i in range(1, 13):
                    if back(computerChoice) == back(userChoice - i):
                        print("USER WINS!")
                        userScore += 1
                        draw = False
                    else:
                        total += 1
                if total == 12:
                    print("COMPUTER WINS!")
                    computerScore += 1
                    draw = False

    if userScore > computerScore:
        print('User wins by ' + str(userScore - computerScore))

    else:
        print('Computer wins by ' + str(computerScore - userScore))

    userReplay = input('Would you like to play again? (Y/N)')
    if userReplay == 'N':
        playing = False
        break
