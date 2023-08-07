from classes import grasslands, dinosaur, carnivore, deep_forest, airport
from area_1 import area_1
from area_2 import area_2
from area_4 import area_4
from door_puzzle import door_puzzle
from hanger import hanger

def area_3():
    """
    Function that has the Ocean scene (Swim from the first area)
    """
    print("You jump into the murky water, the current is too strong and sweeps you downstream towards the ocean\n")
    print("As you finally hit calmer waters, you see a boat in the ocean\nYou can try to swim for the boat or you could try swimming back up the river\n")
    print("Options: upstream, ocean")

    choice = "incorrect"
    while choice == "incorrect":
        option = input("Your choice is: ").lower()
        print("------------------------------\n")

        if option == "upstream":
            print("The current is too strong you cannot go back that way\n")

        elif option == "ocean":
            print("You try to swim for the boat, a massive shadow is lurking under the water, as you approach the boat you get dragged under\n")
            mosasaur = carnivore('Mosasaurus','59','incredibly sharp saw like teeth','flipper like fins, smooth grey scales and a shark like tail')
            print(mosasaur.get_description())
            print("As you try to swim for the surface, the Mosasaur loops back around devouring you in one bite")
            restart_game()

            choice = "correct"
        else:
            print("Please choose a valid option")