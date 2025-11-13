x = 25

def printer():
    x = 50
    return x

#scoped example
print(x) # 25
print(printer()) # 50

#global
name = 'THIS IS A GLOBAL STRING'
def greet():
    #enclosing
    name = 'Sammy'

    def hello():
        # local
        print("Hello " + name)

    hello()

greet()    