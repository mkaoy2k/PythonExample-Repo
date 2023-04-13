"""用隨機亂數產生器來設計一個擲骰子遊戲"""
import random
from PIL import Image


def roll_dice():

    dice_drawing = {
        1: (
            "-----",
            "|   |",
            "| o |",
            "|   |",
            "-----",
        ),
        2: (
            "-----",
            "|o  |",
            "|   |",
            "|  o|",
            "-----",
        ),
        3: (
            "-----",
            "|o  |",
            "| o |",
            "|  o|",
            "-----",
        ),
        4: (
            "-----",
            "|o o|",
            "|   |",
            "|o o|",
            "-----",
        ),
        5: (
            "-----",
            "|o o|",
            "| o |",
            "|o o|",
            "-----",
        ),
        6: (
            "-----",
            "|o o|",
            "|o o|",
            "|o o|",
            "-----",
        ),

    }
    roll = input("Roll the dice? (Yes/No) : ")
    if roll == "":
        # default is yes when just hitting 'enter'
        roll = "yes"

    while roll.lower() == "yes":
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        print(f"===>Dice rolled: {dice1} and {dice2}\n")
        print("\n".join(dice_drawing[dice1]))
        print("\n".join(dice_drawing[dice2]))

        roll = input("Roll again? (Yes/no): ")


# Game Example: rolling two dices
if __name__ == '__main__':

    roll_dice()
