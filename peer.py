# Peer pyTorrent
# Jesus Gracia & Miquel Sabate
# GEI URV 2016/2017
# Version 2.1
# Last-update 15.03.17

from pyactor.context import set_context, create_host, sleep, shutdown, serve_forever
from random import randint
import sys

class Peer(object):
        _tell = ['get_peers', 'announce', 'set_hash', 'init']
        _ask = []
        _ref = ['get_peers']

        torrent_hash = ""
        tracker=""
        neighbors=""
        data=""

        def init(self, torrent_hash):
            self.tracker = host.lookup_url('http://127.0.0.1:1277/tracker', 'Tracker', 'tracker')
            self.interval1 = self.host.interval(5, self.proxy, "announce", torrent_hash)
            # peer will send an announce every 5 seconds to tracker
            self.interval2 = self.host.interval(10, self.proxy, "get_peers")
            # peer will do the method get_peers every 10 seconds

        def announce(self, torrent_hash):
            self.torrent_hash = torrent_hash
            self.tracker.announce(torrent_hash, self.id)

        def get_peers(self):
            self.neighbors = self.tracker.get_peers(self.torrent_hash)
            print self.neighbors
            #for neig in self.neighbors:
                #print neig

        #def push(self):
            #rndm = randint(0, len(self.neighbors))
            #peerNeigh = host.lookup(self.neighbors[rndm])

        #def pull(self):


if __name__ == "__main__":
    set_context()
    rand = randint(1000, 1999)
    host = create_host('http://127.0.0.1:' + str(rand))

    peer = host.spawn('peer' + str(rand), Peer)

    if len(sys.argv) != 2:
        print "Error in the argument. Use: python peer.py torrent_hash"
        shutdown()
        exit()
    torrent_hash = str(sys.argv[1])
    peer.init(torrent_hash)

    serve_forever()
