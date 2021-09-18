"""
1. Write a Python Program to print Prime Numbers between 2 numbers


"""
for num in range(100, 200):
  if all(num% i !=0 for i in range(2, num)):
    print(num)
