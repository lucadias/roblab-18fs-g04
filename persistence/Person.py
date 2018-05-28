import json


class Person:
	_id = None
	_name = ""
	_google_calendar = False
	_iot = False

	def __init__(self, id, name, google_calendar, iot):
		self._id = id
		self._name = name
		self._google_calendar = google_calendar
		self._iot = iot

	def toJSON(self):
		return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)