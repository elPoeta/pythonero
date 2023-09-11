import random


def main():
    problems = get_problems()
    resolve_problems(problems)

def get_level():
    while True:
      try:
        level = int(input("Level: "))
        if level < 1 or level > 3:
          raise ValueError("Level must be 1, 2 or 3")
        return level
      except ValueError:
        continue  


def generate_integer(level):
    if level == 1:
      return random.randint(0, 9)
    elif level == 2:
      return random.randint(10, 99)
    else:
      return random.randint(100, 999)


def get_problems(n=10):
  level = get_level()
  problems = []
  for i in range(n):
    problems.append({ "x": generate_integer(level), "y": generate_integer(level) })
  return problems

def resolve_problems(problems):
  i = 0
  score = 0
  chance = 0
  while i < len(problems):
    chance += 1
    try:
      x = problems[i]["x"]
      y = problems[i]["y"]
      r = int(input(f"{x} + {y} = "))
      if r == ( x + y ):
        score += 1
        chance = 0
        i += 1
      elif chance > 2:
        print(f"{x} + {y} = {x + y}")
        chance = 0
        i += 1
      else:
        print("EEE")    
    except ValueError:
      print("EEE")  
  print(f"Score: {score}")   
    
if __name__ == "__main__":
    main()
    
    
    