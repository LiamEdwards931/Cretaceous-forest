from classes import grasslands, dinosaur, carnivore, deep_forest, airport
from area_1 import area_1
from area_2 import area_2
from area_3 import area_3
from area_4 import area_4
from hanger import hanger

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
                area_4()
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