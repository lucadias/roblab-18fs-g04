import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from Person import Person


# pip install firebase-admin
class Database:

	_credits = None
	_persons_ref = None

	def __init__(self):
		# Fetch the service account key JSON file contents
		self._credits = credentials.Certificate('secretary-37bdb-firebase-adminsdk-7sw3i-e1123562ed.json')

		# Initialize the app with a service account, granting admin privileges
		firebase_admin.initialize_app(self._credits, {
		    'databaseURL': 'https://secretary-37bdb.firebaseio.com/'
		})

		ref = db.reference("version")
		print "Version: " + str(ref.get())

		self._persons_ref = db.reference("persons")

	def save_person(self, person):
		ref = self._persons_ref.child(person._id)
		ref.set(person)

	def get_person(self, person_id):
		per = self._persons_ref.child(person_id).get()
		newPerson = Person(per["id"], per["name"], per["google_calendar"], per["iot"])
		return newPerson


if __name__ == "__main__":
    print("Start Database")
    db_sec = Database()

    db_sec.save_person(Person("2", "Benjamin", True, False))

    print db_sec.get_person("2").name
