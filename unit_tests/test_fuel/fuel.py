def main():
  while True:
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    if percentage is not None:
      break

  gauge(percentage)

def convert(fraction):
  try:
    nums = fraction.split('/')
    if len(nums) != 2:
     raise ValueError("Missing numbers")
    x = int(nums[0])
    y = int(nums[-1])

    if x > y :
      raise ValueError("X is greater than Y")
    return round(float(x / y) * 100)
  except (ValueError, ZeroDivisionError):
     return None


def gauge(percentage):
  if(percentage >= 99):
    print('F')
  elif percentage > 1:
     print(f'{percentage}%')
  else:
    print('E')


if __name__ == "__main__":
    main()
