class forest:
    """
    describes the generic forest
    """
    def __init__(self,sky,color, foliage):
      #properties
       self.sky = sky
       self.color = color
       self.foliage = foliage 
    
    def description(self):
        """
        Describes the forest
        """
        return f"As you take a look around you see {self.foliage}, the {self.sky} was barely shimmering through the towering {self.color} trees."


dusk_forest = forest('evening sky', 'orange', 'an endless forest, unfamiliar foliage, and a murky river')
print(dusk_forest.description())

