"""Game that only completes when you guess the right number."""

from random import randint

secret: int = randint(1, 10)
guess: int = int(input("Guess a number between 1 and 10: "))
max_tries: int = 2
tries_count: int = 0

while guess != secret and (tries_count < max_tries):
    print("Wrong!")
    if (guess < 1) or (guess > 10):
        print("That's not between 1 and 10!")
    if guess > secret:
        print("Your guess was too high!")
    else:
        print("Your guess was too low!")
    guess = int(input("Guess again! You have " + str(int(2 - tries_count)) + " tries left."))
    tries_count += 1

if (tries_count == max_tries) and (guess != secret):
    print("You ran out of tries baby girl :=()")

if guess == secret:
    print("You got it!")
