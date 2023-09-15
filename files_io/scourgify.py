import sys
import csv

def main():
  validate_args()
  #students = get_sorted_students(get_new_format(sys.argv[1]))
  write_csv_file(get_new_format(sys.argv[1]))

def get_new_format(filePath):
  after_read = []
  try:
    with open(filePath, "r", newline='\n') as csvfile:
      reader = csv.DictReader(csvfile)
      for row in reader:
        last, first = row["name"].strip().split(",")
        after_read.append({ "first": first.strip().replace("\"", ""), "last": last.replace("\"", ""), "house": row["house"].replace("\n", "")})
  except FileNotFoundError:
    sys.exit(f"Could not read {filePath}")
  return after_read

def get_sorted_students(students):
  sorted_students = []
  for student in sorted(students, key=lambda student: student["last"], reverse=True):
    sorted_students.append({ "first": student['first'], "last": student['last'], "house": student['house'] })
  return sorted_students

def write_csv_file(students):
  with open(sys.argv[2], "w") as file:
    writer = csv.DictWriter(file, fieldnames = ["first", "last", "house"])
    writer.writeheader()
    for student in students:
      writer.writerow({ "first": student["first"], "last": student["last"], "house": student["house"] })

def validate_args():
  length = len(sys.argv[1:])
  if length <= 0:
    sys.exit("Too few command-line arguments")
  if length > 2:
    sys.exit("Too many command-line arguments")
  file_path = sys.argv[1]
  if not file_path.endswith(".csv"):
    sys.exit("Input is not a CSV file")
  file_path = sys.argv[2]
  if not file_path.endswith(".csv"):
    sys.exit("Output is not a CSV file")


if __name__ == "__main__":
  main()
