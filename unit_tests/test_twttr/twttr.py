def main():
  word = input("Input: ")
  print(f'Output: {shorten(word)}')

def shorten(word):
    output = ''
    for letter in word.strip():
        output += letter if not isVowel(letter) else ''
    return output    

def isVowel(letter):
  return letter.lower()  in "aeiou"
   

if __name__ == "__main__":
    main()
