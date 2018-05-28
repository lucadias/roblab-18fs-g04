import qi
from time import sleep
import os
from azureFaceAPI import azureFaceAPI
connection_url = "192.168.1.102:9559"
app = qi.Application(["--qi-url=" + connection_url])
app.start()
session = app.session
afa = azureFaceAPI()


afa.detectFaceBinary(picture_path[0])

