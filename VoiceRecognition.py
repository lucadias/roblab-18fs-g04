import qi
import time


class VoiceRecognition:
	recognizer = None
	speech_subscriber = None
	callback_function = None

	do_recognition = False

	def __init__(self):

		connection_url = "192.168.1.102:9559"
		app = qi.Application(["--qi-url=" + connection_url])  # Connection to robot
		app.start()
		session = app.session

		memory = session.service("ALMemory")
		self.speech_subscriber = memory.subscriber("WordRecognized")
		self.speech_subscriber.signal.connect(self.speech_detected)
		self.recognizer = session.service("ALSpeechRecognition")
		self.recognizer.pause(False)
		self.recognizer.pause(True)
		word_list = "Yes;No;Bye"
		self.recognizer.setVocabulary(word_list.split(';'), False)
		self.recognizer.pause(False)
		self.recognizer.subscribe("Helper")


		tts = session.service("ALTextToSpeech")
		tts.say("Do you like to introduce yourself?")

	def start_recognition(self):
		self.do_recognition = True

	def stop_recognition(self):
		self.do_recognition = False


	def set_callback(self, callback_function):
		self.callback_function = callback_function

	def speech_detected(self, *args):
		if self.do_recognition:
			print("Word erkannt")
			print(args[0])
			print(args[0], args[0][0], args[0][1])
			if self.callback_function != None:
				if args[0][0] == "No" and args[0][1] > 0.5:
					print("callback")
					self.callback_function(False)
				elif args[0][0] == "Yes" and args[0][1] > 0.5:
					print("callback")
					self.callback_function(True)


#if __name__ == "__main__":
#	speech = VoiceRecognition()
#	while True:
#		pass