# counting positive Numbers
# problem: Given a list of numbers, count how many are positives
# numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
positive_num_count = 0
for num in numbers:
  if num > 0:
    positive_num_count += 1
print("total positive numbers is:", positive_num_count)


#sum of Even numbers
#calculate the sum of even numbers up to given numbers

entered_numbers = int(input("Enter a number:"))
even_sum = 0

for i in range(1, entered_numbers+1):
  if i % 2 == 0:
    even_sum += i

print("Total sum of even numbers in the range of entered number is:", even_sum)

# multiplication table printer 
# problem: Print the multuplication table for a given number up to 10, but skip the fifth iteration.

entered_numbers = int(input("Enter a number:"))

for i in range(1, 11):
  if i == 5:
    continue
  multiplication = entered_numbers * i
  print(f"{entered_numbers} * {i} = {multiplication}")
 

 #find the first non repeated character

characters = "testersabcabc"

for char in characters:
  print(char)
  if characters.count(char) == 1:
    print("first non repeated char is:", char)
    break

