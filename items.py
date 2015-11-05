class Item():
    """Item base class"""
    def __init__(self, name, description, floordescription=None):
        self.name = name
        self.description = description
        
        if floordescription == None:
            self.floordescription = self.description
        else:
            self.floordescription = floordescription
        
    def __str__(self):
        return "A {0}".format(self.name)

class Weapon(Item):
    def __init__(self, name, description, floordescription, damage):
        super().__init__(name = name,
                         description = description,
                         floordescription = floordescription)
        self.damage = damage


class LightSource(Item):
    def __init__(self, name, description, floordescription, life):
        super().__init__(name = name,
                         description = description,
                         floordescription = floordescription)
        self.life = life

class Structure(Item):
    def __init__(self, name, floordescription):
        super().__init__(name = name,
                         description = "You should never see this!",
                         floordescription = floordescription)
    

#|----------------|
#| End class defs |
#|----------------|
