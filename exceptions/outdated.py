def main():
  date = input_date()
  print(date)
  
def input_date():
  while True:
    try:
      date = input('Date: ').lower().strip()
      if not valid_date(date):
        print('#### '+ date)
        raise ValueError("Invalid input date")
      return formatted_date(date)
    except ValueError:  
      continue

def formatted_date(date):
  first_char = date[0:1]
  if first_char.isdigit():
    mm, dd, yyyy = date.split('/')
    return f"{yyyy}-{str(mm).zfill(2)}-{str(dd).zfill(2)}"
  else:
    month_day, year = date.split(',')
    month, day = month_day.split(' ')
    index = months().index(month.capitalize()) + 1  
    
    return f'{year.strip()}-{str(index).zfill(2)}-{str(day).zfill(2)}'
  
def valid_date(date):
  first_char = date[0:1]
  
  if first_char.isdigit():
    split_date = date.split('/')
    if len(split_date) != 3:
      return False
    if int(split_date[0]) > 12:
      return False
    if int(split_date[1]) > 31:
      return False  
  elif first_char.isalpha():
    split_date = date.split(',')
    if(len(split_date) != 2):
      return False
    
    month = split_date[0].split(' ')[0]
    day = split_date[0].split(' ')[-1]
    if months().index(month.capitalize()) < 1:
      return False
    if int(day) > 31:
      return False 
  else:
    return False   
     
  return True
  
def months():
  return [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
  ]
        
main()    