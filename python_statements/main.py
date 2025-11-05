from random import shuffle, randint

# statements such as if else , if else
# if something:
#     do something
# else:
#     do something else
#####################################
#with else if 
# if something:
#     do something
# elif something else:
#     do something else
# else:
#     do something

name = "Samantha"
if len(name) < 4:
    print("Name is short")
elif len(name) >= 4 and len(name) <= 8:
    print("Name is medium length")
else:
    print("Name is long")  
    
    
    
#another example      
already_cooked = False
if already_cooked:
    print("Food is already cooked")
else:
    print("Food is not cooked")
    
    
    
    
### loops

#for loops example
myvals = [1,2,3,4,5]
for val in myvals:
    print(val)
print("##################")    
counter = 0

#while loops 
while counter < 9:
    if counter >= len(myvals):
        break
    print(f"Current Count {counter} and index value {myvals[counter]}")        
    counter += 1
    
    
#nested loops
stringy = ""    
for val in range(1):
        for val2 in range(3):
            stringy += "*"
            print(stringy)
            
# loop for tuples
tup = ({1,2},{3,4},{5,6})
for i,y in tup:
    print(f" tup item {i}, and {y}")            
    
d = { 'k1': 1, 'k2': 2, 'k3': 3}
for key in d:
    print(f"key : {key}")
    
# if you want to get the items
for key, value in d.items():
    print(f"key, value  = {key}, {value}")   
    
    
####### break, continue, pass
##examples    

##break example
for i in range(1,10):
    if i == 3:
        print(f"i is : {i}")
        print(f"Will break out of the loop because i is {i}")
        break
    print(f"i is : {i}")
    
#continue  with range example (startOptional , stop, optionalStep)
for i in range(1,10):
    if i == 3:
        print(f"i is : {i}")
        print(f"Will continue because i is {i}")
        continue
    print(f"i is : {i}")
    
# pass example
## commonly used for empty loops
## as a place holder
for i in range (1,5):
    pass    
x = 'x' in [1,2,3]
print(x)

cards = [1,2,3,4,5]
shuffle(cards)
print(cards)

## rang with step of 2 and up to 10
for num in range(0,11,2):
    print(num)

mywords = "eating sandwiches"
startstr = " "
for character in mywords:
    startstr += character
    print(startstr)
    
    
mylist1 = [1,2,3]    
mylist2 = ["a,b,c", "d,e,f", "g,h,i"] 
for i in zip(mylist1, mylist2):
    print(i)
    
spaceman = ({"name": "John", "id": 12345})
hasNameJohn = "name" in spaceman
print(f"The spaceman has the name property : {hasNameJohn} ")


# random number
# 100 is inclusive
myrand_num = randint(0,100)
print(myrand_num)