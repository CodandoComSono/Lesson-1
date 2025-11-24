from random import randint

computer = randint(1, 10)  # number the computer chose
attempts = 0

print("I'm thinking of a number between 1 and 10. Try to guess it!")

while True:
    player = int(input("Your guess: "))
    attempts += 1

    if player == computer:
        print(f"Congratulations! You guessed it in {attempts} attempt(s)!")
        break
    else:
        print("Wrong! Try again.")

print("Thank you for playing!")
