# use for , .split() , and ifto create a statement that will print out the words that start with "s"

st = "Sammmy Sossa Print only the words that start Sasquach with s in this sentense"
for x in st.split():
    if x[0].lower() == "s":
        print(f"word starts with s {x}")
    #print(f"word {x}") prints the word no matter what
     
     
# use range() to printa all the even numbers from 1 to 10
for x in range(1,11):
    if x % 2 == 0:
        print(f"Even number : {x}")
# also we could use step
for x in range(1,11, 2):
    print(f"Even number : {x}")    
    
mylist = []
for x in range(1, 51):
    if x % 3 == 0:
        print(f"Divisible by 3 : {x}")
        mylist.append(x)
print(f"mylist -  {mylist}")            


#write a program that prints the integers from 1 to 100, but for multiples of three print "Fizz" instead of the number and the multiples of five , print "Buzz" For numbers which are multiple of both three and five print "FizzBuzz"

for x in range(1,101):
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)    
        
        
# use list comprehensions to create a list of the first letters of every word in the string below
st = 'Create a list of the fist letters of every word in this string'
mylist = []
for x in st.split(" "):
    mylist.append(x[0])

print(f"The list with only the first character of each word from the st string, {mylist}")    


examples = "Hello this is my only example Bye"
x = 0
#another solution 
mylist4 = [word[x] for word in examples.split()]
print("my list", mylist4)