import random

print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 50.")
print("Try to guess the number!\n")

# Computer chooses a random number
secret_number = random.randint(1, 50)

# Number of attempts the player gets
attempts = 7

while attempts > 0:
    print("Total Attempts:", attempts)

    # Asking the user for their guess
    guess = input("Enter your guess: ")

    # Checking if input is a number
    if not guess.isdigit():
        print("Please enter a valid number!\n")
        continue

    guess = int(guess)

    # Comparing guess with the secret number
    if guess == secret_number:
        print("🎉 Congratulations! You guessed the correct number:", secret_number)
        break
    elif guess > secret_number:
        print("Too high! Try a smaller number.\n")
    else:
        print("Too low! Try a bigger number.\n")

    attempts -= 1

# If player runs out of attempts
if attempts == 0:
    print("😞 You ran out of attempts!")
    print("The number was:", secret_number)
