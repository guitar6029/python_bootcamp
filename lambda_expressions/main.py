# lambda expressions map and filter
def square(num):
    return num ** 2

my_nums = [1,2,3,4,5]


srq_nums = list(map(square, my_nums))
print(f'sqr nums : {srq_nums}')

def splicer(mystring):
    if len(mystring) % 2 == 0:
        return 'Even'
    else:
        return mystring[0]
    
names = ['Andy', 'Eve', 'Sally']
print(f'names : {list(map(splicer,names)) }')


def check_even(num):
    return num%2==0
check_nums = [1,2,3,4,5,6,7,8,9,10]

print(list(filter(check_even, check_nums)))


square = lambda num: num ** 2

print(square(2)) # 4


cubed = lambda num: num ** 3

print(cubed(3))

getFirtChar = lambda text : text[0]

print(getFirtChar('Lisa'))