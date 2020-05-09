import asyncio
import ssdp
import socket

class MyProtocol(ssdp.SimpleServiceDiscoveryProtocol):

    def response_received(self, response, addr):
        print(response, addr)

    def request_received(self, request, addr):
        print(request, addr)


loop = asyncio.get_event_loop()
connect = loop.create_datagram_endpoint(MyProtocol, family=socket.AF_INET)
transport, protocol = loop.run_until_complete(connect)

notify = ssdp.SSDPRequest('NOTIFY')
notify.sendto(transport, (MyProtocol.MULTICAST_ADDRESS, 1982))

try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

transport.close()
loop.close()
