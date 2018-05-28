from naoqi import ALProxy

memProxy = ALProxy("ALMemory","192.168.1.102",9559)

val = memProxy.getData("Device/SubDeviceList/Platform/InfraredSpot/Right/Sensor/Value")

print (str(val))