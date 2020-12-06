# coding: utf-8
import random

print("Welcome to the guessing game! I'm thinking of a number between 1 and 50. Take a guess below and see what you "
      "get.")

userAnswer = int(input())
numberToGuess = int(random.randint(1, 50))
attempts = 1

if userAnswer == numberToGuess and attempts == 1:
    print("You got it first try! Congratulations!")

while userAnswer != numberToGuess:
    if userAnswer > numberToGuess + 5:
        print("Way too high! Try again.")
        attempts += 1
        userAnswer = int(input())
    elif userAnswer > numberToGuess:
        print("Close, but too high. Try again.")
        userAnswer = int(input())
        attempts += 1
    elif userAnswer < numberToGuess - 5:
        print("Way too low! Try again.")
        userAnswer = int(input())
        attempts += 1
    else:
        print("Too low, but not far off! Try again.")
        userAnswer = int(input())
        attempts += 1

if userAnswer == numberToGuess and attempts > 1:
    print("Congratulations! You got it in", attempts, "tries!")
