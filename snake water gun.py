#Snake drinks water
#Gun shoots the snake
#Gun drowns in the water

import random

def restart():
    ch = int(input("\nDo you want to continue? \nPress 1 for Yes: \nPress 2 for No: \n"))
    if ch == 1:
        print("\n<<<< Welcome again! >>>>\n")
        con()
    else:
        print("\nSee you next time!")

def con():
    i = 0
    your_points = 0
    computer_points = 0
    draw = 0
    while (i<= 2):
        lst = ["s", "w", "g"]
        choice = random.choice(lst)
        your_choice = str(input("Press s, w or g: "))
        if your_choice == "s" or your_choice == "g" or your_choice == "w":
            n = i + 1
            i = i + 1
            print("************* ROUND #", n, " *************")
            if choice == "s":
                if your_choice == "s":
                    print("Draw.\n")
                    draw = draw + 1
                elif your_choice == "w":
                    print("Oops! Computer got a point.\n")
                    computer_points = computer_points + 1
                elif your_choice == "g":
                    print("Woo-hoo! You got a point.\n")
                    your_points = your_points + 1
            elif choice == "w":
                if your_choice == "s":
                    print("Woo-hoo! You got a point.\n")
                    your_points = your_points + 1
                elif your_choice == "w":
                    print("Draw.\n")
                    draw = draw + 1
                elif your_choice == "g":
                    print("Oops! Computer got a point.\n")
                    computer_points = computer_points + 1
            elif choice == "g":
                if your_choice == "s":
                    print("Oops! Computer got a point.\n")
                    computer_points = computer_points + 1
                elif your_choice == "w":
                    print("Woo-hoo! You got a point.\n")
                    your_points = your_points + 1
                elif your_choice == "g":
                    print("Draw.\n")
                    draw = draw + 1
        else:
            print("\nEnter correct alphabet.\n")
    print("Your points:", your_points, "Computer's points:", computer_points, "Draw:", draw)
    if your_points > computer_points:
        print("Congratulations! You won")
    elif your_points < computer_points:
        print("You lost!")
    else:
        print("It's a draw.")
    restart()


print("\n<<<< Welcome to 'Snake', 'Water', 'Gun' game! >>>>\nYou have three rounds.\n")
con()