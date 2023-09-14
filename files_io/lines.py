import sys
import os

def main():
  validate_args()
  print(count_lines())

def validate_args():
  length = len(sys.argv[1:])
  if length <= 0:
    sys.exit("Too few command-line arguments")
  if length > 1:
    sys.exit("Too many command-line arguments")  
  file_path = sys.argv[1]
  if not file_path.endswith(".py"):
    sys.exit("Not a Python file")
  if not os.path.isfile(file_path):
    sys.exit("File does not exist")

def count_lines():
  count = 0
  with open(sys.argv[1]) as file:
    for line in file:
      l = line.lstrip()
      if len(l) > 0 and not l.startswith("#"):
        count +=1
  return count 
       
if __name__ == "__main__":
  main()  