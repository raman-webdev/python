score = 0

print("Who is the present interim prime-minister of Nepal?")
ans1 = input("Enter Answer:").lower()
if ans1 == "sushila karki":
  print("Correct Answer")
  score += 1
else:
  print("Wrong Answer")


print("What is the total population of Nepal?")
ans2 = input("Enter answer:").lower()
if ans2 == "26494504":
  print("Correct Answer")
  score += 1
else:
  print("wrong answer")

print("Total score is:", score)
