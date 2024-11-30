# Class - blueprint for creating objects
# Camel case - eg helloFelicis

class Car: # Pascal Case eg. FelicisWasHere
    # Constructor - optional special method that sets up the attributes of a new instance
    # will be called automatically when a new instance is created
    def __init__(self, make, model, engine): # self is passed implicitly by the interpreter
        #print("Hello Felicis called __init__")
        #print(self)
        # implicitly returns self
        # create an attribute 'make' and copy value of the make param into it
        
        #dunder makes attr private

        self.__make = make # dot notation - <object>.<attr/method>
        self.model = model
        self.engine = engine

    def start(self):
        print(f'{self.__make} {self.model} started!')

    def __str__(self): # returns a string
        return f'This is a {self.__make} {self.model}'
    
    # function overloading - not supported in python
    
    # Getter

    def get_make(self):
        # Authorize
        # if condition
        return self.__make
        # side effects

    # Setter

    def set_make(self, new_make):
        # Validate new_make
        # Authorize
        self.__make = new_make

#inheritence - "is a realationship car a petrolcar is a car"
class PetrolCar(Car):
    def __init__(self, make, model, tank_capacity_l, engine):
        # self.__make = make # dot notation - <object>.<attr/method>
        # self.model = model
        super().__init__(make, model, engine)
        self.tank_capacity_l = tank_capacity_l
    def __str__(self):
        return f'{super().__str__()}. It has a {self.tank_capacity_l}l tank.'


# Composistion - "has a realtionship a car has a engine"

class Engine:
    def __init__(self, type, max_power_kw):
        self.type = type
        self.max_power_kw = max_power_kw

    def __str__(self):
        return f'This is a {self.type} engine with a maximum power of {self.max_power_kw}'

# Main

engine1 = Engine(type='petrol', max_power_kw=235)


my_car = PetrolCar(make='Honda', model='Civi', tank_capacity_l= 47, engine=engine1) # create a new instance of the class car
#your_car = Car("Toyota", "Felicis")
# my car is now an object of type class

#print(my_car.__dict__)

#my_car.start()
#
#your_car = Car()
#print(your_car)

#your_car.start()
print(my_car.engine)
#your_car.model = 'Prius'
#print(your_car)
#print(my_car.get_make())

