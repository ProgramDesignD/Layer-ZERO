from direct.distributed.ServerRepository import ServerRepository
from panda3d.core import ConfigVariableInt

from repos.ai import AIRepository

class GameServerRepository(ServerRepository):
    def __init__(self):
        tcpPort = ConfigVariableInt('server-port', 4400).getValue()
        dcFileNames = ['repos/direct.dc','repos/model.dc']
        ServerRepository.__init__(self, tcpPort, dcFileNames=dcFileNames, threadedNet=True)

# all imports needed by the engine itself
from direct.showbase.ShowBase import ShowBase

# initialize the engine
base = ShowBase(windowType='none')

# instantiate the server
GameServerRepository()
AIRepository()

# start the server
base.run()