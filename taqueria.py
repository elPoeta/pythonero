
def main():
  order_menu()
  
def order_menu():
  total = 0
  dict = get_menu()
  while True:
    try:
      item = input("Item: ").lower().title()
      if item in dict:
        total += dict[item]
        print(f'Total: ${total:.2f}')
    except EOFError:  
      print()
      break;
  return total
  
def get_menu(): 
  return {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
  }

main()