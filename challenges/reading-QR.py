from pyzbar.pyzbar import decode
from PIL import Image
from dotenv import load_dotenv
import requests
import urllib.request
import json
import os

load_dotenv()

token = os.getenv('ACCESS_TOKEN')

# getting the problem set
problem = requests.get(
    f"https://hackattic.com/challenges/reading_qr/problem?access_token={token}")

# parsing the image url
url = problem.json()['image_url']

qrcode = urllib.request.urlretrieve(url, "../assets/reading-QR.jpg")
decodeQR = decode(Image.open(qrcode[0]))
qrdata = decodeQR[0].data.decode()

# payload = json.dumps({"code" : qrdata})
payload = {
    "code" : qrdata
}

solution = requests.post(
    f"https://hackattic.com/challenges/reading_qr/solve?access_token={token}", json=payload)

if solution.status_code == 200:
    print(f"Solution submitted successful - {solution.text}")
else:
    print(f"Something went wrong - {solution.text}")
