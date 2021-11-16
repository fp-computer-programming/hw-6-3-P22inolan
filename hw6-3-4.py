# Author: IBN (AMDG) 11/15/2021

number = input("Give me a list of number or letters separated by spaces. ")
number_lst = number.split()

question = input("Do you want the middle or ends of your list? ")

if question == "ends":
    ends_lst = number_lst.copy()
    del ends_lst[1:-1]
    print(ends_lst)
else:
    middle_lst = number_lst.copy()
    del middle_lst[0]
    del middle_lst[-1]
    print(middle_lst)
