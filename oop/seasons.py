from datetime import date
import sys
import inflect
import operator

p = inflect.engine()


def main():
  date_of_birth = input("Date of Birth: ")
  print(convert(date_of_birth))



def convert(date_of_birth):
  try:
    difference = operator.sub(date.today(), date.fromisoformat(date_of_birth))
    minutes = difference.days * 24 * 60
    return f"{(p.number_to_words(minutes, andword='')).capitalize()} minutes"
  except ValueError:
    sys.exit("Invalid date")

if __name__ == "__main__":
    main()
