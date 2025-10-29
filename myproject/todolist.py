import random 

Number = random.randint(1, 10)
 
inputNumber = None

while inputNumber != Number:

  inputNumber = int(input("Enter your guess number:")) 

  if inputNumber > Number:
    print("Too high!")
  elif inputNumber < Number:
    print("Too low!")
  else:
    print("Congratulations! You guessed it right.")
