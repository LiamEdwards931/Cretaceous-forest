from classes import grasslands, dinosaur, carnivore, deep_forest, airport
from area_2 import area_2
from area_3 import area_3
from area_4 import area_4
from door_puzzle import door_puzzle
from hanger import hanger

def area_1():
    """
    Function that has the grasslands scene (Go left from the first area)
    """
    grass_land = grasslands('evening sky', 'the forest you just came from, the deeper forest to the right and fallen foliage in the middle of the plains')
    print(grass_land.description())
    print("The roar from behind you is getting louder, and thundering footsteps from a stampeding herd of herbivores are booming from the plains in front of you\n")
    print("As you evaluate your options you see 3 choices\n")
    print("Options: back, detour, hide\n")

    choice = "incorrect"
    while choice == "incorrect":
        option = input("Your choice is: ").lower()
        print("------------------------------\n")

        if option == "back":
            print("You decide to go back from where you came to avoid the herd\n")
            Allosaurus = carnivore('Allosaurus', '27', 'rows of sharp teeth serrated at the edges', 'blunt horn just in front of and above the eyes')
            print(Allosaurus.get_description())
            print("As you try to evade the massive carnivore, it chases and devours you in its powerful jaws\n")
            choice = "correct"
            restart_game() 

        elif option == "detour":
            print("You decide to avoid the herd by running around them, as you get around")
            rex = carnivore('T-rex','41','serrated blade like teeth, a massive head with powerful jaws','tiny arms in comparison to its massive body')
            print(rex.get_description())
            print("You manage to evade the T-rex as it was distracted by a straggling dinosaur from the herd, and you head towards the Deep Forest\n")
            choice = "correct"
            area_2()
          
        elif option == "hide":
            print("You run towards the foliage to shelter yourself from the stampede,\nYou snag your leg on a branch, giving you a deep cut you are covered in blood you have 'Injured' status")
            print("You survive the encounter and proceed towards where the stampede came from\n")
         
            global injured
            injured = True
            choice = "correct"
            area_4()
        else:
            print("Please choose a valid option")