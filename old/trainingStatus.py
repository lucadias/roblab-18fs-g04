########### Python 2.7 #############
import httplib, urllib, base64

class trainingStatus:

	def __init__(self):
	    print("init trainingStatus")

	def trainingStatus:
		headers = {
		    # Request headers
		    'Ocp-Apim-Subscription-Key': '427c314271e24c218eee1c65079fd434',
		}

		params = urllib.urlencode({
		})

		body = {
			
		}

		try:
		    conn = httplib.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
		    conn.request("GET", "/face/v1.0/persongroups/secretarygroup/training?%s" % params, str(body), headers)
		    response = conn.getresponse()
		    data = response.read()
		    print(data)
		    conn.close()
		except Exception as e:
		    print("[Errno {0}] {1}".format(e.errno, e.strerror))
		return data["status"]
	####################################
