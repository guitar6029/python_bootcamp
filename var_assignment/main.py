## work in python , but will break in other languages
my_dog = 1
my_dog = 'Sammy'
print(my_dog)

a = 5
print(f"The value of a is : {a}")

a = a + 5
print(f"The value of a is : {a}")

#overwrite a value
a = 45
print(f"The value of a should be 45 , and it is : {a}")

# to check the type , very useful
# should be int, in the console 
# it will be <class 'int'>
print(f'The type of a is : {type(a)}')

my_income = 100

tax_rate = 0.1

my_taxes = my_income * tax_rate
print(f"my_taxes is : {my_taxes}")