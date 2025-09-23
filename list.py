student = ["Krishna", 87.23, 22, "Ithari"]
print(student)
print(student[1:3])
print(student[-1:-4:-1])
print(student[::-1])

collection = [1, "Suman", "22yrs", 85.6, "Bhaktapur"]
print(collection)
collection.append("Lokanthali")
print(collection)

new_collection = collection + ["Gatthaghar", "Balkot"]
print(new_collection)

fruits = ["mango", "apple", "litchee"]
fruits.extend(["pineapple", "banana"])
print(fruits)

numbers = [10, 3, 44, 0, 67]
# numbers.sort()
# print(numbers)

# numbers.sort(reverse=True)
# print(numbers)

numbers.reverse()
print(numbers)

numbers2 = [1, 2, 3, 4, 5]
numbers2.reverse()
print(numbers2)

numbers2.insert(2, 2)
print(numbers2)

numbers3 = [10, 11, 12, 13, 14, 15,11]
# numbers3.remove(11)
# print(numbers3)
numbers3.pop(0)
print(numbers3)

numbers4 = [16, 17, 18, 19, 10]
numbers4[0] = 5
print(numbers4)


#practice questions
#WAP to ask user to enter the name of three movies and store them in a list

movies = []
# movie1 = input(str("Enter first movie:"))
# movie2 = input(str("Enter second movie:"))
# movie3 = input(str("Enter third movie:"))

# movies.append(movie1)
# movies.append(movie2)
# movies.append(movie3)

print(movies)

#next method

mov = []
# mov.append(input("Enter 1st movie:"))
# mov.append(input("Enter 2st movie:"))
# mov.append(input("Enter 3st movie:"))

print(mov)


#WAP to check if a list conatain a palindrome of elements. (Hint: use copy() method)

list = [1,2,3,2,1]

new_list = list.reverse()

if list == new_list:
  print("palindrome")
else:
  print("Not palindrome")
