#lists 
# same types 
my_list = [1,2,3]

#different types
my_list = [ "STRINGS", 100, True]

print(f'The length of the list : ', len(my_list))

#create a new list
my_other_list = [1,2,3]
#we can combine lists using +
my_new_list = my_other_list + my_list
print(f"my_new_list : {my_new_list}")

# updated index value at index 0
my_new_list[0] = 'Hello'
print(f"my_new_list : {my_new_list}")


# new python frameworks list
pythonFrameWorks = ["Flask", "Django", "FastAPI"] 

#append new items
my_new_list.append(pythonFrameWorks[1])

print(f"my_new_list : {my_new_list}")

#sort list
my_new_list = ['d', 'x', 'a', 'n', 'f']
my_new_list.sort()
print(f"my_new_list : {my_new_list}")

