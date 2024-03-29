import re


def main():
    print(count(input("Text: ")))


def count(s):
    regex = r"(^|\W)um($|\W)"
    match = re.findall(regex, s, re.IGNORECASE)
    return len(match) if match else 0  


if __name__ == "__main__":
    main()