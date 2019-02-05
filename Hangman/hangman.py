import os
import random

won = True
gameState = True

correct = False
wrong = False
easy = False
medium = False
hard = False
began = False

wordList = []
lossPoints = 0
winPoints = 0
print("*----------*Hangman*----------*\n\n")
print("   Pick a Difficulty to Begin     ")
print("----------------------------------\n")
print("E for easy: 6 loss points loses the game, and are reset after every win")
print("M for medium: 4 loss points loses the game, and do not reset")
print("H for hard: 2 loss points loses the game, and words have all letters hidden at start")
while 1:
    start = input("")
    if start == ("e" or "E"):
        easy = True
        break
    elif start == ("m" or "M"):
        medium = True
        break
    elif start == ("h" or "H"):
        hard = True
        break
    else:
        print("Not a valid choice, press choose again")
        os.system("pause")

with open("words.txt") as file:
    for line in file:
        line = line.strip()
        wordList.append(line)
while won:
    if easy:
        upper = "     ||           \O/    "
        lower = "     ||           / \    "
    elif (medium and not began) or (hard and not began):
        upper = "     ||           \O/    "
        lower = "     ||           / \    "
    began = True
    lossPoints = 0
    won = False
    gameState = True
    rando = str(random.choice(wordList))
    newRand = list(rando)
    if easy or medium:
        for x in range(random.randint(1, len(rando))):
            newRand[random.randrange(0, len(newRand))] = ' _'
    if hard:
        for x in range(0, len(rando)):
            newRand[x] = ' _'

    while gameState:
        os.system('cls')
        print("Type exit to quit at any time")
        print("Guess correctly and you win")
        print("Guess wrong and you lose a point")
        if easy:
            print("Losing 6 points means you lose! But every win resets your points")
        if medium:
            print("Losing 4 points means you lose!")
        if hard:
            print("Losing 2 points means you lose! All the letters are hidden at the start, so good luck!")
        print("     ===============     ")
        print("     ||          \|{     ")
        print("     ||           {}     ")
        print("     ||            [     ")
        print(upper)
        print("     ||            |     ")
        print(lower)
        print("     ||                  ")
        print("     ||                  ")
        print("     ||                  ")
        print("    /||\                 ")
        print("   /||||\                ")
        print("".join(newRand))
        print("Letters: " + str(len(newRand)))
        if correct:
            print("Correct!")
        if wrong:
            print("Wrong :(")
        if lossPoints < 0:
            print("Wrong Answers: " + str(lossPoints))
            if hard or (medium and (lossPoints == -3)) or (easy and (lossPoints == -5)):
                print("One more point and you lose!")

        if winPoints > 0:
            print("Wins: " + str(winPoints))
        guess = input("Take a guess")
        if len(guess) > len("a"):
            print("Please guess one letter at a time")
            os.system("pause")
            continue
        if guess == "exit":
            guess = input("Do you want to exit? Type yes or no")
            if guess == "yes":
                print("Goodbye")
                gameState = False
                break
            else:
                continue
        if guess == rando[rando.find(guess)]:
            correct = True
            wrong = False
            for x in range(0, len(rando)):
                if rando[x] == guess:
                    newRand[x] = guess
            if "".join(newRand) == rando:
                print(rando)
                print("You Win! Press any key for a new word.")
                os.system("pause")
                winPoints += 1
                won = True
                break
        else:
            wrong = True
            correct = False
            lossPoints -= 1
            if lossPoints == -1:
                if hard:
                    upper.replace("\O/", "O")
                if medium:
                    upper = upper.replace("\O", " O")
            if lossPoints == -2:
                if hard:
                    lower.replace("/ \ ", "    ")
                    print("The correct answer was: " + rando)
                    print("You lose, sorry!")
                    break
                if medium:
                    upper = upper.replace("/", " ")
            if lossPoints == -3:
                if medium:
                    lower = lower.replace("/", " ")
                if easy:
                    upper = upper.replace("\O", " O")
            if lossPoints == -4:
                if medium:
                    lower = lower.replace("\ ", "  ")
                    print("The correct answer was: " + rando)
                    print("You lose, sorry!")
                    break
                if easy:
                    upper = upper.replace("/", " ")
            if lossPoints == -5:
                lower = lower.replace("/", " ")
            if lossPoints == -6:
                lower = lower.replace("\ ", "  ")
                print("The correct answer was: " + rando)
                print("You lose, sorry!")
                break

    gameState = False
