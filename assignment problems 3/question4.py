# assignment 3 problem 4 in python
# Question 4 -> given a tuple of integers, create:
# A. tuple of all even numbers
# b.tuple of all odd numbers 

values = input("enter the list of integers:").split()
tup = tuple(map(int, values))
even =()
odd =()
for i in tup:
  if i % 2 == 0:
    even += (i,)
  else:
    odd += (i,)

print("all even numbers:", even)
print("all odd numbers:", odd)