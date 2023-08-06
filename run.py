from classes import grasslands, dinosaur, carnivore, deep_forest, airport


def start_up(player_name):
    """
    Function for the title screen of the text game
    """
    print("------------------------------")
    print(f"Welcome To Cretaceous Forest {player_name}\n")
    print("A Text Based Game To Survive In a Cretaceous Era Forest\n")
    print("------------------------------\n")
   
    print("You wake up and you do not know where you are, the last thing you remember seeing was an airfield on your way in and decide that will be your best way to escape\n")
    print(f"It is your job {player_name} to choose the options that will get you to safety.\n")
    print("------------------------------\n")
    from classes import forest
    dusk_forest = forest('evening sky', 'orange', 'an endless forest, unfamiliar foliage, and a murky river')
    print(dusk_forest.description())
    print("You try to make sense of where you are when you hear a deafening roar.\n")
    # First Scene
    print("You see a fork in the road, the paths to choose are left to the grassland or right into the deep forest, you could also try your luck swimming in the river,\nwhich path do you take?\n")
    print("Options: left, right, swim\n")

    choice = "incorrect"
    while choice == "incorrect":
        option = input("Your choice is: ").lower()
        print("------------------------------\n")
        if option == "left":
            area_1("left")
            choice = "correct"
        elif option == "right":
            area_2("right")
            choice = "correct"
        elif option == "swim":
            area_3("swim")
            choice = "correct"
        else:
            print("Please choose a valid option")


def area_1(directions):
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
            area_2("detour")
          
        elif option == "hide":
            print("You run towards the foliage to shelter yourself from the stampede,\nYou snag your leg on a branch, giving you a deep cut you are covered in blood you have 'Injured' status")
            print("You survive the encounter and proceed towards where the stampede came from\n")
         
            global injured
            injured = True
            choice = "correct"
            area_4("hide")
        else:
            print("Please choose a valid option")


def area_2(directions):
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
            area_4("climb")
            choice = "correct"
        else:
            print("Please choose a valid option")


def area_3(directions):
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


def door_puzzle():
    """
    Function for the door puzzle (keycode)
    """
    correct_sequence = [4, 7, 2, 9]
    sequence_input = []

    print("You get to the hanger and you notice a keypad with 9 numbers on it, a red light flickering to show power is still on.\n")
    print("Enter 0 to leave the puzzle.\n")

    def display_keypad():
        keypad_layout = [
            ["[" + str(num) + "]" if num in sequence_input else " " + str(num) + " " for num in range(1, 4)],
            ["[" + str(num) + "]" if num in sequence_input else " " + str(num) + " " for num in range(4, 7)],
            ["[" + str(num) + "]" if num in sequence_input else " " + str(num) + " " for num in range(7, 10)]
        ]
        for row in keypad_layout:
            print("".join(row))

    # Player's input
    while len(sequence_input) < 4:
        try:
            display_keypad()
            num = int(input("Enter a single number (1-9) or 0 to leave: "))
            if num == 0:
                print("You decided to leave the puzzle.")
                area_4("leave")
            elif 1 <= num <= 9:
                sequence_input.append(num)
            else:
                print("Invalid input. Please enter a number between 1 and 9 or 0 to leave.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Tests your input against the correct sequence
    if sequence_input == correct_sequence:
        print("The light changes from red to green, you hear a click... you try the door and it opens\n")
        hanger()
    else:
        print("That code didn't work... try again.")
        door_puzzle()


def hanger():
    """
    runs the hanger scene
    """
    print("You make it through the door inside the hanger, you spot the plane\n")


def main_functions():
    """
    Runs the main functions of the text-based game.
    """
    #Variable for name is here so when restart game is called it allows you to change your name if you wish.
    global player_name
    player_name = input('Please Enter Your Name To Start:')
    #Injured variable True or False is here
    global injured
    injured = False
    start_up(player_name) 


def restart_game():
    print("Do you want to play again?\n")
    choice = input("Enter 'yes' to restart, or any other key to quit: ")

    if choice.lower() == "yes":
        main_functions()
    else:
        print(f"Thank you for playing Creataceuous Forest {player_name}!")


main_functions()




       


