########## Python 2.7 #############
import httplib, urllib, base64

class detectFace:

	def __init__(self):
	    print("init detectFace")


	def detectFace(self, stringIMGURL ):
		headers = {
		    # Request headers
		    'Content-Type': 'application/json',
		    'Ocp-Apim-Subscription-Key': '427c314271e24c218eee1c65079fd434',
		}

		params = urllib.urlencode({
		    # Request parameters
		    'returnFaceId': 'true',
		    'returnFaceLandmarks': 'false',
		})

		body = {
			"url" : stringIMGURL
		}

		try:
		    conn = httplib.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
		    conn.request("POST", "/face/v1.0/detect?%s" % params, str(body), headers)
		    response = conn.getresponse()
		    data = response.read()
		    print(data)
		    conn.close()
		except Exception as e:
		    print("[Errno {0}] {1}".format(e.errno, e.strerror))
		return data["faceID"]
	####################################
