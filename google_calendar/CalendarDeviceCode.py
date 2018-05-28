import requests
import json

if False:
	headers = {
		"Content-Type": "application/x-www-form-urlencoded",
		"Host": "accounts.google.com"
	}

	json_data = {
		"client_id": "428817651700-99v34a1ist38fndgol2e1mcpibreh87d.apps.googleusercontent.com",
		"scope": "https://www.googleapis.com/auth/calendar"
	}

	url = "https://accounts.google.com/o/oauth2/device/code"

	r = requests.post(url, data=json_data, headers=headers)
	print(r)
	print(r.content)

else:
	headers = {
		"Content-Type": "application/x-www-form-urlencoded"
	}

	json_data = {
		"client_id": "428817651700-99v34a1ist38fndgol2e1mcpibreh87d.apps.googleusercontent.com",
		"client_secret": "fWmSuC7_I-dpMrhwIhCuzc9B",
		"code": "AH-1Ng0pa3awpjXtyKdwwSou7rifkTeQBkLacLvxNbjmLpe3JGnvEK8RI_sn_M_wn6YIZedd_5SjMhvYWMxNGJNrJfLT4dzz3w",
		"grant_type": "http://oauth.net/grant_type/device/1.0"
	}

	url = "https://www.googleapis.com/oauth2/v4/token"
	r = requests.post(url, data=json_data, headers=headers)
	print(r)
	print(r.content)