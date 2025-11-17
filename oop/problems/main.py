# fill in the line class methos to accept coordinates as a piar of tuples and return th slope and distance of the line
import math

class Line:
    def __init__(self, coor1,coor2):
        self._coors = (coor1, coor2)

    def distance(self):
        print(f" first coords : {self._coors[0]}")
        print(f" second coords : {self._coors[1]}")
        print(f"1st coords x : {self._coors[0]['x']}")
        return math.sqrt(((self._coors[0]['x'] - self._coors[1]['x'] ) ** 2) + ((self._coors[1]['y'] - self._coors[0]['y']) ** 2))

    def slope(self):
        return ((self._coors[1]['y'] - self._coors[0]['y']) / (self._coors[0]['x'] - self._coors[1]['x']))


cooordinates_1 = ({"x": 3 , "y": 2}, {"x": 8, "y": 10})    
li = Line(cooordinates_1[0], cooordinates_1[1])
print(li.distance())
print(li.slope())


# fill in the class
class Cylinder:
    def __init__(self, height = 1, radius = 1):
        self._height = height
        self._radius = radius

    def volume(self):
        # V = pi r ^ 2 h
        return math.pi * (self._radius ** 2) * self._height
    def surface_area(self):    
        # A = 2 pie r h + 2 pi r ^2
        return (2 * math.pi * self._radius * self._height)  +  ( 2 * math.pi * (self._radius ** 2))
    
cy = Cylinder(10, 3)
print(cy.volume())    
print(cy.surface_area())


# Create a bank accoutn class that has 2 attributes
# owner and balance

# and two methods
# deposit and withdraw

# usual ssafety checks such as withdrawals cannot exceeet the available balance

class BankAccount():
    def __init__(self,account_name, initial_balance = 0):
        self._account_name = account_name
        self._balance = float(initial_balance)

    @property
    def account_name(self):
        return self._account_name

    @property
    def balance(self):
        return self._balance    

    def withdraw(self, amount):
        amount = float(amount)
        if amount > self._balance:
            print( f"Cannot withdraw, balance insufficient")
        else:
            self._balance -= amount
            print(f"Successfully withdrawn {amount}")
        
    def deposit(self, amount):
        amount = float(amount)
        self._balance += amount
        print(f'Successfully deposited {amount}')      

    def request_to_delete_account(self):
        print(f'You have requested to close your account, we should reply within 1-2 business days')


account_john_doe = BankAccount("John Doe", 2465)

print(account_john_doe.balance)
account_john_doe.deposit(300)
account_john_doe.withdraw(1100)
print(account_john_doe.balance)
account_john_doe.withdraw(4100)
print(account_john_doe.balance)