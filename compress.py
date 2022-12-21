from zipfile import ZipFile

path = './image.jpeg'

with ZipFile('photos.zip', 'w') as myzip:
    myzip.write(path)
