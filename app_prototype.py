import requests
from PIL import Image
import io
import os
from time import sleep

url = 'https://source.unsplash.com/featured/?{KEYWORD}'

print("Type what you want to see: ")
topic = input()

for i in range(0, 10):
    response = requests.get(url.format(KEYWORD = topic))
    if i == 0:
        prev_response_url = ''
    while prev_response_url == response.url:
        response = requests.get(url.format(KEYWORD = topic))
    img_bytes = io.BytesIO(response.content)
    img = Image.open(img_bytes)
    img.thumbnail((600, 600))
    img.save(f'img{i+1}.jpg')
    prev_response_url = response.url
