import cognitive_face as CF

KEY = 'fdd8f1e69955499e8a29a54073d7f4e8'  # Replace with a valid subscription key (keeping the quotes in place).
CF.Key.set(KEY)

BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0'  # Replace with your regional Base URL
CF.BaseUrl.set(BASE_URL)

# You can use this example JPG or replace the URL below with your own URL to a JPEG image.
img_url = 'https://i.imgur.com/LCMBbQV.jpg'
faces = CF.face.detect(img_url)
print(faces)