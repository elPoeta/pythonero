import inflect

words = []
while True:
  try:
    s = input("Input: ")
    words.append(s)
  except EOFError:
    break;

p = inflect.engine()
print()
print(f"Adieu, adieu, to {p.join(words)}")
