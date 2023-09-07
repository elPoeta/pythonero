def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    length = len(s)
    if length < 2 or length > 6:
        return False
    
    if not (s[0:2]).isalpha():
        return False

    for i in range(length):
        letter = s[i]
        if letter.isalnum():
            if letter.isdigit():
                if letter == '0':
                    return False
                return (s[i:]).isdigit()     
        else:
            return False
              
    return True


main()
