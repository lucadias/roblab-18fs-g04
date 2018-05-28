########### Python 2.7 #############
import httplib, urllib, base64

class identifyFace:

	def __init__(self):
	    print("init identifyFace")

	def identifyFace(self, faceIds ):
		headers = {
		    # Request headers
		    'Content-Type': 'application/json',
		    'Ocp-Apim-Subscription-Key': '427c314271e24c218eee1c65079fd434',
		}

		params = urllib.urlencode({
		})


		body = {
		    "personGroupId": "secretarygroup",
		    "faceIds":[faceIds],
		    "maxNumOfCandidatesReturned": 1,
		    "confidenceThreshold": 0.5
		}
		try:
		    conn = httplib.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
		    conn.request("POST", "/face/v1.0/identify?%s" % params, str(body), headers)
		    response = conn.getresponse()
		    data = response.read()
		    print(data)
		    conn.close()
		except Exception as e:
		    print("[Errno {0}] {1}".format(e.errno, e.strerror))

	####################################
	#[{
	#"faceId":"5d20ee66-278c-4c3e-a6a1-89e8cfe7fb22",
	#"candidates":[
	#	{
	#	"personId":"be977823-edb2-4f97-a904-8c5f91498730",
	#	"confidence":1.0
	#	}
	#]
	#}]
	#