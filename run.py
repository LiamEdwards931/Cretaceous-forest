injured = False
dead = False


def start_up():
    """
    Function for the title screen of the text game
    """
    print("------------------------------")
    player_name = input('Please Enter Your Name:')
    print(f"Welcome To Cretaceous Forest {player_name}\n")
    print("A Text Based Game To Survive In a Cretaceous Era Forest\n")
    print("------------------------------\n")
    intro()
    

def intro():
    """
    Runs the introduction to the text-game
    """
    print("You wake up and you do not know where you are, the last thing you remember is that the plane to escape is leaving soon.\n")
    print("It is your job to choose the options that will get you to safety.\n")
    print("------------------------------\n")
    from classes import forest
    dusk_forest = forest('evening sky', 'orange', 'an endless forest, unfamiliar foliage, and a murky river')
    print(dusk_forest.description())
    print("You try to make sense of where you are when you hear a deafening roar.\n")
    # First Scene
    print("You see a fork in the road, the paths to choose are left to the grassland or right into the deep forest, you could also try your luck swimming in the river, which path do you take?")
    print("Options: left, right, swim")
    
    choice = "incorrect"
    while choice == "incorrect":
        option = input("Your choice is: ").lower()
        print("------------------------------\n")

        if option == "left":
            area_1("left")
            choice = "correct"
        elif option == "right":
            print("option2")
            choice = "correct"
        elif option == "swim":
            print("option3")
            choice = "correct"
        else:
            print("Please choose a valid option")


def area_1(input):
    from classes import grasslands
    grass_land = grasslands('evening sky', 'the forest you just came from, the deeper forest to the right and fallen foliage in the middle of the plains')
    print(grass_land.description())
    print("The roar from behind you is getting louder, and thundering footsteps from a stampeding herd of herbivores are booming from the plains in front of you\n")
    print("As you evalauate your options you see 3 choices\n")
    print("Options: back, forest, hide\n")
    choice = "incorrect"
    while choice == "incorrect":
        option = input("Your choice is: ").lower()
        print("------------------------------\n")

        if option == "back":
            area_1("left")
            choice = "correct"
        elif option == "forest":
            print("option2")
            choice = "correct"
        elif option == "hide":
            print("option3")
            choice = "correct"
        else:
            print("Please choose a valid option")
    

def main_functions():
    """
    Runs the main functions of the text based game.
    """
    start_up()

main_functions()
