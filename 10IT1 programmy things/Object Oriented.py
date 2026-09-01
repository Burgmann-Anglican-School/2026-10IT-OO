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
    def __init__(self, legs, breed, colour, height, age, name):
        #We take the arguments as input to the function and connect them
        # to the class itself
        self.legs = legs
        self.breed = breed
        self.colour = colour
        self.height = height
        self.age = age
        self.name = name

    def converse(self, other):
        print(f"{self.name} says 'Hi' to {other.name}")

    def __str__(self):
        return f"{self.name} is a {self.breed} that is {self.age} years old"

my_dog = Dog(4, "Golden Retriever", "blonde", '7ft', 13, "Clifford the dying dog")
my_dog2 = Dog(4, "Caboodle", "orange", '2ft', 1, "Gerald the flying dog")
my_dog3 = Dog(4, "Toy poodle", "yellow", '1ft', 3, "Garry the frying dog")
my_dog4 = Dog(4, "Daschund", "green", '3ft', 5, "Emanuel the lying dog")

my_dog.converse(my_dog2)
print(my_dog)
