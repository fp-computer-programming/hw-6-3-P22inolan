# Author: IBN (AMDG) 11/15/2021

numbers = input("Give me a list of numbers. ")

print(numbers)

number_lst = numbers.split()

sorter = number_lst.copy()

sorter.sort()

if number_lst == sorter:
    print("The list is sorted.")
else:
    print("The list is not sorted.")
