import sys
import csv
from tabulate import tabulate

def main():
  lines = get_csv_lines(sys.argv[1])
  print(tabulate(lines, headers="keys", tablefmt="grid"))
  
def get_csv_lines(filePath):
  try:
    file_name, _ = filePath.split('.')
    first_key = f"{file_name.capitalize()} Pizza"
    dict = { first_key: [], "Small": [], "Large": [] }
    with open(filePath, newline='') as csvfile:
      reader = csv.DictReader(csvfile)
      for row in reader:
        dict[first_key].append(row[first_key])
        dict["Small"].append(row["Small"])
        dict["Large"].append(row["Large"])
  except FileNotFoundError:  
    sys.exit("File does not exist")
  return dict  
    
def validate_args():
  length = len(sys.argv[1:])
  if length <= 0:
    sys.exit("Too few command-line arguments")
  if length > 1:
    sys.exit("Too many command-line arguments")  
  file_path = sys.argv[1]
  if not file_path.endswith(".csv"):
    sys.exit("Not a CSV file")
    
if __name__ == "__main__":
  main()  