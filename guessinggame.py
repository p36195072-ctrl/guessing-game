secret = 7
guess = 5 

while guess != secret:
    guess = int(input("Enter number: "))

    if guess == secret:
        print("Correct")
    else:
        print("Rejected")


   


