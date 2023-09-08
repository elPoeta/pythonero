def main():
  dict = input_data()
  print_data(dict)

def input_data():
  dict = {}
  while True:
    try:
      item = input().upper()
      if item in dict:
        dict[item] += 1
      else:
        dict[item] = 1    
    except EOFError:  
      break;
  return dict
 
def print_data(dict):
  for k,v in dict.items():
    print(f'{v} {k}')

 

main()  