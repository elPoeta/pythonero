import time
import re
from utils import clear_screen
from color import Color
class Hagman:
    def __init__(self, word="hello", limit_fail=5):
        self.word = list(' '.join(s for s in list(word.upper())))    
        self.fails = 0
        self.display = "_ " * len(word)
        self.limit_fail = limit_fail
        self.letters = []
        self.ascii_pics = self.set_ascii_pics()
        self.win = False

    def set_ascii_pics(self):
        first_common_pics = f"   {Color.restore}_____      {Color.green}🧩 Py-Hagman 🧩 {Color.restore} \n  |     |  \n  |     |     ❌ {Color.red}%%fails%% {Color.restore}  📝 %%letters%%  \n  |     "
        last_common_pic = f"__|__        {Color.cyan}%%display%% {Color.restore}\n"
        return [
             f"{first_common_pics}\n  |        \n  |        \n  |        \n{last_common_pic}",
             f"{first_common_pics}{Color.red}|{Color.restore}  \n  |        \n  |        \n  |        \n{last_common_pic}",
             f"{first_common_pics}{Color.red}|{Color.restore}  \n  |     {Color.red}O{Color.restore}  \n  |        \n  |        \n{last_common_pic}",
             f"{first_common_pics}{Color.red}|{Color.restore}  \n  |     {Color.red}O{Color.restore}  \n  |     {Color.red}|{Color.restore}  \n  |        \n{last_common_pic}",
             f"{first_common_pics}{Color.red}|{Color.restore}  \n  |     {Color.red}O{Color.restore}  \n  |    {Color.red}/|\ {Color.restore} \n  |        \n{last_common_pic}",
             f"{first_common_pics}{Color.red}|{Color.restore}  \n  |     {Color.red}O{Color.restore}  \n  |    {Color.red}/|\ {Color.restore} \n  |    {Color.red}/ \ {Color.restore}\n{last_common_pic}",
        ]
        
    def print_pics(self, pos=0):
        clear_screen()
        print(self.ascii_pics[pos]
              .replace('%%display%%', self.display)
              .replace('%%fails%%', str(self.fails))
              .replace('%%letters%%', str(self.letters)))    
    
    def play_game(self):
        while self.fails < self.limit_fail:
            try:
                self.print_pics(self.fails)
                guess = input(f'💬 {Color.yellow}Enter your guess: ').strip().upper()
                if self.is_not_letter(guess):
                    continue
                if(self.is_guessed(guess)):
                    continue
                self.letters.append(guess)   
                if self.is_found_letters(guess):
                    break
            except KeyboardInterrupt:
                break;    
        return self.check_winner()           
        
    def is_not_letter(self, guess):
        pattern = r"^[A-Za-z]*$"
        if len(guess) > 1 or not re.match(pattern, guess):
          return self.wrong_message('Invalid input. Enter a single letter') 
        return False  
          
    def is_guessed(self, guess):
        if guess in self.letters:
            return self.wrong_message('Oops! You already tried that guess, try again!') 
        return False
    
    def wrong_message(self, message):
        clear_screen()  
        print(f'🚫 {Color.red}{message}{Color.restore}\n')
        time.sleep(2)      
        return True
    
    def is_found_letters(self, guess):
        found_letter = False    
        for index, letter in enumerate(self.word):
            if guess == letter:
                self.display = self.display[:index] + guess + self.display[index + 1:]
                found_letter = True
        if not '_' in list(self.display):
            self.win = True
            return True
        if not found_letter:
            self.fails += 1
        return False    
        
    def check_winner(self):
        clear_screen()
        self.print_pics(self.fails)
        time.sleep(1)
        clear_screen()
        if self.win:
            print(f'{Color.green} 🎆 YOU WIN!{Color.restore}\n')
        else:
            print(f'{Color.red} ❌ YOU LOSE!{Color.restore}\n')     
        time.sleep(2.5)      
        return True       
    
