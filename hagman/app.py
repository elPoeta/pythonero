import sys
from utils import clear_screen, get_args
from game import Game

def main():
    clear_screen()
    words = get_words()
    game = Game(words)
       
    
def get_words():
    args = get_args();
    file_name = args.f
    try:
        words = []
        with open(file_name) as file:
            for line in file:
                words.append(line.strip())
        return words        
    except FileNotFoundError:  
        sys.exit(f"File {file_name} does not exist") 
        
if __name__ == '__main__':
    main()   