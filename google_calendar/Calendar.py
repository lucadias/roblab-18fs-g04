import requests
import json
import time


class Calendar:

	_oauth_headers = {
		"Content-Type": "application/x-www-form-urlencoded"
	}

	_client_id = "428817651700-99v34a1ist38fndgol2e1mcpibreh87d.apps.googleusercontent.com"
	_client_secret = "fWmSuC7_I-dpMrhwIhCuzc9B"

	_request = None
	_device_code = ""
	_poll_interval = 5


	def __init__(self):
		print("Init Calendar")

	def step_1_request_device_code(self):
		json_data = {
			"client_id": self._client_id,
			"scope": "https://www.googleapis.com/auth/calendar"
		}
		url = "https://accounts.google.com/o/oauth2/device/code"

		r = requests.post(url, data=json_data, headers=self._oauth_headers)
		self._request = r

	def step_2_show_device_code(self):
		if self._request.status_code == 200:
			print("Please enter this Device Code: " + self._request.json()["user_code"])
			self._device_code = self._request.json()["device_code"]
			self._poll_interval = self._request.json()["interval"]
		else:
			print("Error: " + self._request.content)

	def step_3_poll_for_authorization(self):
		authorizing = True
		while authorizing:

			json_data = {
				"client_id": self._client_id,
				"client_secret": self._client_secret,
				"code": self._device_code,
				"grant_type": "http://oauth.net/grant_type/device/1.0"
			}

			url = "https://www.googleapis.com/oauth2/v4/token"
			r = requests.post(url, data=json_data, headers=self._oauth_headers)

			if r.status_code == 200:
				authorizing = False
				print("Authorized")
				print(r.content)
			elif r.json()["error"] == "authorization_pending":
				print("Auth. pending")
				print(r.content)
			elif r.json()["error"] == "access_denied":
				authorizing = False
				print("Access Denied")
			else:
				print(r)
				print(r.content)

			if authorizing:
				time.sleep(self._poll_interval)

if __name__ == "__main__":
    print("Start Calendar")
    cal = Calendar()
    cal.step_1_request_device_code()
    cal.step_2_show_device_code()
    cal.step_3_poll_for_authorization()