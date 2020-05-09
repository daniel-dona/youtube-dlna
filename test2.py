import simple_ssdp as ssdp
import upnpclient
import time

disc = list(ssdp.discover("urn:schemas-upnp-org:device:MediaRenderer:1", retries=2, timeout=3))
uri = disc[0].getlocation() #Si detecta más de uno habría que implementar alguna forma de seleccionar

dev = d = upnpclient.Device(uri)

d.AVTransport.SetAVTransportURI(InstanceID=0,CurrentURI="https://archive.org/download/BigBuckBunny/big_buck_bunny_720p_h264.mov",CurrentURIMetaData= '')

d.AVTransport.SetAVTransportURI(InstanceID=0,CurrentURI="https://archive.org/download/BigBuckBunny/big_buck_bunny_720p_h264.mov",CurrentURIMetaData= '')

while True:
	d.AVTransport.GetPositionInfo(InstanceID=0)
	time.sleep(1)



