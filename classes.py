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


class deep_forest:
    """
    class for the deep forest
    """
    def __init__(self, height, density, sound):
        self.height = height
        self.density = density
        self.sound = sound

    def get_description(self):
        """
        Appends the super class, and adds a description
        """
        return f"You evaluate your surroundings, becuase the {self.density} it was hard to get a good view of in front of you\nAs you look up you see {self.height} meter high trees\nThe ambience was quiet and eerie. Until you hear {self.sound}"


class airport:
    """
    class for the airport
    """
    def __init__(self, surroundings):
        self.surroundings = surroundings
   
    def description(self):
        """
        describes the airport
        """
        return f"You see {self.surroundings}, You see a hanger across the beaten path and decide to make your way over to it."

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





