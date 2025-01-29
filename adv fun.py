# # # # # #1st
# lambda arg:exp
# obj=map(lambda i:i**2,[1,2,3,4,5])
# print(list(obj))

# numbers=[1,2,3,4,5,6,7,8]
# def positive(i):
#     return i%2==0
# obj=filter(positive,numbers)
# print(list(obj))

# obj=filter(lambda i:i%2==0,[1,2,3,4,5,6,7,8])
# print(list(obj))

# # # # # #2nd 
# def even(i):
#     return i%2==0
# obj=filter(even,[1,2,3,4,5,6])
# print(list(obj))

# def even(i):
#     return i%2==0
# print(even (4))

# # # # #3rd
# from functools import reduce
# def add(a,b):
#     return a+b
# obj=reduce(add,[1,2,3,4,5,6,7,8])
# print(obj)


# # #4th
# name="Bhargavi"
# vowels_count=sum(1 for char in name if char.lower()in "aeiou")
# print(vowels_count)