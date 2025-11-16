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



#polymorphism
class Dog():
    def __init__(self,name):
        self.name = name
    def speak(self):
        return self.name + " says woof!"
    



class Cat():
    def __init__(self,name):
        self.name = name
    def speak(self):
        return self.name + " says meow!"


niko = Dog("niko")        
felix = Cat("felix") 

print(niko.speak())
print(felix.speak())



for pet in [niko, felix]:
    print(type(pet))
    print(type(pet.speak()))



class Guitar():
    def __init__(self, num_strings, type_guitar, price, year):
        self._num_strings = num_strings
        self._type_guitar = type_guitar
        self._price = price
        self._year = year
    @property
    def num_strings(self):
        return self._num_strings
    @property
    def type_guitar(self):
        return self._type_guitar
    
    @property
    def price(self):
        return self._price
    
    @property
    def year(self):
        return self._year
    
    def play_sound(self):
        return ("Strumming a guitar")
    
    def __str__(self):
        return f"# of strings : {self._num_strings}\nType: {self._type_guitar}\nYear: {self._year}\nPrice: {self._price}\n"
    
    def __len__(self):
        return self._num_strings
    def __eq__(self, other):
        return (self._year == other.year and self._num_strings == other.num_strings and self._price == other.price)
    
class Gibson(Guitar):
    def __init__(self, brand, num_strings, type_guitar, price, year):
        super().__init__(num_strings, type_guitar, price, year)
        self._brand = brand
        
    @property
    def brand(self):
        return self._brand

    def play_sound(self):
        return (f"{self.brand} : You cant play Stairway to Heaven here!")    
    
    def __str__(self):
        guitar_properties = super().__str__()
        return f"{guitar_properties}Brand: {self.brand}"   
    

les_paul_custom = Gibson('Gibson', 6, 'electric', 2699, 2024)
firebird_gold = Gibson('Gibson', 6, 'electric', 2699, 2024)
print(les_paul_custom.brand)
print(les_paul_custom.year)
print(les_paul_custom.play_sound())
print(les_paul_custom)
print(len(les_paul_custom))
print(les_paul_custom == firebird_gold)