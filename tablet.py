import qi
import time


connection_url = "192.168.1.102:9559"
app = qi.Application(["--qi-url=" + connection_url])  # Connection to robot
app.start()
session = app.session
# tts = session.service("ALTextToSpeech")
# tts.say("I like to talk to myself and think about the world of humans.")

CALLBACK_ID = None

def callback(i, text):
    print(i)
    print(text)
    session.service("ALTabletService").onInputText.disconnect(CALLBACK_ID)

print("try")
try:
    tablet = session.service("ALTabletService")

    tablet.showWebview("https://pste.eu/p/RWR5.html")
    #tablet.showWebview("https://www.google.com")

    script = """
        node = document.getElementsByTagName("body")[0];
        while (node.hasChildNodes()) {
            node.removeChild(node.lastChild);
        }
        h1 = document.createElement("h1");
        h1.innerHTML = "Hallo Luca";
        node.append(h1);
    """

    script2 = """
        document.getElementById("title").innerHTML = "Hallo zusammen";
    """

    time.sleep(2)
    tablet.executeJS(script2)
    print("js executet")

    time.sleep(2)
    #tablet.showInputDialog("number", "[1] Kalender 1\n[2] Kalender 2\n[3] Kalender 3\n[4] Kalender 4", "Okeiiii", "Tschoona", "1", 100)
    #CALLBACK_ID = session.service("ALTabletService").onInputText.connect(callback)


    time.sleep(10)
    tablet.hideDialog()
    tablet.hideWebview()


    print("done")
except Exception, e:
    print e