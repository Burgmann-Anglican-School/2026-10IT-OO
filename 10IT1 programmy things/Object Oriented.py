#Dog implementation with variables
dog_legs = 4
dog_breed = "caboodle"
dog_colour = "black"
dog_height = '27cm'
dog_age = 8
dog_name = 'Zoe'

#dog dictionary
zoe = {"legs":4, "breed": "caboodle", "colour":"black", "height":'27cm', 'age':8}
#Classes use PascalCase
#Variables use snake_case
#Constants use UPPER_CASE
#Variables are singular, data structures are plural
class Dog:

    #def defines a function. A function in a class is called a method.
    # __init__ is the initialise method, aka class constructor
    # the double underscore is a special python identifier called a 
        # dunder.
    #Most methods must have self as an argument
    def __init__(self, legs, colour, height, age, name):
        #We take the arguments as input to the function and connect them
        # to the class itself
        self.legs = legs
        self.colour = colour
        self.height = height
        self.age = age
        self.name = name

    #This funtion takes another dog object (other) and lets the first dog talk to the second
    # we use it like this: dog1.converse(dog2)
    def converse(self, other):
        print(f"{self.name} says 'Hi' to {other.name}")

    #This function lets a dog say the words you write into the function as an argument
    # we use it like dog1.speak("put cool words here")
    def speak(self, words):
        return f'{self.name} says {words}'

    #This is a dunder str, it overrides the print function    
    #When print is called on instances of this class, it runs
    # this function
    def __str__(self):
        return f"{self.name} is a dog that is {self.age} years old"

#These are child classes. Dog is the parent class
#They will do everything dog does, but they override the speak method
class GoldenRetriver(Dog):
    #GoldenRetrievers cannot speak like a dog, they just "bark"
    def speak(self):
        return "bark"

#This overrides nothing and is identical to Dog
class Caboodle(Dog):
    pass

class ToyPoodle(Dog):
    #This version of speak defaults to yap if no words are provided
    def speak(self, words='yap'):
        #super referes to the parent class
        return super().speak(words)
        
class Dachshund(Dog):
    def speak(self):
        return "sausage"
        
my_dog = GoldenRetriver(4, "blonde", '7ft', 13, "Clifford the dying dog")
my_dog2 = Caboodle(4, "orange", '2ft', 1, "Gerald the flying dog")
my_dog3 = ToyPoodle(4, "yellow", '1ft', 3, "Garry the frying dog")
my_dog4 = Dachshund(4, "green", '3ft', 5, "Emanuel the lying dog")

my_dog.converse(my_dog2)
print(my_dog)

print(my_dog.speak())
print(my_dog2.speak('words'))
print(my_dog3.speak())
print(my_dog4.speak())

#Car question/answer below
class Car:

    def __init__(self, colour, kilometerage, speed):
        self.colour = colour
        self.k = kilometerage
        self.speed = speed

    def __str__(self):
        return f"The {self.colour} car has {self.k} kilometres."

    def vroom(self):
        return self.speed

    def difference(self, other):
        return abs(self.k - other.k)

    def compare_speed(self, other):
        return abs(self.speed - other.speed)

class Toyota(Car):
    pass

class BMW(Car):
    def compare_speed(self, other):
        return "always faster"

blue_car = Toyota("blue", 20000, 100)
red_car = BMW("red", 30000, 120)

print(blue_car)
print(red_car)
print(blue_car.difference(red_car))
print(red_car.speed)
print(blue_car.compare_speed(red_car))
print(red_car.compare_speed(blue_car))