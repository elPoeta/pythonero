# Fuel gauges indicate, often with fractions, just how much fuel is in a tank. For instance 1/4 indicates that a tank is 25% full, 
# 1/2 indicates that a tank is 50% full, and 3/4 indicates that a tank is 75% full.

# In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer,
# and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. If, though, 1% or less remains, 
# output E instead to indicate that the tank is essentially empty. And if 99% or more remains, output F instead to indicate that the tank 
# is essentially full.

# If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. (It is not necessary for Y to be 4.)
# Be sure to catch any exceptions like ValueError or ZeroDivisionError.

def main():
  fuel = get_tank_fuel()
  
  if(fuel >= 99):
    print('F')
  elif fuel > 1:
     print(f'{fuel}%')
  else:   
    print('E')
    
def get_tank_fuel():
  while True:
    try:
      fraction = input("Fraction: ")
      nums = fraction.split('/')
      if len(nums) != 2:
        continue
      x = int(nums[0])
      y = int(nums[-1])
    
      if x > y :
        raise ValueError("X is greater than Y")
      return round(float(x / y) * 100)
    except (ValueError, ZeroDivisionError):
      pass
      
  
main()     