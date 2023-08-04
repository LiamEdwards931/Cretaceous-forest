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


class grasslands:
    """
    describes the grassland area
    """
    def __init__(self, sky, area):
        self.sky = sky
        self.area = area
        
    def description(self):
        """
        descrives the grasslands
        """
        return f"You make your way through the forest and finally reach the grasslands,\nThe {self.sky} exploded across the horizon,\nWhen you take a look around you see {self.area}"



