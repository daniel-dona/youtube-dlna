#!/usr/bin/env python3

import simple_ssdp as ssdp
import upnpclient
import time
import youtube_dl
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-v", dest='video', default="https://www.youtube.com/watch?v=dQw4w9WgXcQ", help="YouTube video URL")
parser.add_argument("-d", dest='dongle', default="search_it", help="YouTube video URL")

args = parser.parse_args()

ydl_opts = {

	}

ydl = youtube_dl.YoutubeDL(ydl_opts)

with ydl:
    result = ydl.extract_info(
        args.video,
        download=False # We just want to extract the info
    )

if result["_type"] == 'playlist':
	result = result['entries'][0] #Playlist TODO
	


if 'entries' in result:
    # Can be a playlist or a list of videos
    video = result['entries'][0]
else:
    # Just a video
    video = result
 
play_uri = None   
    
for f in video['formats']:
	if f['format_id'] == '22': ## Video y audio, 720p
		play_uri = f['url']
		
	if f['format_id'] == '18' and play_uri == None: ## Video y audio, 720p
		play_uri = f['url']


if play_uri == None:
	print(video['formats'])
	quit()

if args.dongle == 'search_it':

	print("Searching dongle...")

	disc = list(ssdp.discover("urn:schemas-upnp-org:device:MediaRenderer:1", retries=5, timeout=1))

	if len(disc) != 1:
		print("Oops! Not expected!")
		quit()

	uri = disc[0].getlocation() #Si detecta más de uno habría que implementar alguna forma de seleccionar

else:

	uri = args.dongle

print("Device location: ", uri)

d = upnpclient.Device(uri)

print("Device name: ", d.friendly_name)
print("UDN: ", d.udn)

d.AVTransport.Stop(InstanceID=0)
d.AVTransport.SetAVTransportURI(InstanceID=0,CurrentURI=play_uri,CurrentURIMetaData= '')
d.AVTransport.Play(InstanceID=0, Speed="1")
time.sleep(1)
d.AVTransport.Pause(InstanceID=0)
time.sleep(5)
d.AVTransport.Play(InstanceID=0, Speed="1")

print("Done!")



while True:
	info = d.AVTransport.GetPositionInfo(InstanceID=0)
	print("###### "+info['TrackDuration']+"/"+info['AbsTime']+" ######", end="\r", flush=True)
	time.sleep(1)



