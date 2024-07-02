from direct.distributed.ServerRepository import ServerRepository
from panda3d.core import ConfigVariableInt

class GameServerRepository(ServerRepository):
    def __init__(self):
        tcpPort = ConfigVariableInt('server-port', 4400).getValue()
        dcFileNames = ['model.dc']
        ServerRepository.__init__(self, tcpPort, dcFileNames=dcFileNames, threadedNet=True)