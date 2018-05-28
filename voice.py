import qi
import time

connection_url = "192.168.1.102:9559"
app = qi.Application(["--qi-url=" + connection_url])  # Connection to robot
app.start()
session = app.session
tts = session.service("ALTextToSpeech")
tts.say("Do you like to introduce yourself?")

sr = session.service("ALSpeechRecognition")
sr.pause(False)
memory = session.service("ALMemory")
memory.subscribeToEvent("WordRecognized", "Test", "onWordRecognized")

def onWordRecognized(self, key, value, message):
    if(len(value) > 1 and value[1] >= 50/100.):
        tts.say("Nothing")
        print(value[0])
        tts.say(value[0]) #~ activate output of the box
    else:
        tts.say("Nothing")

word_list = "Yes;No;Bye"

sr.pause(True)
sr.setVocabulary(word_list.split(';'), False)
sr.pause(False)