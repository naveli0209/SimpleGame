import random

def play_diceroll():
    input("Press Enter to roll the dice...")

    user_roll = random.randint(1, 6)
    i_roll = random.randint(1, 6)

    print(f"You rolled: {user_roll}")
    print(f"I rolled: {i_roll}")

    if user_roll > i_roll:
        print("You Win!")

    elif user_roll < i_roll:
        print("I Wins!")

    else:
        print("It's a Draw!")