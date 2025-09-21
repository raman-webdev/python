str1 = "Hello"
str2 = "World"

final_str = str1 + " " + str2

print(final_str)
print(len(final_str))

#slicing string = accesing the parts of string

str3 = "Macbook Laptop"
print(str3)
print(len(str3))
print(str3[0:9])
print(str3[0:len(str3)])
print(str3[0:4])

#string function

str4 = "I am learning Python"
print(str4)
print(str4.endswith("Python"))

str5 = "invalid"
print(str5)
print(str5.capitalize())
print(str5)

str6 = "hpvictus"
print(str6)
print(str6.replace("v", "V"))
print(str6)

str7 = "I am currently studying python"
print(str7.find("studying "))
print(str7.count("y"))

#practice questons
#WAP tp input user's first name and print its length

name = input("Enter Username:")
print(name)
print(len(name))

#WAP to find the occrance of "$" in a string
str8 = "I am $Raman and I have balance of $4900 and debt of $100"
print(str8)
print(str8.count("$"))