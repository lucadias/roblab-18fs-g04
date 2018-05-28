import requests
import time


class MyStrom:
	_headers = {
		"Content-Type": "application/json"
	}

	def __init__(self):
		print "init MyStrom"

	def turn_mystrom_on(self, ip):
		url = "http://" + str(ip) + "/relay?state=1"
		r = requests.get(url, headers=self._headers)

	def turn_mystrom_off(self, ip):
		url = "http://" + str(ip) + "/relay?state=0"
		r = requests.get(url, headers=self._headers)



if __name__ == "__main__":
	mystrom = MyStrom()
	mystrom.turn_mystrom_on("192.168.1.193")
	time.sleep(2)
	mystrom.turn_mystrom_off("192.168.1.193")