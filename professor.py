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
      p = problems[i]
      r = int(input(f"{p['x']} + {p['y']} = "))
      score, chance, i = check(p, r, score, chance, i)  
    except ValueError:
      print("EEE")  
  print(f"Score: {score}")   

def check(p, r, score, chance, i):
  if r == ( p["x"] + p["y"] ):
    score += 1
    chance = 0
    i += 1
  elif chance > 2:
    print(f"{p['x']} + {p['y']} = {p['x'] + p['y']}")
    chance = 0
    i += 1
  else:
    print("EEE")
  return (score, chance, i)     

     
if __name__ == "__main__":
    main()
    
    
    