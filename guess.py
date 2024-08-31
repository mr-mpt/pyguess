import random
import sys
import time

# Not even Satan is eviler than me hahahaha
thoughts = [
            "coke", 
            "cream", 
            "book", 
            "fan", 
            "flashlight", 
            "chair", 
            "person", 
            "phone", 
            "soap", 
            "flower", 
            "texas", 
            "goofy", 
            "java", 
            "coffee", 
            "eight", 
            "github",
            "food", 
            "pepsi", 
            "toy", 
            "hopping",
            "cmd",
            "snake",
            "cat",
            "dog",
            "poo",
            "pee",
            "skibidi",
            "light",
            "eye",
            "money",
            "skunk",
            "messi",
            "ronaldo",
            "baseball",
            "basketball",
            "football",
            "hockey",
            "soccer",
            "monkey",
            "cabernet",
            "beer"
            ]


def yes():
    print("Out of:")
    time.sleep(1)
    for randthought in thoughts:
        print(randthought)
    print("(I'll give you 5 seconds to study the list)")
    time.sleep(5)
    print("what am I thinking?")
    while True:
        guess = input("answer> ")
        theanswer = random.choice(thoughts)
        if guess == theanswer:
            print("You did it!")
            break
        else:
            print("nope!")

option = input("Welcome to the ultimate guessing game! Wanna play? ")
if option == "Yes" or "yes":
    yes()
elif option == "No" or "no":
    print("Princess is scared of the game!")
    sys.exit()
else:
    print("answer 'Yes' or 'No'")
