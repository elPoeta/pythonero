import sys
import random
from utils import clear_screen
from hagman import Hagman
from color import Color
class Game:
    def __init__(self, words, limit_fails):
        self.words = words
        self.limit_fails = limit_fails
        
    def start(self):
       while(True):
            try: 
               clear_screen() 
               print(f'{Color.green}[1] - 🕹️\t New Game{Color.restore}\n')
               print(f'{Color.red}[2] - 🚪 Exit{Color.restore}\n')
               option = input(f'{Color.cyan}Option: ')
              # print('\x1b[1;0m')
               match option:
                  case '1':
                     self.new_game()
                     break
                  case '2':
                     print(f'\n{Color.yellow}👋 Goodbye!!!{Color.restore}\n')
                     break
                  case _:
                     continue
            except KeyboardInterrupt:  
                sys.exit(f'\n{Color.yellow}👋 Goodbye!!!{Color.restore}\n') 
    
    def new_game(self):
        clear_screen()
        word = random.choice(self.words)
        hagman = Hagman(word, self.limit_fails)
        hagman.play_game()