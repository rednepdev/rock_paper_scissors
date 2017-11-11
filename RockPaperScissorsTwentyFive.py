from random import randint
import time
import os
os.system('cls' if os.name == 'nt' else 'clear')

playerpoints = int(0)
computerpoints = int(0)
i = int(0) ##sets our for loop variable

playing = True

main_array = ['gun', 'dynamite', 'nuke', 'lightning', 'devil', 'dragon', 'alien', 'water', 'bowl', 'air', 'moon', 'paper', 'sponge', 'wolf',
              'cockroach', 'tree', 'man', 'woman', 'monkey', 'snake', 'axe', 'scissors', 'fire', 'sun', 'rock'] ## list of moves


def back(x):
    return main_array[x]


while playing:
    wantRules = input("Would you like the rules (Y/N)")
    if wantRules == 'Y':
        print("WARNING: Lots of text coming your way (~300 lines, so get ready to scroll!)")
        time.sleep(4)  # give them adequate warning
        rulesFile = open('rules.txt') ## moves rules.txt into a varaible
        rulesArray = rulesFile.readlines();
        rules = ''.join(rulesArray)
        print(rules) ##prints all that
        time.sleep(20)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Prepare yourself! We are going to play three rounds of rock, paper, scissors (The 25 version). Can you beat me, a computer?")
    time.sleep(4)
    os.system('cls' if os.name == 'nt' else 'clear')
    while playerpoints < 3 and computerpoints < 3 : ##checks if either scores are within the range of 3
        os.system('cls' if os.name == 'nt' else 'clear')
        computerChoice = randint(0, len(main_array))
        userMove = input('Gun, dynamite, nuke, lightning, devil, dragon, alien, water, bowl, air, moon, paper, '
                                              'sponge, wolf, cockroach, tree, man, woman, monkey, snake, axe, scissors, fire, '
                                              'sun or rock? ').lower()  ## convert to lowercase
        userChoice = main_array.index(userMove) ## gets the index of usermoveos.system('cls' if os.name == 'nt' else 'clear')

        if computerChoice == userChoice:
            print("Computer move was " + main_array[computerChoice])
            print('DRAW!')
            draw = True
            time.sleep(4)
        else:
            total = 0
            for i in range(1, 13):
                if back(computerChoice) == back(userChoice - i):
                    print("Computer move was " + main_array[computerChoice])
                    print("USER WINS!")
                    playerpoints += 1
                    draw = False
                    time.sleep(4)
                else:
                    total += 1
            if total == 12:
                print("Computer move was " + main_array[computerChoice])
                print("COMPUTER WINS!")
                computerpoints += 1
                time.sleep(4)

    if playerpoints > computerpoints:
        print("User wins by " + str(playerpoints - computerpoints) + " points")

    else:
        print("Computer wins by " + str(computerpoints - playerpoints) + " points")

    userReplay = input('Would you like to play again? (Y/N)')
    if userReplay == 'N':
        playing = False
