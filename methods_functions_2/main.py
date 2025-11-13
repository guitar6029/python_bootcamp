from functools import reduce

# functions and methods homework

# write a function that computes the volume of a sphere given its radius
# ((4/3 ) *pi * r) ^3

import math

def vol(rad):
    return ((4/3) * math.pi  ) * rad ** 3

print(vol(2))

# write a function that checks whether a number is in a given range ( inclusive of high and low)
def ran_check(num, low, high):
    if (num >= low and num <= high):
        return True
    
    return False

print(ran_check(10,2,7))


# WRITE A pYTHON FUNCTION THAT ACCEPTS A STRING AND CALCULATES THE NUMBER OF UPPER CASE LETTERS AND LOWER CASE LETTERS
# SAMPLE STRING 'Hello Mr Rogers, how are you this fine Tuesday?'
# Expected Output
# No. of Upper case characters : 4
# No. of lower case characters : 33


def up_low(s):
    totalUps  = 0
    totalDowns  = 0
    for letter in s:
        if letter.isupper():
            totalUps += 1
        elif letter.islower():
            totalDowns += 1
    print(f"No. of Upper case characters : {totalUps}")            
    print(f"No. of Lower case characters : {totalDowns}")            


up_low('Hello Mr Rogers, how are you this fine Tuesday?')    



# write a python function that takes a list and returns a new list with unique elements of the frist list
# sample list 
# sample list [1,1,1,1,2,2,3,3,3,3,4,4,5]
# returne list [1,2,3,4,5]

def unique_list(lst):
    return list(set(lst))

print(unique_list([1,1,1,6,1,2,2,3,3,3,3,4,5]))    


# write a python function to multiply all the numbers in a list
# sample list [1,2,3-4]
# expected result -24

def multiply(nums):
    return reduce(lambda a, b: a * b, nums)

print(multiply([1,2,3,-4]))

#check wheter the word or a phrase is a palindrome or not
def palindrome(s):
    return str((s)[::-1]) == s 

print(palindrome("tit"))

import string
# write a python function to check whether a string is pangram or not
def ispangram(str1, alphabet=string.ascii_lowercase):
    for letter in alphabet:
        if letter not in str1.lower():
            return False
    return True

print(ispangram("The quick brown fox jumps over the lazy dog"))            