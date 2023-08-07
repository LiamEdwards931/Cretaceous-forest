from classes import grasslands, dinosaur, carnivore, deep_forest, airport
from area_1 import area_1
from area_2 import area_2
from area_3 import area_3
from door_puzzle import door_puzzle
from hanger import hanger

def area_4(direction):
    """
    function that has the airport scene
    """
    print("You arrive at the airport\n")
    airfield = airport('a guard tower on the outskirt and a path with cover from overgrown bushes')
    print(airfield.description())
    print("After surveying the area and considering the options you think you can sneak through the bushes to the hanger\nTake the longer route through the outskirts of the path, or make a run for it\n")
    print("options: outskirt, run, sneak\n")
    choice = "incorrect"
    while choice == "incorrect":
        option = input("Your choice is: ").lower()
        print("------------------------------\n")

        if option == "outskirt":
            if (injured):
                print("You make your way around the outskirts, The Velociraptor pack from the deep forest smell your blood from your injury")
                print("You get ambushed, and eaten alive")
                restart_game()
            else:
                print("You make your way around the outskirts and spot a guard tower, inside the tower there is a note with a code [4,7,2,9]\n")
                print("you continue on your path the hanger entrance")
                door_puzzle()
            choice = "correct"
        elif option == "run":
            print("You run for the door but the T-rex from earlier comes out of nowhere, chasing you down and devouring you\n")
            restart_game()
            choice = "correct"
        elif option == "sneak":
            print("You decide to sneak the long way around the airport and you arrive at the hanger door\n")
            door_puzzle()
            choice = "correct"
        else:
            print("Invalid choice. Please choose again.\n")