Number Guessing Game

A beginner-friendly Python project that demonstrates how to use loops and conditions to create a simple guessing game.

📌 Description

This program:

Stores a secret number
Repeatedly asks the user to guess the number
Checks if the guess is correct
Prints "Correct" if the user wins
Prints "Rejected" for wrong guesses

The loop continues until the correct number is entered.

 Concepts Used

while loop
if-else conditions
User Input
Integer Conversion using int()
Comparison Operators

💻 Code

secret = 7
guess = 5

while guess != secret:
    guess = int(input("Enter number: "))

    if guess == secret:
        print("Correct")
    else:
        print("Rejected")

▶️ Example Output

Enter number: 3
Rejected

Enter number: 5
Rejected

Enter number: 7
Correct
