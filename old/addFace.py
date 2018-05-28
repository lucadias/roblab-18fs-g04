########### Python 2.7 #############
import httplib, urllib, base64


class addFace:

	def __init__(self):
	    print("init addFace")

	def addFace(self, stringIMGURL):
		headers = {
		    # Request headers
		    'Content-Type': 'application/json',
		    'Ocp-Apim-Subscription-Key': '89cf9dccd73f4450a8e8dbc9fdc31ff9',
		}

		params = urllib.urlencode({
		})

		body = {
			 "url": stringIMGURL
		}

		try:
		    conn = httplib.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
		    conn.request("POST", "/face/v1.0/persongroups/secretarygroup/persons/be977823-edb2-4f97-a904-8c5f91498730/persistedFaces?%s" % params, str(body), headers)
		    response = conn.getresponse()
		    data = response.read()
		    print(data)
		    conn.close()
		except Exception as e:
		    print("[Errno {0}] {1}".format(e.errno, e.strerror))
		return data["persistedFaceId"]
####################################
