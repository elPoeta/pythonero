import sys
import random
from utils import clear_screen
from hagman import Hagman
from color import Color
class Game:
    def __init__(self, words, limit_fails):
        self.words = words
        self.limit_fails = limit_fails
        self.color = Color()
        
    def start(self):
       while(True):
            try: 
               clear_screen() 
               print(f'{self.color.green}[1] - 🕹️\t New Game{self.color.restore}\n')
               print(f'{self.color.red}[2] - 🚪 Exit{self.color.restore}\n')
               option = input(f'{self.color.cyan}Option: ')
               match option:
                  case '1':
                     self.new_game()
                     break
                  case '2':
                     print(f'\n{self.color.yellow}👋 Goodbye!!!{self.color.restore}\n')
                     break
                  case _:
                     continue
            except KeyboardInterrupt:  
                sys.exit(f'\n{self.color.yellow}👋 Goodbye!!!{self.color.restore}\n') 
    
    def new_game(self):
        clear_screen()
        word = random.choice(self.words)
        hagman = Hagman(word, self.limit_fails, self.color)
        end = hagman.play_game()
        if end:
           self.start()