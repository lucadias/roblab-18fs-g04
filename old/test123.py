import qi
from pepperFaceRecognition import pepperFaceRecognition

connection_url = "192.168.1.102:9559"
app = qi.Application(["--qi-url=" + connection_url])
app.start()
session = app.session
tts = session.service("ALTextToSpeech")
tts.say("hallo")


pfr = pepperFaceRecognition('luca',session)

