import sys
import argparse

if __name__ == "__main__":
    argument_parser = argparse.ArgumentParser(description="Prints the minimum number of coins to make change for an amount of money")
    argument_parser.add_argument("cents", metavar="cents", type=int, help="Enter the cents")
    args = argument_parser.parse_args()

    cents = args.cents if args.cents else 0

    coins = 0
    while cents > 0:
        if cents >= 25:
            cents -= 25
        elif cents >= 10:
            cents -= 10
        elif cents >= 5:
            cents -= 5
        elif cents >= 2:
            cents -= 2
        else:
            cents -= 1
        coins += 1
    print(coins)

