#tuples 
t = (1,2,3)

mylist = [12,3,45]

# <class 'tuple'>
print(f"t is type of {type(t)}")
# <class 'list'>
print(f"mylist is type of {type(mylist)}")


#count 
t.count(1)
print(t.count(1))


#tuples do not support item assignment
# so t[0] = 'NEW' will not work
