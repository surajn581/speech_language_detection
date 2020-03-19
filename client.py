
import requests
import json
import winsound
import io
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder


# addr = 'http://127.0.0.1:5000/get_labels'
# test_url = addr

# # prepare headers for http request
# content_type = 'text/plain'
# headers = {'content-type': content_type}

# image_path='sample/archies1.jpg'
# text = im2txt(image_path)
# # encode image as jpeg
# # _, img_encoded = cv2.imencode('.jpg', img)
# #print(img_encoded)
# #print(img_encoded.tostring())
# # send http request with image and receive response
# response = requests.post(test_url, data=text, headers=headers)


# URL = 'http://ec2-13-233-140-137.ap-south-1.compute.amazonaws.com:5050/'
# URL = "http://127.0.0.1:5000/audio"

# filename = 'beep.py'

# mp_encoder = MultipartEncoder(
#     fields={
#         'q': 'hello',
#         'audio': (filename, open(filename, 'rb'), 'text/plain'),
#     }
# )
# r = requests.post(
#     URL,
#     data=mp_encoder,  
#     headers={'Content-Type': mp_encoder.content_type}
# )
# # data = r.json()
# # decode response
# print(r)
# print(r.text)

import requests
filename = 'suits.jpg'
url = "http://127.0.0.1:5000/audio"
# winsound.PlaySound(filename, winsound.SND_FILENAME)
fin = open(filename,encoding="utf-8", errors='replace')
print(fin)
# with io.BufferedReader(fin) as r:
# 	lines = [str(line,'utf-8') for line in r]

# print(lines)
files = {'file': fin}
r = requests.post(url, files=files)
print(r)
print(r.text)  