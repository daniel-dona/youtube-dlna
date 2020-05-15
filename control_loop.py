import threading
import queue
import upnpclient


class ControlLoop(threading.Thread):

	def __init__(self, uri, qi, qo, *args, **kwargs):
		self.uri = uri
		self.qi = qi
		self.qo = qo
		self.status = 0
		
		super().__init__(*args, **kwargs)

	def connect(self, uri):
		try:
			self.device = upnpclient.Device(uri)
			self.status = 1
			self.log("Connected to "+ uri)
		except:
			self.log("Unable to connect to "+ uri)
			self.status = 0
			
	def log(self, msg):
		print("[Control Loop]", msg)
		
	def _status(self):
		threading.Timer(1.0, self._status).start()
		if self.status == 1:
			self.qo.put(self.device.AVTransport.GetPositionInfo(InstanceID=0))
			self.log("Heartbeat")
			
	def media(self, uri):
		if self.status == 1:
			self.log("New media: " + uri)
			self.device.SetAVTransportURI(InstanceID=0,CurrentURI=uri,CurrentURIMetaData= '')
			d.AVTransport.Play(InstanceID=0, Speed="1")
			d.AVTransport.Pause(InstanceID=0)
			d.AVTransport.Play(InstanceID=0, Speed="1")
			
	def play(self):
		if self.status == 1:
			self.log("Play function")
			self.device.AVTransport.Play(InstanceID=0, Speed='1')

	def run(self):
		
		self._status()
		self.connect(self.uri)
		
		while True:
			work, args = self.qi.get()
			
			self.log("Received command:"+ work)
			
			if work == 'stop':
				return
			
			if work == 'play':
				self.play()
				
			if work == 'pause':
				self.pause()
				
			if work == 'seek':
				self.seek(time)
				
			
				
			
	
