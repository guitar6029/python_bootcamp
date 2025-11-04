# strings
# strings formatting examples

#format and f-strings


# one way to format strings
#by format()
# " String here {} then also {} ".format("value1", "value2")
print('This is a string {}'.format('INSERTED'))
print("The {2} {1} {0}".format('fox', 'brown', 'quick'))
print("The {q} {b} {0}".format('fox', b='brown', q='quick'))

#another example
result = 100/777
print("The result is {r}".format(r=result))
#example  { [name] : [width].[precision] }
print("The result is {r:1.3}".format(r=result))
result = 104.15
print("The result is {r:1.3f}".format(r=result))


#f strings , introduced in python 3.6
name = "John"
print(f'Hello {name}')