# io basics

#modes
# r - read
# w - write ( will overwrite existing file or create new file)
# a - append (will add on to the end of the file)

# r+ - read and write
# w+ - write and read (overwrite existing file or create new file)


# first get the file 
myexamplefile = open("example.txt")

# we can read the file
# assign the content to a variable
content = myexamplefile.read()

# print the content
print(content)

#close the file
myexamplefile.close()

##### file locations
# get the example1 from /examplepath1/examplepath2/examplepath2.txt

# this is relative path example
examplefile = open("./examplepath1/examplepath2/examplepath2.txt")
examplepath_content = examplefile.read()
print(examplepath_content)

# DONT FORGET TO CLOSE THE FILE
examplefile.close()


#another way , it automatically closes the file
with open("./examplepath1/examplepath2/examplepath2.txt") as examplefile:
    examplepath_content = examplefile.read()
    print("with open way example, where the file is automatically closed")
    print(examplepath_content)