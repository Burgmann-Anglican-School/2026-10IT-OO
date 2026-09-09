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
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    #This is a new method that lets the dog say something
    def speak(self, words):
        return f"{self.name} says {words}"

    #This is a new method that takes 2 dogs, one as self, the other as other_dog
    def converse(self, other_dog):
        return f"{self.name} says hi to {other_dog.name}"

    #This is the dunder str, it overrides the print function
    def __str__(self):
        return f"{self.name} is a {self.age} year old {self.breed}"

my_dog = Dog('Markus', 20, 'labradoodle')
dog2 = Dog('Markuce', 47, 'pug')

print(my_dog.name)
print(my_dog.age)
print(my_dog.breed)
print(my_dog)
print(my_dog.speak('Hello'))
print(my_dog.converse(dog2))