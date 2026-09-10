class Pack:

    def __init__(self, size, contents = []):
        self.size = size
        self.contents = contents

    def addItem(self, item):
        pass

    def dropItem(self, item):
        pass

    def packCapacity(self):
        pass

class Item:

    def __init__(self, size):
        self.size = size

    def getSize(self):
        pass

class Potion(Item):

    def __init__(self, potency, size):
        super().__init__(size)
        self.potency = potency

    def use(self):
        pass

class Weapon(Item):

    def __init__(self, power, _range, size):
        super().__init__(size)
        self.power = power
        self.range = _range

    def getPower(self):
        pass

    def getRange(self):
        pass

class Axe(Weapon):

    def __init__(self, name, power, _range, size):
        super().__init__(power, _range, size)
        self.name = name
    
    def chop(self):
        pass

    def swing(self):
        pass

my_axe = Axe('bob', 7, 3, 3)