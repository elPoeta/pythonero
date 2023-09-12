fileName = input('File name: ').lower().strip()

extension = fileName.split('.')[-1]

match extension:
    case 'gif' | 'jpg' | 'jpeg' | 'png':
        ext = extension if extension != 'jpg' else 'jpeg'
        print(f'image/{ext}')
    case 'pdf' | 'zip':
        print(f'application/{extension}')
    case 'txt':
        print(f'text/plain')
    case _:
        print('application/octet-stream')
