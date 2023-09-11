import sys
import random
from pyfiglet import Figlet

def main():
  length = len(sys.argv)
  if length <= 2:
    sys.exit("Invalid usage")
  elif length > 2:
    if len(sys.argv) < 3 or len(sys.argv)  >= 4:
      sys.exit("Invalid usage")

    flag, font = sys.argv[1:]

    if flag != "-f" and flag != "-font":
      sys.exit("Invalid usage")

    figlet = Figlet()
    fonts = figlet.getFonts()

    if font not in fonts:
      sys.exit("Invalid usage")

    write_output(figlet, font)

  else:
    figlet = Figlet()
    fonts = figlet.getFonts()
    random_font = random.choice(fonts)
    write_output(figlet, random_font)

def write_output(figlet, font):
    figlet.setFont(font=font)
    s = input("Input: ")
    print("Output:")
    print(figlet.renderText(s))

if __name__ == "__main__":
  main()