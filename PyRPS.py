# Import RandInt from Random
from random import randint

# Generate a Random Integer from 1 to 3
ranNum = randint(1, 3)

# Prompt User to Enter a Number from 1 to 3
print("+--------------------+")
print("|      1 = Rock      |")
print("|      2 = Paper     |")
print("|      3 = Scissors  |")
print("+--------------------+")

# Retrieve Input from User
uSel = int(input("User: "))

# Determine the Winner and Display the Results
if uSel == 1:

    if ranNum == 1:

        print("Its a Draw! You and the computer both chose Rock.")

    elif ranNum == 2:

        print("You lost! You chose Rock and the computer chose Paper.")

    elif ranNum == 3:

        print("You won! You chose Rock and the computer chose Scissors.")

elif uSel == 2:

    if ranNum == 1:

        print("You won! You chose Paper and the computer chose Rock.")

    elif ranNum == 2:

        print("It's a Draw! You and the computer both chose Paper.")

    elif ranNum == 3:

        print("You lost! You chose Paper and the Computer chose Scissors.")

elif uSel == 3:

    if ranNum == 1:

        print("You lost! You chose Scissors and the computer chose Rock.")

    elif ranNum == 2:

        print("You won! You chose Scissors and the computer chose Paper.")

    elif ranNum == 3:

        print("It's a Draw! You and the computer both chose Scissors.")

else:

    # Display an Error Message
    print("Please select a number from the provided list.")
