def main():
    text = input("Input: ").strip()
    output = ''
    for letter in text:
        output += letter if not isVowel(letter) else ''
    print(f'Output: {output}')


def isVowel(letter):
    dict = {
        'a': 'a',
        'e': 'e',
        'i': 'i',
        'o': 'o',
        'u': 'u',
    }
    return letter.lower() in dict


main()
