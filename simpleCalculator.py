print("Calculator")

def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

def multiply(a, b):
  return a * b

def divide(a, b):
  if b != 0:
    return a / b
  else:
    return "cannot divide by 0."

def calculation():

  while True:
    print("/n Select an operation.")
    print("1. Addition(+)")
    print("2. Subtraction(-)")
    print("3. Multiplication(*)")
    print("4. Division(/)")
    print("5. Exit")

    choice = input("Enter your choice (1-5):")

    if choice == "5":
      print("Exiting Calculator!")
      break

    num1 = float(input("Enter your first number:"))
    num2 = float(input("Enter your second number"))

    if choice == "1":
      print(f"The total sum is: {add(num1, num2)}")
    elif choice == "2":
      print(f"The difference is: {subtract(num1, num2)}")
    elif choice == "3":
      print(f"The Multiplication of entered number is: {multiply(num1, num2)}")
    elif choice == "4":
      print(f"The division of entered number is: {divide(num1, num2)}")
    else:
      print("Invalid Number!")

calculation()


