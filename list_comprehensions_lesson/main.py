### list comprehensions examples

# what they are :
# list comprehensions are a way to create a new list based on the values of an existing list

mystring = "hello"
mylist = []
for letter in mystring:
    mylist.append(letter)
    
print("mylist: ", mylist)    

mylist = [x for x in 'jambalya soup mixer']
print("mylist: ", mylist)

# one way, but could get more confusing 
mylist = [ x ** 2 for x in range(0,11) if x % 2 == 0]
print("mylist: ", mylist)

# easier , and much more readable
mylist = []
for x in range(0,11):
    if x % 2 == 0:
        mylist.append(x ** 2)
print("mylist case 2, much more readable: ", mylist)        

startingPoint = 101
for x in range(101, 0, -1):
    if x % 2 == 0:
        print(f"{x} Fizz")
    else:
        print(f"{x} Buzz")    