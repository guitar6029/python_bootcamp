#### def __init__(self, param1, param2):
#       self.param1 = param1
#       self.param2 = param2
#   def some_method(self):
#       print(self.param1)

class Sample():
    pass

my_sample = Sample()
print(type(my_sample))

class Dog():
    
    def __init__(self, name, owner_name, favorite_treats):
        self.name = name
        self.owner_name = owner_name
        self.favorite_treats = favorite_treats
    def get_name(self):
        return self.name
    def add_treat_to_favorites(self,snack):
        self.favorite_treats.append(snack)
    def get_treats(self):
        return self.favorite_treats

rufus =  Dog('Rufus', 'Jacob', ['pickles', 'bacon strips', 'beef liver chips'])  
print(f"Dog's name is : {rufus.get_name()}")

print(f'{rufus.get_name()} favorite snacks are :')
for snack in rufus.favorite_treats:
    print(snack)
# add some new treat



class Circle():
    pi = 3.14
    def __init__(self, size: dict):
        self.size = size

circle = Circle({"width" : 10, "height": 10})
print(f'Circle width and height : {circle.size["width"]}, {circle.size["height"]}')    

### inheritance and polymorphism


class Animal():
        def __init__(self):
            print("ANIMAL CREATED")

        def who_am_i(self):
            print("I  am an animal")
        def eat(self):
            print("I am eating") 


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")
    def who_am_i(self):
        print("I am a dog")


mydog = Dog()
print(mydog.who_am_i())