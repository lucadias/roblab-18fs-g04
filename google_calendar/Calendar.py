import requests
import json
import time
import datetime


class Calendar:

	_base_url = "https://www.googleapis.com/calendar/v3"
	_calendar_id = None

	_oauth_headers = {
		"Content-Type": "application/x-www-form-urlencoded"
	}

	_client_id = "428817651700-99v34a1ist38fndgol2e1mcpibreh87d.apps.googleusercontent.com"
	_client_secret = "fWmSuC7_I-dpMrhwIhCuzc9B"

	_request = None
	_device_code = ""
	_poll_interval = 5

	_access_token = ""
	_refresh_token = ""

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
				self._access_token = r.json()["access_token"]
				self._refresh_token = r.json()["refresh_token"]
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


	def step4_get_calendar(self):
		req = requests.get(self._base_url + "/users/me/calendarList?access_token=" + self._access_token)
		self._calendar_id = req.json()["items"][0]["id"]
		print(self._calendar_id)


	def step5_get_next_event(self):
		url = self._base_url + "/calendars/" + self._calendar_id + "/events?access_token=" + self._access_token + "&singleEvents=true&orderBy=startTime" + "&timeMin=" + datetime.datetime.now().isoformat() + "Z"
		print(url)
		req = requests.get(url)
		print(req.content)
		print(req.json()["items"][0]["summary"])
		if "date" in req.json()["items"][0]["start"]:
			print(req.json()["items"][0]["start"]["date"])
		elif "datetime" in req.json()["items"][0]["start"]:
			print(req.json()["items"][0]["start"]["dateTime"])


if __name__ == "__main__":
    print("Start Calendar")
    cal = Calendar()
    #cal.step_1_request_device_code()
    #cal.step_2_show_device_code()
    #cal.step_3_poll_for_authorization()
    cal._access_token = "ya29.GlvJBVRc8-Ao5AjYg_vX9vry27mSK-gj9DajxBPCbUopJ0fI-w7XsjBvogWF1YT-fcgNNBxkPAyMa_L6aiQhwiHlZeWt37PjUntzgwKwOnXp1oyudcmmbXG5xrZm"
    if cal._access_token != "":
    	cal.step4_get_calendar()
    	cal.step5_get_next_event()