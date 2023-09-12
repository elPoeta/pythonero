import random

def main():
  level = get_level()
  random_number = random.randint(1, level)  
  start(random_number)
  
def get_level():
  while True:
    try:
      level = int(input("Level: ")) 
      if level >= 1:
        return level     
    except ValueError:
      continue
    
def start(random_number):
  while True:
    try:
      guess = int(input("Guess: "))
      if guess < random_number:
        print("Too small!")
      elif guess > random_number:
        print("Too large!") 
      else:
        print("Just right!")
        break;   
    except ValueError:  
      continue   
      
if __name__ == "__main__":
  main()        
      