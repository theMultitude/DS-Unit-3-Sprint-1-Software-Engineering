class Product(object):
    """
    A Python Class from which Acme Co. can build specific product instances
    """
    import random
    ri = random.randint(1000000, 9999999)
    def __init__(self, name, price=10, weight=20, flammability=0.5, identifier=ri):
        self.name=name
        self.price=price
        self.weight=weight
        self.flammability=flammability
        self.identifier=identifier

    def stealability(self):
        x = (self.price)/(self.weight)
        strA = ["Not so stealable...", "Kinda stealable.", "Very stealable!"]
        if(x < 0.5):
            return strA[0]
        elif(0.5 <= x and x < 1.0):
            return strA[1]
        else:
            return strA[2]

    def explode(self):
        y = (self.flammability)*(self.weight)
        strA = ["...fizzle", "...boom!", "...BABOOM!"]
        if(y < 10):
            return strA[0]
        elif(10 <= y and y < 50):
            return strA[1]
        else:
            return strA[2]

class BoxingGlove(Product):
    import random
    ri = random.randint(1000000, 9999999)
    def __init__(self, name, price=10, weight=10, flammability=0.5, identifier=ri):
        self.name=name
        self.price=price
        self.weight=weight
        self.flammability=flammability
        self.identifier=identifier

    def explode(self):
        str = '...it\'s a glove.'
        return str

    def punch(self):
        str = 'Hey that hurt!'
        return str
