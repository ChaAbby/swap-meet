
from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, category = "", condition = 0):
        self.category = "Electronics"
        self.condition = condition

    def __str__(self):
        ''' 
        reassigns the stringified item
        '''
        return "A gadget full of buttons and secrets."