from naoqi import *
from time import sleep
from threading import Lock

ROBOT_IP = '192.168.1.102'

class MyFaceRec(ALModule):
    """A Module to recognize persons"""
    def __init__(self, name):
        ALModule.__init__(self,name)
        self.mutex = Lock()
        try:
            self.faceProxy = ALProxy("ALPeoplePerception")
        except Exception, fpError:
            raise fpError
        try:
            self.memProxy = ALProxy("ALMemory")
        except Exception, memError:
            raise memError


    def onLoad(self):
        try:
            self.faceProxy.subscribe("faceRec")
        except Exception, sErr:
            print "Couldnt subscribe to 'faceRec'"
            raise sErr
        self.BIND_PYTHON(self.getName(), "onPeopleDetected")
        self.faceProxy.setGraphicalDisplayEnabled(True)
        self.faceProxy.setMovementDetectionEnabled(True)
        self.faceProxy.setTimeBeforePersonDisappears(5)
        self.faceProxy.setMaximumDetectionRange(0.5)

    def onInput_onStart(self):
        self.mutex.acquire()
        try:
            self.memProxy.subscribeToEvent("JustArrived", self.getName(), "onPeopleDetected")
            print "I'm starting to look for people"
        except Exception, subscrErr:
            self.mutex.release()
            print "Error with subscribing to PeopleDetected"
            self.onUnload()
            raise subscrErr
        self.mutex.release()


    def onUnload(self):
        self.mutex.acquire()
        try:
            self.memProxy.unsubscribeToEvent("JustArrived", self.getName())
        except Exception, unsubErr:
            self.mutex.release()
            print "Error with unsubscribing to PeopleDetected"
            exit(1)
            raise unsubErr
        print "I'm done"
        try:
            self.faceProxy.unsubscribe("faceRec")
        except Exception, usErr:
            self.mutex.release()
            print "Error with unsubscribing from 'faceRec"
            exit(1)
            raise usErr
        self.mutex.release()

    def onPeopleDetected(self, key, personId, faceRec):
        print "I've seen somebody!"


global broker
broker = ALBroker("pythonBroker", "0.0.0.0", 0, ROBOT_IP, 9559)
global pythonPeopleModule
pythonPeopleModule = MyFaceRec('pythonFaceRec')
pythonPeopleModule.onLoad()
pythonPeopleModule.onInput_onStart()
sleep(10)
pythonPeopleModule.onUnload()
