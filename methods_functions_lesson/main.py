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
    if mywords[0][0].lower() == mywords[1][0].lower():
        return True
    else:
        return False
    
    
print(animal_crackers("Gitgo bitgo"))    # False
print(animal_crackers("YellowTail yesMan"))  # True


# other side of seven, given a value return a value that is twice as far away on the other side of 7

def other_side_of_seven(val):
    # first calculate the left side
    left_side = 7 - val
    other_side = 7 + (left_side * 2)
    return other_side

print(other_side_of_seven(4))


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
    base100 = 100
    base200 = 200
    return abs(base100 - numValue) <= 10 or abs(base200 - numValue) <= 10


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