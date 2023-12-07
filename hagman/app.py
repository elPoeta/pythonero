import sys
import argparse
import random
from utils import clear_screen
from color import Color
from hagman import Hagman


def main():
    clear_screen()
    color = Color()
    words = get_words()
    start(words, color)


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


def pick_word(words):
    return random.choice(words)


def start(words, color):
    while True:
        try:
            clear_screen()
            print(f"{color.green}[1] - 🕹️\t New Game{color.restore}\n")
            print(f"{color.red}[2] - 🚪 Exit{color.restore}\n")
            option = input(f"{color.cyan}Option: ")
            match option:
                case "1":
                    new_game(words, color)
                    break
                case "2":
                    print(f"\n{color.yellow}👋 Goodbye!!!{color.restore}\n")
                    break
                case _:
                    continue
        except KeyboardInterrupt:
            sys.exit(f"\n{color.yellow}👋 Goodbye!!!{color.restore}\n")


def new_game(words, color):
    clear_screen()
    word = pick_word(words)
    hagman = Hagman(word, color)
    end = hagman.play_game()
    if end:
        start(words, color)


if __name__ == "__main__":
    main()
