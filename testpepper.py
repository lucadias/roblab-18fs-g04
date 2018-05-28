from azureFaceAPI import azureFaceAPI
import qi

connection_url = "192.168.1.102:9559"
app = qi.Application(["--qi-url=" + connection_url])
app.start()
session = app.session
tts = session.service("ALTextToSpeech")
tts.say("hallo")

afa = azureFaceAPI()
#resultdetectFace = afa.detectFace("https://i.imgur.com/b2Tp1Hx.jpg")
#print(resultdata)
resultidentifyFace = afa.identifyFace("5d20ee66-278c-4c3e-a6a1-89e8cfe7fb22")
print(resultidentifyFace)