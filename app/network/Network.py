import sumolib

from app import Config
from colorama import Fore

import os
import sys

# import of SUMO_HOME
if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("please declare environment variable 'SUMO_HOME'")

class Network(object):
    """ simply ready the network in its raw form and creates a router on this network """

    # empty references to start with
    edges = None
    nodes = None
    nodeIds = None
    edgeIds = None

    tlsIds = []   
    @classmethod
    def loadNetwork(cls):
        """ loads the network and applies the results to the Network static class """
        # parse the net using sumolib
        parsedNetwork = sumolib.net.readNet(Config.sumoNet)
        # apply parsing to the network
        Network.__applyNetwork(parsedNetwork)

    @classmethod
    def __applyNetwork(cls, net):
        """ internal method for applying the values of a SUMO map """
        cls.nodeIds = map(lambda x: x.getID(), net.getNodes())  # type: list[str]
        cls.edgeIds = map(lambda x: x.getID(), net.getEdges())  # type: list[str]
        cls.nodes = net.getNodes()
        cls.edges = net.getEdges()
        
        cls.tls = cls.gettlsIds(net)

    @classmethod
    def nodesCount(cls):
        """ count the nodes """
        return len(cls.nodes)

    @classmethod
    def edgesCount(cls):
        """ count the edges """
        return len(cls.edges)

    @classmethod
    def gettlsIds(cls,net):
        """ get tls id list"""
        for tlsID in net._id2tls:
            cls.tlsIds.append(tlsID)
