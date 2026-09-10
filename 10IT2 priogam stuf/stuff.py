#dog implementation with variables
dog_legs = 4
dog_colour = "brown"
dog_name = 'Bazza'
dog_breed = 'Husky'
dog_other_appendages = 2
#Dog implementation with dictionaries
bazza = {'legs': 4, 'colour': 'brown', 'breed':'husky'}

#creating a class
class Dog:

    #this is the dunder init, iot initialises the class
    #the first argument will always be self,  this lets the class
    # refer to itself
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #This is a new method that lets the dog say something
    def speak(self, words):
        return f"{self.name} says {words}"

    #This is a new method that takes 2 dogs, one as self, the other as other_dog
    def converse(self, other_dog):
        return f"{self.name} says hi to {other_dog.name}"

    #This is the dunder str, it overrides the print function
    def __str__(self):
        return f"{self.name} is a {self.age} year old"

class Labradoodle(Dog):
    def speak(self):
        return 'hello'

class Pug(Dog):
    def converse(self, other, words='stuff'):
        return f'{self.name} says {words} to {other.name}'

my_dog = Labradoodle('Markus', 20)
dog2 = Pug('Markuce', 47)

print(my_dog.speak())
print(dog2.speak('Hello'))
print(my_dog.converse(dog2))
print(dog2.converse(my_dog))



class Car:

    def __init__(self, colour, kilometerage):
        self.colour = colour
        self.kilometerage = kilometerage

    def __str__(self):
        return f'The {self.colour} car has {self.kilometerage} kilometres.'
    
    def difference(self, other_car):
        return abs(self.kilometerage - other_car.kilometerage)


blue_car = Car('blue', 20000)
red_car = Car('red', 30000)

print(blue_car)
print(red_car)
print(blue_car.difference(red_car))

