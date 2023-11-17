import os
import argparse

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')
   
def get_args():
    parser = argparse.ArgumentParser(description="*** Hagman ***")
    parser.add_argument("-f", default="words.txt", help="file of words", type=str)
    parser.add_argument("-l", default=5, help="fail limit", type=int)
    return parser.parse_args()                                