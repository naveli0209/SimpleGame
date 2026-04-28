from stonepaperscissor import play_stonepaperscissor
from diceroll import play_diceroll

def game():
    while True:
        print("\n===== GAME MENU =====")
        print("1. Stone-Paper-Scissors")
        print("2. Dice Roll Game")
        print("3. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1: play_stonepaperscissor()
        elif choice == 2: play_diceroll()
        elif choice == 3:
            print("Thanks for playing")
            break
        else:
            print("Invalid choice!")
game()