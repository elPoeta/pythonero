import sys
import os
from PIL import Image, ImageOps

def main():
  validate_args()
  build_image()
  
def build_image():
  try:
    muppet = Image.open(sys.argv[1])
    shirt = Image.open("shirt.png")
  except FileNotFoundError:  
    sys.exit("Input does not exist")
  
  (w,h) = shirt.size  
  muppet = ImageOps.fit(muppet, (w, h))
  muppet.paste(shirt, shirt)
  muppet.save(sys.argv[2])
  
  
def validate_args():
  length = len(sys.argv[1:])
  if length <= 1:
    sys.exit("Too few command-line arguments")
  if length > 2:
    sys.exit("Too many command-line arguments")
  (_, file_ext1) = os.path.splitext(sys.argv[1])
  (_, file_ext2) = os.path.splitext(sys.argv[2])   
  extensions = [".jpg", ".jpeg", ".png"]
  if file_ext1.lower() not in extensions or file_ext2.lower() not in extensions:
    sys.exit("Invalid input")
  if file_ext1.lower() != file_ext2.lower():
    sys.exit("Input and output have different extensions")  

if __name__ == "__main__":
  main()