import random
number = random.randint(100,999)
guessanswers = ["","",""]
print(number)
def fermiandpico(functionguess):
    for i in range(0,3):
        if listnumber[i] == functionguess[i]:
            guessanswers[i] = "f"
    for i in range(0,3):
        if guessanswers[i] != "f":
            for q in range(0,3):
                if listnumber[i] == listguess[q] and guessanswers[q] != "f":
                    guessanswers[i] = "p"

guess = input("What is your guess?")
while len(guess) != 3:
    print("Sorry, your guess has to be 3 characters long")
    guess = input("What is your guess?")
listnumber = list(str(number))
listguess = list(str(guess))
fermiandpico(listguess)
while str(guess) != str(number):
    for i in range(0,3):
        if guessanswers[i] == "f":
            print("Fermi")
        if guessanswers[i] == "p":
            print("Pico")
    guess = input("What is your next guess?")
    while len(guess) != 3:
        print("Sorry, your guess has to be 3 characters long")
        guess = input("What is your next guess?")
    listguess = list(str(guess))
    guessanswers = ["", "", ""]
    fermiandpico(listguess)
print("Congrats! You guess the number!")