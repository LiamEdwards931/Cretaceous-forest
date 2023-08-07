from classes import grasslands, dinosaur, carnivore, deep_forest, airport
from area_1 import area_1
from area_2 import area_2
from area_3 import area_3
from area_4 import area_4
from door_puzzle import door_puzzle

def hanger():
    """
    runs the hanger scene
    """
    print("You make it through the door inside the hanger.\n")
    print("The hanger is dim, with only a small light illuminating the area\n")
    print("You see the plane in front of you to escape the island, you plan your next move")
    print("Options: escape, investigate, open door")

    choice = "incorrect"
    while choice == "incorrect":
        option = input("Your choice is: ").lower()
        print("------------------------------\n")

        if option == "investigate":
            print("You search around the hanger looking for anything useful that you may need\n")
            print("You don't really find anything that can be useful")
            print("You take a deeper look around the hanger and notice on the wall there is a key hanging up\n")
            door_key = True
            print("You pick up the key")
        elif option == "open door":
            if (door_key):
                print("You put the key in the lock, it turns and you enter the room\n")
                print("As you scan the room you see a fuel can in the corner labelled plane fuel")
                has_fuel_can = True
                print("You pick up the fuel can\n")
            else:
                print("The door is locked..\n")
        elif option == "escape":
            if (has_fuel_can):
                print("You attempt to start the plane..\n")
                print("The engine starts..\n")
                print("You pull out onto the runway.. and take off at full speed")
                print(f"You have survived the island... for now well done! {player_name}")
                restart_game()
            else:
                print("You attempt to start the plane..\n")
                print("The engine stuggles to start..\n")
                print("The engine finally starts..")
                print("The engine cuts dead.. you notice that the fuel gauge is now empty..")
        else:
            print("Invalid choice. Please choose again.\n")