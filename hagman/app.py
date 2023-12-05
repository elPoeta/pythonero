import sys
import argparse
import random
from utils import clear_screen
from game import Game

words = []


def main():
    global pick_word
    global words
    clear_screen()
    words = get_words()
    game = Game(pick_word)
    game.start()


def get_args():
    parser = argparse.ArgumentParser(description="*** Hagman ***")
    parser.add_argument("-f", default="words.txt", help="file of words", type=str)
    return parser.parse_args()


def get_words():
    args = get_args()
    file_name = args.f
    try:
        words = []
        with open(file_name) as file:
            for line in file:
                words.append(line.strip())
        return words
    except FileNotFoundError:
        sys.exit(f"File {file_name} does not exist")


def pick_word():
    global words
    return random.choice(words)


if __name__ == "__main__":
    main()
