import random
secret_number = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")


guessNumber = None
attempts = 0
while guessNumber != secret_number:

  guessNumber = int(input("Enter your guess number: "))
  attempts += 1

  if guessNumber < secret_number:
    print("Too low! Try again.")
  elif guessNumber > secret_number:
    print("Too high! Try again")
  else:
    print("Congratulations! You guessed it right.")

print("You took", attempts ," attempts  to guess right number.")





