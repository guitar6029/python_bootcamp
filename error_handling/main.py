def add(n1,n2):
    print(n1 + n2)

#add(10,20)
# num1 = 10
# while True:
#     try:
#         num2 = float(input("Enter a number "))
#         add(num1, num2)
#         break
#     except:
#         print("Enter a number please")


# try:
#     f = open('testfile', 'w')
#     f.write('Write a test line')
# except TypeError:
#      print("there was a type error")  
# except OSError:
#      print("you have an OS error")
# finally:
#      print("i always run")     

def ask_for_init():
    result = 0
    while True:
        try:
            result = int(input('Enter a number : \n'))
            break
        except:
            print("It must be a number")
                
    return result
result = ask_for_init()
print(f"the result is {result}")        