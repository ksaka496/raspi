import requests
import config 

url = "https://notify-api.line.me/api/notify"
access_token = config.accesskey

headers = {'Authorization': 'Bearer ' + access_token}
message = 'image test'

image = '/test.jpg' 
payload = {'message': message}
files = {'imageFile': open(image, 'rb')}
r = requests.post(url, headers=headers, params=payload, files=files)
