# youtube-dlna
YouTube video player for DLNA TV devices (MiraCast and similar)

Requirements:

- upnpclient
- youtube-dl

``` pip3 install upnpclient youtube-dl ```

Of course

- Python 3


Usage:

```./play.py [-d DEVICE_URL] -v https://youtube.com/watch...```

If no DEVICE_URL specified the device will be searched using SSDP. This is a bit slow... but you can copy the URL found in next attempts...

Tested on MiraScreen G2, should work in other cheap ass MiraCast dongles and clones, and clones of clones, and any AliExpress crap... enjoy!
