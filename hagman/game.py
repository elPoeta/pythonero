import sys
import random
from utils import clear_screen
from hagman import Hagman
class Game:
    def __init__(self, words, limit_fails):
        self.words = words
        self.limit_fails = limit_fails
        
    def start(self):
       while(True):
            try: 
               clear_screen() 
               print('[1] - 🕹️\t New Game\n')
               print('[2] - 🚪 Exit\n')
               option = input('Option: ')
               match option:
                  case '1':
                     self.new_game()
                     break
                  case '2':
                     print('\n👋 Goodbye!!!\n')
                     break
                  case _:
                     continue
            except KeyboardInterrupt:  
                sys.exit('\n👋 Goodbye!!!\n') 
    
    def new_game(self):
        clear_screen()
        word = random.choice(self.words)
        hagman = Hagman(word, self.limit_fails)
        hagman.play_game()