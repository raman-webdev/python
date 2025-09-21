# userInput = int(input("Enter age:"))

# if userInput>=18:
#   print("User is eligible to vote.")
# else:
#   print("User is underage to vote.")


grade = int(input("Enter grade:"))

if grade >= 90:
  print("A+")
elif grade < 90 and grade >= 80:
  print("A")
elif grade < 80 and grade >= 70:
  print("B+")
elif grade < 70 and grade >= 60:
  print("B")
elif grade < 60 and grade >= 40:
  print("passed")
else:
  print("Failed")


#nested if-else

age = int(input("Enter Age:"))

if age>= 18:
  if age>= 70:
    print("Not allowed to drive")
  else:
    print("Allowed to drive")  
else:
  print("Not eligible to drive")


#Practice Questions
  
#WAP to check if a number entered by user is odd or even
  
num = int(input("Enter a number:"))

if num%2 == 0:
  print("Entered number is even")
else:
  print("Entered number is odd")


#WAP to find the greatest of 3 numbers entered by users

enteredNum1 = int(input("Enter first num: "))
enteredNum2 = int(input("Enter second num: "))
enteredNum3 = int(input("Enter third num: "))

# Case 1: All numbers equal
if enteredNum1 == enteredNum2 == enteredNum3:
    print("All the entered numbers are equal")

# Case 2: Two numbers equal and greater than the third
elif enteredNum1 == enteredNum2 and enteredNum1 > enteredNum3:
    print("num1 and num2 are equal but greater than num3")
    print(enteredNum1, "is greatest")
elif enteredNum1 == enteredNum3 and enteredNum1 > enteredNum2:
    print("num1 and num3 are equal but greater than num2")
    print(enteredNum1, "is greatest")
elif enteredNum2 == enteredNum3 and enteredNum2 > enteredNum1:
    print("num2 and num3 are equal but greater than num1")
    print(enteredNum2, "is greatest")

# Case 3: All numbers different
elif enteredNum1 > enteredNum2 and enteredNum1 > enteredNum3:
    print(enteredNum1, "is greatest")
elif enteredNum2 > enteredNum1 and enteredNum2 > enteredNum3:
    print(enteredNum2, "is greatest")
else:
    print(enteredNum3, "is greatest")


#WAP to check if a number is a multiple of 7 or not

x =  int(input("Enter number:"))

if x%7 == 0:
   print(x,"is multiple of 7")
else:
   print(x,"is not multiple of 7")
