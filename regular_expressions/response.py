import validators


def main():
    print(validate(input("What's your email address? ")))


def validate(s):
    return f"Valid" if validators.email(s) else f"Invalid"


if __name__ == "__main__":
    main()