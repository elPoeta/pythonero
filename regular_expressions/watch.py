import re

def main():
    print(parse(input("HTML: ")))


def parse(s):
  regex = r"https?://(www\.)?youtube\.com/embed/([a-zA-Z0-9]+)"
  pattern = f'<iframe src="{regex}"></iframe>'
  matches = re.search(pattern, s)
  if matches:
    return f"https://youtu.be/{matches.group(2)}"
  else:
    return None



if __name__ == "__main__":
    main()