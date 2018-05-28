import httplib, urllib, base64
import ast
import requests
import json


class azureFaceAPI:

    currentpersonFaceId = None

    def __init__(self):
        print("init azureFaceAPI")

    def createPerson(self, personname):
        headers = {
            # Request headers
            'Content-Type': 'application/json',
            'Ocp-Apim-Subscription-Key': '89cf9dccd73f4450a8e8dbc9fdc31ff9',
        }

        params = urllib.urlencode({
        })

        body = {"name": personname}

        try:
            conn = httplib.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
            conn.request("POST", "/face/v1.0/persongroups/secretarygroup/persons?%s" % params, str(body), headers)
            response = conn.getresponse()
            data = response.read()
            print(data)
            conn.close()
        except Exception as e:
            print("[Errno {0}] {1}".format(e.errno, e.strerror))

        d = ast.literal_eval(data)
        print d["personId"]
        return d['personId']

    def removePerson(self,persongroupid,personid):

        headers = {
            # Request headers
            'Ocp-Apim-Subscription-Key': '89cf9dccd73f4450a8e8dbc9fdc31ff9',
        }

        params = urllib.urlencode({
        })

        try:
            conn = httplib.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
            conn.request("DELETE", "/face/v1.0/persongroups/"+persongroupid+"/persons/"+personid+"?%s" % params, "{body}",
                         headers)
            response = conn.getresponse()
            data = response.read()
            print(data)
            conn.close()
        except Exception as e:
            print("[Errno {0}] {1}".format(e.errno, e.strerror))

        ####################################


    def addFaceBinary(self, img, personid):
        url = "https://westcentralus.api.cognitive.microsoft.com/face/v1.0/persongroups/secretarygroup/persons/"+personid+"/persistedFaces"

        headers = {
            'ocp-apim-subscription-key': "89cf9dccd73f4450a8e8dbc9fdc31ff9",
            'Content-Type': "application/octet-stream",
            'cache-control': "no-cache",
        }

        data = open(img, 'rb').read()

        response = requests.post(url, headers=headers, data=data)

        d = ast.literal_eval(response.text)
        if not d:
            print ("fehler")
            return "fehler keine person erkannt"

        print d

    def addFace(self, stringIMGURL, personid):
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
            conn.request("POST",
                         "/face/v1.0/persongroups/secretarygroup/persons/"+personid+"/persistedFaces?%s" % params,
                         str(body), headers)
            response = conn.getresponse()
            data = response.read()
            print(data)
            conn.close()
        except Exception as e:
            print("[Errno {0}] {1}".format(e.errno, e.strerror))
        return

    def listfaces(self):
        headers = {
            # Request headers
            'Ocp-Apim-Subscription-Key': '89cf9dccd73f4450a8e8dbc9fdc31ff9',
        }

        params = urllib.urlencode({
            # Request parameters
            'start': '1',
            'top': '1000',
        })

        try:
            conn = httplib.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
            conn.request("GET", "/face/v1.0/persongroups/secretarygroup/persons?%s" % params, "{body}", headers)
            response = conn.getresponse()
            data = response.read()
            print(data)
            conn.close()
        except Exception as e:
            print("[Errno {0}] {1}".format(e.errno, e.strerror))
        return

    def traingroup(self):
        headers = {
            # Request headers
            'Ocp-Apim-Subscription-Key': '89cf9dccd73f4450a8e8dbc9fdc31ff9',
        }

        params = urllib.urlencode({
        })

        body = {

        }

        try:
            conn = httplib.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
            conn.request("POST", "/face/v1.0/persongroups/secretarygroup/train?%s" % params, str(body), headers)
            response = conn.getresponse()
            data = response.read()
            print(data)
            conn.close()
        except Exception as e:
            print("[Errno {0}] {1}".format(e.errno, e.strerror))
        return

    def trainingStatus(self):
        headers = {
            # Request headers
            'Ocp-Apim-Subscription-Key': '89cf9dccd73f4450a8e8dbc9fdc31ff9',
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


    def detectFaceBinary(self, img):
        url = "https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect"

        headers = {
            'ocp-apim-subscription-key': "89cf9dccd73f4450a8e8dbc9fdc31ff9",
            'Content-Type': "application/octet-stream",
            'cache-control': "no-cache",
        }

        data = open(img, 'rb').read()

        response = requests.post(url, headers=headers, data=data)

        d = ast.literal_eval(response.text)
        if not d:
            print ("fehler keine person erkannt")
            return "fehler keine person erkannt"

        print d
        print d[0]['faceId']
        self.currentpersonFaceId = d[0]['faceId']
        return d[0]['faceId']

    def detectFace(self, stringIMGURL):
        headers = {
            # Request headers
            'Content-Type': 'application/json',
            'Ocp-Apim-Subscription-Key': '89cf9dccd73f4450a8e8dbc9fdc31ff9',
        }

        params = urllib.urlencode({
            # Request parameters
            'returnFaceId': 'true',
            'returnFaceLandmarks': 'false',
        })

        body = {
            "url": stringIMGURL
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
        return data

    ####################################

    def identifyFace(self, faceIds):
        headers = {
            # Request headers
            'Content-Type': 'application/json',
            'Ocp-Apim-Subscription-Key': '89cf9dccd73f4450a8e8dbc9fdc31ff9',
        }

        params = urllib.urlencode({
        })

        body = {
            "personGroupId": "secretarygroup",
            "faceIds": [faceIds],
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

        d = ast.literal_eval(data)
        if not d[0]["candidates"]:
            print ("person nicht bekannt")
            return "person nicht bekannt"
        returnvalue = d[0]["candidates"][0]["personId"]
        print(returnvalue)
        return returnvalue

    def getPerson(self,personid):
        headers = {
            # Request headers
            'Ocp-Apim-Subscription-Key': 'b91e5612915c46d7b7b9614f2e1f82cc',
        }

        params = urllib.urlencode({
        })

        try:
            conn = httplib.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
            conn.request("GET", "/face/v1.0/persongroups/secretarygroup/persons/"+personid+"?%s" % params, "",
                         headers)
            response = conn.getresponse()
            data = response.read()
            print(data)
            conn.close()
        except Exception as e:
            print("[Errno {0}] {1}".format(e.errno, e.strerror))

        d = json.loads(data)

        print(type(d))
        print("print d:")
        print(d)
        return d['name']