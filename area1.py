def area_1(direction):
    from classes import grasslands
    grass_land = grasslands('evening sky', 'the forest you just came from, the deeper forest to the right and fallen foliage in the middle of the plains')
    print(grass_land.description())
    print("The roar from behind you is getting louder, and thundering footsteps from a stampeding herd of herbivores are booming from the plains in front of you\n")
    print("As you evaluate your options you see 3 choices\n")
    print("Options: back, forest, hide\n")
    
    choice = "incorrect"
    while choice == "incorrect":
        option = input("Your choice is: ").lower()
        print("------------------------------\n")

        if option == "back":
            print("You decide to go back from where you came to avoid the herd")
            from classes import dinosaur
            allosaur = dinosaur('Allosaurus', '28', 'carnivore')
            print(allosaur.description())
            print('As you try to evade the massive carnivore, it chases and catches you in its powerful jaws')
            dead = True
            choice = "correct"
        elif option == "forest":
            print("option2")
            choice = "correct"
        elif option == "hide":
            print("option3")
            choice = "correct"
        else:
            print("Please choose a valid option")

area_1("left")