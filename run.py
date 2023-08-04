player_name = input('Please Enter Your Name:')


def start_up():
    """
    Function for the title screen of the text game
    """
    print("------------------------------")
    print(f"Welcome To Cretaceous Forest {player_name}\n")
    print("A Text Based Game To Survive In a Cretaceous Era Forest\n")
    print("------------------------------\n")
    intro()
    
   

def intro():
    """
    Runs the introduction to the text-game
    """
    print("You wake up and you do not know where you are, the last thing you remember is that the plane that is on the airfieldto escape is leaving soon.\n")
    print(f"It is your job {player_name} to choose the options that will get you to safety.\n")
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
            import area1
            choice = "correct"
        elif option == "right":
            print("option2")
            choice = "correct"
        elif option == "swim":
            print("option3")
            choice = "correct"
        else:
            print("Please choose a valid option")


def main_functions():
    """
    Runs the main functions of the text-based game.
    """
    start_up()  



def restart_game():
    while True:  
        print("You have died, would you like to restart? y/n")
        answer = input("Answer here: ").lower()
        if answer == 'y':
            main_functions()  
        elif answer == 'n':
            print("Thanks for playing! Goodbye.")
            break  
        else:
            print("Invalid input. Please enter 'y' to restart or 'n' to quit.")
   

main_functions()

