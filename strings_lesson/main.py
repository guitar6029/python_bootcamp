### strings

####Strings are not mutable! 
# (meaning you can't use indexing to change 
# individual elements of a string)

name = "John"
print(name)

#to get rid of white space from the sides
# we can use strip()
#for example
name = "       This has some spaces and the name is John     "
#how the string looks like without the strip()
print(name)
#how the string looks like after the strip
print(name.strip())

#escape sequences
# \n new line
# \t tab
# \r carriage return
print("This is a \n new line")
print("This is a \t tab")
print("This is a \r carriage return")


#check the lenght of the string
name = "John"
print(f'len(name) is {len(name)}')

#indexing
mystring = "Hello World"
print(mystring)

#grab the first letter
myfirstletter = mystring[0]
print(myfirstletter)

#return the last letter
mylastletter = mystring[-1]
print(mylastletter)

secondtolastletter = mystring[-2]
print(secondtolastletter)


#slicing
mystring = "abcdefghiklmnopqrstuvwxyz"
#from the 2 character  to end
print(mystring[2:])

uptoposition3 = mystring[:3]
print("The first 3 characters are, :3 is inclusive \n so a,b,c " + uptoposition3)

# grab 2 a 4
print(mystring[2:4])

# also valid to show the enitre string
print(mystring[::])

# step by 2
print(mystring[::2])
# should be a,c,e,g,i, l, n, p, r, t, v, x, z

#reverse string
myreversedstring = mystring[::-1]
print(myreversedstring)

mystring = 'This is python'[2]
print(mystring)
print('tinker'[1:4])

#string properties and methods
# strings are immutable
# so name[0] = 'j' will not work

#but this wll
pam = 'pam'
myletter_j = 'j'
mylastletters = pam[1:]
print(mylastletters); 
newname = myletter_j + mylastletters
print(newname)

#let me sleep
myz = 'z'
myz = myz * 10
print(myz)

print("2" + "3")
# type str
print(type("2" + "3"))

x = 'Hows it going?'
print("Uppercase : ", x.upper())
uppercase = x.upper()
print(uppercase)
words = x.split()
print(words)