

def start_up():
    """
    Function for the title screen of the text game
    """
    print("------------------------------")
    player_name = input('Please Enter Your Name:')
    print(f"Welcome To Cretaceous Forest {player_name}\n")
    print("A Text Based Game To Survive In a Cretaceous Era Forest")
    print("To Restart The Game Just Type Restart")
    print("------------------------------")
    input("Press Any Key To Start The Game")
    

def main_functions():
    """
    Runs the main functions of the text based game. 
    """
    start_up()

main_functions()
restart()

import classes