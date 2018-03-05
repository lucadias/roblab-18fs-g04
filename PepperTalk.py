import qi
connection_url = "192.168.1.102:9559"
app = qi.Application(["--qi-url=" + connection_url])
app.start()
session = app.session
tts = session.service("ALTextToSpeech")
tts.say("\\rspd=150\")

motion = session.service("ALMotion")
motion.moveTo(1.0, 1.0, 0.0)