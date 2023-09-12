def main():
    greet = input("- ")
    print(convert(greet))


def convert(greet):
    return greet.replace(":)", "🙂").replace(":(", "🙁")


main()
