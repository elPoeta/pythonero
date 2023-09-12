camel_case = input('camelCase: ').strip()
snake_case = ''
for letter in camel_case:
    snake_case += letter if letter.islower() else '_' + letter.lower()

print(f'snake_case: {snake_case}')
