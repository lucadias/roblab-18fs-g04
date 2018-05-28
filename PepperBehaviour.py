from VoiceRecognition import VoiceRecognition
import time


class PepperBehaviour:
	speech = None
	def __init__(self):
		print("Init Behaviour")
		speech = VoiceRecognition()
		speech.set_callback(self.callback)
		time.sleep(5)
		speech.start_recognition()
		time.sleep(5)
		speech.stop_recognition()

	def callback(self, yes):
		print(yes)

if __name__ == "__main__":
	hallo = PepperBehaviour()
	while True:
		pass