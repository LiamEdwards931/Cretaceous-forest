from classes import grasslands, dinosaur, carnivore, deep_forest



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
            print("You run towards the foliage to shelter yourself from the stampede, You survive the encounter and proceed towards where the stampede came from\n")
            choice = "correct"
            #airfield()
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
            velociraptor = carnivore('Velociraptor','5','small blade teeth','sharp curved claw, capable of slicing through thick hides')
            print(velociraptor.get_description())
            print("The velociraptor disappears from sight, just as you breath a sigh of relief..")
            print("You get ambushed by a second one in the pack from the nearby bushes\n you are eaten alive by the raptor pack..")
            restart_game()
            choice = "correct"
        elif option == "climb":
            print("option 2")
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




       


