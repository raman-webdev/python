# def square_of_num(num):
#   return num ** 2 

# result = square_of_num(int(input("Enter a number:")))
# print(result)

# # Function with multiple parameters
# # problem: create a function that takes two numbers aas parameters and returns their sum

# def sum_number(num1, num2):
#   return num1 + num2

# user_input1 = int(input("Enter numner1:"))
# user_input2 = int(input("Enter number2:"))

# print(sum_number(user_input1, user_input2))


# # Polymorphism in Functions
# # write a function multiply that multiples two numbers, but can also accept and multiply strings.

# def multiply(parameter1, parameter2):
#   return parameter1 * parameter2

# input1 = int(input("Enter 1st number:"))
# input2 = input("Enter 2nd number:")

# print(multiply(input1, input2))


# function returning multiple values
# problem: create a function that returns both the area and circumstances of a circle given its radius

# def circle(radius):
#   pie = 3.14
#   area = pie * (radius ** 2)
#   circumference = 2 * pie * radius
#   return [area, circumference]



# input = float(input("Enter the radius of circle: "))
# area = circle(input)[0]

# circumference = circle(input)[1]
                       
# print(f"The area and circumference of the circle is {round(area,2)} and {round(circumference,2)} respectively.")

 

# dict = {
#   'name': "Subodh",
#   "age": 29,
#   "roll": 45,
#   "is_single": True,
# }

# detail = ""
# for key,value in dict.items():
#   if(key == "name"):
#     detail += "The name is "+ value
# print(detail)


# reverse a string

str = "Hello World from Python"

arr = str.split()

string1 = ""
for i in arr:
  print(i)
  string1 += i[len(i)::-1] + " "

print(string1)


def countInStr(full, letter):
  sum = 0
  for i in full:
    if i == letter:
      sum+=1
  return sum
    


items = "programming"
arr = list(set(items.split()))
print(arr)
items = "".join(arr)

count = []
for i in items:
  print(f"{i}: {countInStr(items, i)}")




