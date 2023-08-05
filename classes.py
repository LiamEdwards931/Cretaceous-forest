#Creates the environments
class forest:
    """
    describes the generic forest
    """
    def __init__(self, sky, color, foliage):
        # properties
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
        Describes the grasslands
        """
        return f"You make your way through the forest and finally reach the grasslands,\nThe {self.sky} exploded across the horizon,\nWhen you take a look around you see {self.area}"


#Creates the animals
class dinosaur:
    """
    Creates a dinosaur class
    """
    def __init__(self, species, length):
        self.species = species
        self.length = length

    def description(self):
        """
        Describes the dinosaur
        """
        return f"A {self.length} ft long {self.species} emerges."


class carnivore(dinosaur):
    """
    Creates the carnivore behavior class
    """
    def __init__(self, species, length, teeth, describe):
        super().__init__(species, length)
        self.describe = describe
        self.teeth = teeth

    def get_description(self):
        """
        Appends the super class, and adds a description
        """
        return f"{super().description()}\nThe most distinct feature you can make out is its {self.describe}\nAs you inspect the dinosaur, you see {self.teeth}"





