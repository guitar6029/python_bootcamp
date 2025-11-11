from random import shuffle
# methods and functions
## common snake casing
def name_of_function_example():
    print("this is a function")
    
    
#with a default argument
def get_name_and_greet(name="Johnny"):
    return name + " is here"  

#another example returns some value
def get_vals(val1, val2):
    return val1 + val2



sums = get_vals(1,2)
print(sums) 

# silly example
def check_if_has_leftovers(val1, val2):
    if val1 % val2 == 0:
        return True
    else:
        return False
    
    
# check if even for lists
def check_if_even_list(mylist):
    for number in mylist:
        if number % 2 == 0:
            return True
        else:
            pass
    return False

print(check_if_even_list([1,2,3]))        


def check_if_all_even_in_list(mylist):
    for number in mylist:
        if number % 2 != 0:
            return False
    return True


print(check_if_all_even_in_list([2,4,5]))

def get_even_numbers_from_list(mylist):
    even_nums = []
    for num in mylist:
        if num % 2 == 0:
            even_nums.append(num)
    return even_nums

mynums = get_even_numbers_from_list([1,3,2,5,6,10,4]) 
print(mynums) 

#sort mynums
mynums = sorted(mynums)       
print(mynums) 


#### unpacking tuples
stock_prices = [("SOMECOMPANY1", 450), ("SOMECOMPANY2", 120)]
stock_prices_only = []
for item in stock_prices:
    stock_prices_only.append(item[1])
    
    
print(f"stock_prices_only : {stock_prices_only}")


######

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

mylist = [11,14,16,17]
print(f"shuffled list : {shuffle_list(mylist)}")
    
    
def player_guess():
    guess= ''
    while guess not in ['0', '1', '2']:
        guess = input("Guess a number, 0, 1, or 2 \n")
        if guess in ['0', '1', '2']:
            print(f"Ok, you guessed {guess}!")
            break
        else:
            print("Try again")    
            
#######player_guess()            


def myfunc(*args):
    return sum(args) * 0.05



def fun(*args):
    return sum(args)

print(fun(5, 10, 15))   

# **kwargs example
def fun(**kwargs):
    for k, val in kwargs.items():
        print(k, val)

fun(a=1, b=2, c=3)

def myfunc(*args):
    # = [ x ** 2 for x in range(0,11) if x % 2 == 0]
    return [x for x in args if x % 2 == 0]
    #return [x for in args if x % 2 == 0]
    
print(myfunc(1,2,3,4,5,6,7,8,9,10) )


def myfunc(mystr):
    mynewstr = ''
    for index,letter in enumerate(mystr):
        if index % 2 == 0:
            mynewstr+= letter.upper()
        else:
            mynewstr+= letter.lower()
    return mynewstr        

print(myfunc("hello world"))

def lesser_of_two_evens(a,b):
    if a % 2 == 0 and b % 2 == 0:
        return a if a < b else b
    else:
        return a if a > b else b
    
print(lesser_of_two_evens(5,9))


def animal_crackers(text):
    mywords = text.split()
    return mywords[0][0].lower() == mywords[1][0].lower()
    
print("ANIMAL CRACKERS FUNCTION")
print(animal_crackers("Gitgo bitgo"))    # False
print(animal_crackers("YellowTail yesMan"))  # True
print("-------------END ANIMAL CRACKERS FUNCTION")

# other side of seven, given a value return a value that is twice as far away on the other side of 7

def other_side_of_seven(val):
    # first calculate the left side
    left_side = 7 - val
    other_side = 7 + (left_side * 2)
    return other_side

print(other_side_of_seven(4))



#makes twenty given two intergers. return True ifthe sum of the intergers is 20
# or if one of the integers is 20, ifnot , return false
# 20, 10 => True
# 12,8 => True
# 2,3 => False


# def makes_twenty(n1, n2):
#     if n1 == 20 or n2 == 20:
#         return True
#     elif n1 + n2 == 20:
#         return True
#     else:
#         return False 

def makes_twenty(n1,n2):
    return n1 == 20 or n2 == 20 or (n1 + n2) == 20
    
print("MAKES TWENTY")    
print(makes_twenty(20, 10))
print(makes_twenty(12, 8))
print(makes_twenty(2, 3))
print("------------MAKES TWENTY")  


#old macdonald : write a function that capitalized the first and fourth letters of a name
# old_macdonald('macdonald) => MacDonald
def old_macdonald(name):
    
    mystr = ''
    for index, letter in enumerate(name):
        if index == 0 or index == 3:
            mystr += letter.upper()
        else:
            mystr += letter
    return mystr        
            
        
print(old_macdonald('james'))
print(old_macdonald('macdonald'))


#master yoda given a sentence, return a sentence with the words reversed
def master_yoda(mystring):
    listy = mystring.split()[::-1]
    return "'" + " ".join(listy) + "'"

print(master_yoda("I am home"))
print(master_yoda("We are ready"))

  

#ALMOST THERE : Given an integer n , return True if n is within 10 of either 100 or 200
# almost_there(90) => True
# almost_there(104) => True
# almost_there(150) => False
# almost_there(209) => True

#primitive version
def almost_there(n):
    return (90 <= n <= 110) or (190 <= n <= 210)

#more advanced
def almost_there(numValue):
    baseA = 100
    baseB = 200
    return abs(baseA - numValue) <= 10 or abs(baseB - numValue) <= 10


print(almost_there(90))
print(almost_there(104))
print(almost_there(150))
print(almost_there(209))

#level 2 , write a function that counts the number of times a given pattern appears in a string , including overlap
# laughter("hah", "hahahah") => 3
# note 'hahahah' count('hah) only returns 2
def laughter(pattern, strval):
    count = 0
    for i in range(len(strval) - len(pattern) + 1):
        if strval[i:i+len(pattern)] == pattern:
            count += 1
    return count

print(laughter("ha", "hah3ahah3"))     

#FIND 33
#given a list of ints, return True if the array contains a 3 next to a 3 somewhere
# has_33([1,3,3]) => True   
# has_33([1,3,1,3]) => False   
# has_33([3,1,3]) => False   

def has33(mylist):
    has33Val = False
    for i in range(len(mylist) - 1 ):
        if mylist[i] == 3 and mylist[i + 1] == 3:
            has33Val = True
            break
    return has33Val

### also 
# def has33(mylist):
#    return any(mylist[i] == 3 and mylist[i + 1] == 3 for i in range(len(mylist) - 1))
#
#
#
print("HAS 33")
print(has33([3,3,1]))
print("-------------HAS 33")

#PAPER DOLL, Given a string , return a string where for every character in the original there are three characters

def paper_doll(text):
    mytripplestr = ""
    for char in text:
        mytripplestr += char * 3
    return mytripplestr
    

print(paper_doll('Hello'))

#BLACKJACK Given three integers between 1 and 11,
# if their sum is less than or queal to 21,
#return their sum. if their sum exceeds 21 and there's and eleven, 
# reduce the total sum by 10.
# finally , if the sum (even after adjustment) exceeds 21,
# return 'BUST'


def blackjack(a, b, c):
    total = a + b + c
    hasEleven = 11 in [a, b, c]

    if total <= 21:
        return total
    elif hasEleven and total - 10 <= 21:
        return total - 10
    else:
        return 'BUST'

        
print(blackjack(5,6,7)) # 18
print(blackjack(9,9,9)) # BUST  
print(blackjack(9,9,11)) # 19        


#SUMMER of 69, return the sum of the numbers
# in the array , except ignore sections of 
# numbers startingwith a 6 and extending to the next 9 (every 6 will be followed by at least one 9), return 0 for no numbers
def summer_69(mylist):
    skip = False
    total = 0
    for i in mylist:
        if i == 6:
            skip = True
            continue
        if skip:
            if i == 9:
                skip = False
                continue    
        if skip == False:
            total = total + i
            print(f"skip is false , total is {total}")    
            continue
    return total        
            
print("SUMMER OF 69")
print(summer_69([1,3,5]))  # 1, 3 ,5 = 9          
print(summer_69([4,5,6,7,8,9]))  # 4,5 = 9          
print("---------SUMMER OF 69")

# spy game : write a function that takes a list of integers and returns True if it contains 007 in order 

def spy_game(mylist):
    
    helper = [0,0,7]
    if mylist[0] == 7:
        return False
    else:
        for i in mylist:
            if len(helper) > 0 and i == helper[0]:
                #remove the first 0
                helper.pop(0)
                print(f'i == helper[0] {i}')
            print(f'i {i}')

        print(f"helper list : {helper}")
    return len(helper) == 0

print(spy_game([1,2,4,0,0,7,5])) # true
print(spy_game([1,0,2,4,0,5,7])) # true
print(spy_game([1,7,2,0,4,5,0])) # false

# Count primes , write a function that returns the number of the prime 
# that exist up to  and including a given number

# A prime number is a natural number greater than 1 that has only two factors: 1 and itself. This means it cannot be formed by multiplying two smaller natural numbers. For example, numbers like 2, 3, 5, 7, and 11 are all prime numbers.

def count_prime(num):
    if num == 0 or num == 1:
        return False
    numOfPrimes = []
    for nums in range(2,num):
        isPrime = True
        for div in range(2, nums):
            if nums % div == 0:
                isPrime = False
                break
        if isPrime:
            numOfPrimes.append(nums)    
        
    print(f'Num of primes list {numOfPrimes}')
    return len(numOfPrimes)     

print("COUNT PRIME")
print(f"{count_prime(10)}")
print("______________COUNT PRIME")