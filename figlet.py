import sys
from pyfiglet import Figlet

if len(sys.argv) < 3 or len(sys.argv)  >= 4:
  sys.exit("Invalid usage")

flag, font = sys.argv[1:]

if flag != "-f":
   sys.exit("Invalid usage")

figlet = Figlet()

fonts = figlet.getFonts()


figlet.setFont(font=font)

s = input("Input: ")

print(figlet.renderText(s))