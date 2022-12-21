import requests
from io import BytesIO
from PIL import Image

req = requests.get(
    'https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1172&q=80')

print(req.status_code)

img = Image.open(BytesIO(req.content))
path = './image.' + img.format.lower()
try:
    img.save(path, img.format)
except IOError:
    print('Cannot save image')
