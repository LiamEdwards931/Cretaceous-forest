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
    print("You wake up and you do not know where you are, the last thing you remember, is that the plane to escape is leaving soon.\n")
    print(f"It is your job to choose the options that will get you to safety.\n")
    from classes import dusk_forest
    print("You try to make sense of where you are, when you hear a deafening roar.\n")
    #First Scene
    print("You see a fork in the road, the paths to choose are left or right, you could also try your luck swimming in the river, which path do you take?")
    print("Options: left, right, swim")
    print("Your choice is: ")
    option = input()
    choice = "incorrect"
    while(choice == "incorrect"):
        if(option.lower() == "left"):
            print("option1")
            choice = "correct"
        elif(option.lower()=="right"):
            print("option2")
            choice = "correct"
        elif(option.lower()=="swim"):
            print("option3")
            choice = "correct"
        else:
            print("Please choose a valid option")
            option = input()
   

def main_functions():
    """
    Runs the main functions of the text based game.
    """
    start_up()
    intro()
    


def gameover():
    while True:
        if dead == True:
            print("You have died game-over")
        else:
            main_functions()


main_functions()