from classes import grasslands, dinosaur, carnivore, deep_forest, airport
from area_1 import area_1
from area_3 import area_3
from area_4 import area_4
from door_puzzle import door_puzzle
from hanger import hanger

def area_2():
    """
    Function that has the deep forest scene (Go right from the first area, detour from the second area)
    """
    print("You find yourself in the Deep Forest\n")
    dense_forest = deep_forest('30','forest is so dense','rustling in the bushes')
    print(dense_forest.get_description())
    print("Concerned by the rustling in the bushes and the roars you heard earlier, you know you need to move forwards\n")
    print("There are two paths you can take: sprint through the forest, climb through the trees")
    print("Options: run, climb")

    choice = "incorrect"
    while choice == "incorrect":
        option = input("Your choice is: ").lower()
        print("------------------------------\n")

        if option == "run":
            print("You try to sprint through the forest, as you do..")
            velociraptor = carnivore('Velociraptor','5','small blade teeth', 'sharp curved claw, capable of slicing through thick hides')
            print(velociraptor.get_description())
            print("The velociraptor disappears from sight, just as you breath a sigh of relief..")
            print("You get ambushed by a second one in the pack from the nearby bushes\n you are eaten alive by the raptor pack..")
            restart_game()
            choice = "correct"
        elif option == "climb":
            print("You decide to not take any chances with the rustling in the bushes\nYou climb to a safe level in the trees and start to procede forwards")
            print("you see a clearing in the trees, and see the airport.. you climb down\n")
            area_4()
            choice = "correct"
        else:
            print("Please choose a valid option")