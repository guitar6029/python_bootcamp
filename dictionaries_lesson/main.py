# dictionaries lesson
#dictionaries : objects retrieved by the key name

# lists are ordered, dictionaries are unordered

# example 
my_spaceship = {
    "name": "Artemis",
    "version": "1.0",
    "color": "blue",
    "tradable": True
}

print(f'spacehip name : {my_spaceship["name"]}')

#uppercase name
my_spaceship["name"] = my_spaceship["name"].upper();
print(f'spacehip name : {my_spaceship["name"]}')

#print the keys
print(f'keys : {my_spaceship.keys()}')

#print the values
print(f'values : {my_spaceship.values()}')

#print the items
print(f'items : {my_spaceship.items()}')

d = {"k1": [1,2,3]}
print(d['k1'][1]) # will be 2