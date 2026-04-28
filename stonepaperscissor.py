import random

def play_stonepaperscissor():
    options = ["stone", "paper", "scissors"]

    user = input("Enter stone / paper / scissors: ").strip().lower()
    
    if user not in options:
        print("Invalid choice!")
        return

    me = random.choice(options)

    print(f"me chose: {me}")

    if user == me:
        print("It's a Draw!")

    elif (user == "stone" and me == "scissors") or (user == "paper" and me == "stone") or (user == "scissors" and me == "paper"):
        print("You Win!")

    else:
        print("I Win!")