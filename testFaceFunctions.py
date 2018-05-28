import os

import requests

from azureFaceAPI import azureFaceAPI
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import base64

afa = azureFaceAPI()

# resultdetectFace = afa.detectFace("https://i.imgur.com/b2Tp1Hx.jpg")
# print(resultdata)


# afa.createPerson("luca")
# {"personId":"b66373f2-1eb6-418c-8a63-f2add18dc185"}

# afa.addFace("https://i.imgur.com/yOPVtKo.jpg","b66373f2-1eb6-418c-8a63-f2add18dc185")
# {"persistedFaceId":"bfb3239f-f323-491a-8201-f2dfbfec0864"}

# afa.traingroup()

# afa.trainingStatus()


print(open('imageluca.jpg', 'rb').read())


#afa.identifyFace(afa.detectFaceBinary("imageluca.jpg"))

# afa.identifyFace("1740bb9e-542a-4370-aa43-46707002d0c6")

#afa.listfaces();

# [{"faceId":"1740bb9e-542a-4370-aa43-46707002d0c6","faceRectangle":{"top":397,"left":1033,"width":485,"height":485}}]

# [{"faceId":"6398159d-4d80-4bc4-85b5-8dc8e8ecb9a8","faceRectangle":{"top":397,"left":1031,"width":484,"height":484}}]


# afa.identifyFace("6398159d-4d80-4bc4-85b5-8dc8e8ecb9a8")


# afa.removePerson('secretarygroup','8defce83-6b3d-4b73-974c-cba78dcd7b26')

# afa.listfaces();
