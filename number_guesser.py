from random import randint

upper_limit = input("What is the upper limit? ")

if upper_limit.isdigit():
    upper_limit = int(upper_limit)

    if upper_limit <= 0:
        print("Enter a number larger than 0")
        quit()
else:
    print("Enter a number")
    quit()

random_number = randint(0, upper_limit)
number_guesses = 0

while True:
    guess = input(f"Guess a number between 0 and {upper_limit} (including {upper_limit}): ")
    number_guesses += 1

    if guess.isdigit():
        guess = int(guess)
    else:
        print("Enter a number")
        continue

    if guess > random_number:
        print("You guessed too high")
    elif guess < random_number:
        print("You guessed too low")
    else:
        print("You won!")
        break

print(f"You got it in {number_guesses} guesses")
