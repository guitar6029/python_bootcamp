# Errors and Exceptions Homework

#Problem 1
# handle the exception thrown by the code below by using try and except blocks.

# for i in ['a', 'b', 'c']:
#     print(i ** 2)

def prob_1(list):
    
    sqr_list = []
    for i in list:
        try:
            attempt = i ** 2
            sqr_list.append(attempt)
        except:
            print(f'the value must be numbers and not strings: {i} ')
    return sqr_list        

mylist = ['a', 2, 4]

sqrt_list = prob_1(mylist)
for i in sqrt_list:
    print(i)


def divide(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        return 0

result = divide(4,0)    
print(f"result : {result} ")
result = divide(4,2)    
print(f"result : {result} ")

#ask for integer
#which then prints the square of it
# use a while loop with a try,except, else block
def ask():
    input_num = 0    
    while True:
        try:
            input_num = int(input("Enter a number , integer, 1,12, 54 etc..."))
        except:
            print('Enter a number , INTEGER ONLY ..........')    
        else:   
            sqr_val = input_num ** 2
            print(f"The value is : {sqr_val}")
            break

ask()